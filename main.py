import cv2
import numpy as np
import math


frameWidth = 1200
frameHeight = 900

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break














