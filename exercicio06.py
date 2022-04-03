import cv2
import numpy as np

color = cv2.imread('einsteinColor.webp')
gray = cv2.imread('einsteinColor.webp', 2)

backToGray = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
ret, backToBlack = cv2.threshold(backToGray, 127, 255, cv2.THRESH_BINARY)
resp = np.concatenate((color, backToGray, backToBlack), axis = 1)
cv2.imshow('Imagens Concatenadas', resp)
cv2.waitKey(0)

