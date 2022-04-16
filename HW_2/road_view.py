import cv2
import numpy as np

img = cv2.imread("road.jpg")
# Dots sequence: Left Bottom - Right Bottom - Right Top - Left Top
scale = img.shape[0] / img.shape[1]
w = 640
h = int(scale * w)

img_warp = cv2.resize(img, (w, h))
img_warp_n_clear = cv2.resize(img, (w, h))


def draw_circle(event, x, y, flags, param):
    global dot_num, isAllDots
    if event == cv2.EVENT_LBUTTONDBLCLK:
        dot_num += 1
        if dot_num >= len(dots):
            return 0
        dots[dot_num] = [x, y]
        cv2.circle(img_warp, dots[dot_num], 3, (255, 255, 0), -1)
        # if dot_num == 0:
        # elif dot_num == 1:
        if dot_num == 1:
            cv2.line(img_warp, dots[dot_num - 1], dots[dot_num], (0, 255, 0), 1)
        elif dot_num == 2:
            cv2.line(img_warp, dots[dot_num - 1], dots[dot_num], (0, 255, 0), 1)
        elif dot_num == 3:
            cv2.line(img_warp, dots[dot_num - 1], dots[dot_num], (0, 255, 0), 1)
            cv2.line(img_warp, dots[0], dots[dot_num], (0, 255, 0), 1)
            print(dots)
            isAllDots = 1


isAllDots = 0
dot_num = -1
dots = [[0, 0], [0, 0], [0, 0], [0, 0]]
print(dots)

cv2.imshow('img_warp', img_warp)
cv2.setMouseCallback('img_warp', draw_circle)

while not isAllDots:
    cv2.imshow('img_warp', img_warp)
    cv2.waitKey(25)

dots2 = np.float32(dots)
pts2 = np.float32([[0, 0], [500, 0], [500, 400], [0, 400]])
M = cv2.getPerspectiveTransform(dots2, pts2)
img_result = cv2.warpPerspective(img_warp_n_clear, M, (500, 400))
cv2.imshow('img_warp_new', img_result)

cv2.waitKey(0)
