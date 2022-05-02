import cv2

img = cv2.imread("lion.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
HSV_2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)

cv2.imshow("Original", img)
cv2.imshow("RGB", RGB)
cv2.imshow("gray", gray)
cv2.imshow("Lab", Lab)
cv2.imshow("YCrCb", YCrCb)
cv2.imshow("HSV", HSV)
cv2.imshow("HSV_2", HSV_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
