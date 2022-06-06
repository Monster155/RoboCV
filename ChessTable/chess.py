import cv2
import numpy as np

img = cv2.imread("test.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

image_copy = img.copy()
cv2.drawContours(image_copy, contours, 0, (0, 255, 0), -1)

mask = np.zeros(img.shape[:2], dtype=img.dtype)
cv2.drawContours(mask, contours, 0, (255), -1)
cv2.imshow("Mask", mask)
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Result", result)

cv2.imshow('None approximation', cv2.resize(image_copy, [96 * 4, 128 * 4]))

x, y, w, h = cv2.boundingRect(contours[0])
img_cropped = img[y:y + h, x:x + w].copy()
cv2.imshow('Cropped', cv2.resize(img_cropped, [96 * 4, 128 * 4]))

cv2.waitKey()
