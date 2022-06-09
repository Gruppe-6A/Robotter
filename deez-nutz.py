import cv2
import numpy as np
import pytesseract
import sys
from time import sleep


input_img = cv2.VideoCapture(0).read()[1]


def crop_num(img):
    # convert the image to HSV color space

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # find Otsu threshold on value channel (white can be any Hue/Satuation)
    ret, thresh_V = cv2.threshold(
        img_hsv[:, :, 2], 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # some morphology operation to clear unwanted spots
    kernel = np.ones((5, 5), np.uint8)
    thresh = thresh_V
    img_dilated = cv2.dilate(thresh, kernel, iterations=1)

    # find contours on the result above
    contours, hierarchy = cv2.findContours(
        img_dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    results = []
    contours = list(contours)
    contours.sort(key=lambda x: x[0, 0, 1])  # Sort by contours on y-axis
    for c in contours:
        # Loop through contours with an area larger than 500000
        if cv2.contourArea(c) > 500000:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.015 * peri, True)

            if len(approx) == 4:
                screenCnt = approx

            pts = screenCnt.reshape(4, 2)
            rect = np.zeros((4, 2), dtype="float32")

            s = pts.sum(axis=1)
            rect[0] = pts[np.argmin(s)]
            rect[2] = pts[np.argmax(s)]

            diff = np.diff(pts, axis=1)
            rect[1] = pts[np.argmin(diff)]
            rect[3] = pts[np.argmax(diff)]

            # Define top-left, top-right, bottom-right, bottom-left corner
            dst = np.array([[0, 0], [384, 0], [384, 600],
                           [0, 600]], dtype="float32")
            M = cv2.getPerspectiveTransform(rect, dst)
            warp = cv2.warpPerspective(img, M, (384, 600))

            warp = warp[15:88, 4:55]  # Crop card to number
            results.append(warp)

    return results


def read_images(imgs):
    config = ('-c tessedit_char_whitelist=0123456789AJQK -l eng --oem 1 --psm 8')
    results = []
    for i in imgs:

        # Ploting the image using matplotlib
        
        
        gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cv2.imshow('hello', thresh)
        # Blur and perform text extraction
        thresh = 255 - cv2.GaussianBlur(thresh, (5, 5), 0)
        text = pytesseract.image_to_string(thresh, config=config)
        results.append(text.strip("\n\x0c"))
    return results


def calc_hand_value(cards):
    value_lookup = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, '%': 3, 'i': 10}

    value = 0
    for c in cards:
        #value += value_lookup[c]
        value += value_lookup.get(c, 10)

    return value


#cropped = crop_num(input_img)
results = read_images([input_img])
print(results)
