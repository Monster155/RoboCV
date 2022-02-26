import cv2
import numpy as np

img_warp = cv2.imread("cats.jpg")
height, width, channels = img_warp.shape
scale = height / width
img_warp = cv2.resize(img_warp, (960, int(960 * scale)))
img_copy = img_warp.copy()

dots = np.array([[0, 0], [0, 0], [0, 0], [0, 0]])
count = 0


def draw_circle(event, x, y, flags, param):
    global count
    global img_warp
    if event == cv2.EVENT_LBUTTONDBLCLK:
        dots[count % 4] = [x, y]
        count += 1
        if count < 4:
            for i in range(0, count):
                cv2.circle(img_warp, (dots[i][0], dots[i][1]), 3, (255, 255, 0), -1)
        else:
            img_warp = img_copy.copy()
            for i in range(0, 4):
                cv2.circle(img_warp, (dots[i][0], dots[i][1]), 3, (255, 255, 0), -1)


cv2.imshow('img_warp', img_warp)
cv2.setMouseCallback('img_warp', draw_circle)

while (1):
    cv2.imshow('img_warp', img_warp)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:  # ESC button in ASCII
        # TODO check is rect https://stackoverflow.com/questions/2303278/find-if-4-points-on-a-plane-form-a-rectangle
        break

width, height = 250, 350
pts1 = np.float32(dots)
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img_warp, matrix, (width, height))
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)
