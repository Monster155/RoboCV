import cv2
import numpy as np

img = cv2.imread("img.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

image_copy = img.copy()
cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)

mask = np.zeros_like(img)
out = np.zeros_like(img)
out[mask == 255] = img[mask == 255]

cv2.imshow('None approximation', image_copy)

x, y, w, h = cv2.boundingRect(contours[1])
img_cropped = img[y:y + h, x:x + w].copy()
cv2.imshow('Cropped', img_cropped)


def nothing(scale):
    global img_result
    img_result = img.copy()
    scale /= 10
    scale += .01  # disable scale = 0 error
    sW = int(w * scale)
    sH = int(h * scale)
    sX = int(x + w / 2 - sW / 2)
    sY = int(y + h / 2 - sH / 2)
    img_result[sY:sY + sH, sX:sX + sW] = cv2.resize(img_cropped, (sW, sH))


img[y:y + h, x:x + w] = 255
img_result = img.copy()

cv2.namedWindow('slider')
cv2.createTrackbar('scale', 'slider', 0, 10, nothing)

while 1:
    cv2.imshow('Result', img_result)
    k = cv2.waitKey(1)
    if k == 27:  # ESC button in ASCII
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
