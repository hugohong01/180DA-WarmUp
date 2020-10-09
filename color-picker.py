import numpy as np
import cv2

bgr = np.array([50,50,255])

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Define range of color
    upper = np.array([0,50,50])
    lower = np.array([50,50,50])
    upper_bgr = bgr + upper
    lower_bgr = bgr - lower

    # Threshold the image
    mask = cv2.inRange(frame, lower_bgr, upper_bgr)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
