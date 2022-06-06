import cv2
import numpy as np

# Shi Tomas
img = cv2.imread('test.jpg')
img = cv2.resize(img, [85 * 3, 120 * 3])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (5, 5))

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow("Image", img)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Harris
img = cv2.imread("test.jpg")
img = cv2.resize(img, [85 * 3, 120 * 3])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
