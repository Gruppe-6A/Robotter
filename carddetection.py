import numpy as np
import pytesseract
import cv2

tesseract_cmd = r'/usr/bin/tesseract'

def get_card_value():
    cap = cv2.VideoCapture(0)
    x  =0
    text = ''
    #while True:
    while(text not in ['0','1','2','3','4','5','6','7','8','9','A','J','Q','K']):
        ret, frame = cap.read()
        frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)
        frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)
        frame = frame[210:-85, 220:-270]
        
        #cv2.imshow('frame', frame)
        
            
        #config = ("-c tessedit"
        #          "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ0123456789")
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        thresh = 255 - cv2.GaussianBlur(thresh, (5, 5), 0)
        cv2.imshow('frame', thresh)
        #thresh = 255 - cv2.GaussianBlur(thresh, (5,5), 0)
        
        config = ('-l eng -c tessedit_char_whitelist=0123456789AJQK --oem 1 --psm 8')
        text = pytesseract.image_to_string(thresh, config=config).strip('\n\x0c')
        
    cap.release()
    cv2.destroyAllWindows()            
    return text

