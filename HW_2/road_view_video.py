import cv2
import numpy as np

cap = cv2.VideoCapture('road_movie.mp4')

ret, frame = cap.read()
scale = frame.shape[0] / frame.shape[1]
w = 640
h = int(scale * w)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# out = cv2.VideoWriter('road_movie_out.mp4', fourcc, 30.0, (w, h))

img_warp = cv2.resize(frame, (w, h))


def draw_circle(event, x, y, flags, param):
    global dot_num
    if event == cv2.EVENT_LBUTTONDBLCLK:
        dot_num += 1
        if dot_num >= len(dots):
            return 0
        dots[dot_num] = [x, y]
        cv2.circle(img_warp, dots[dot_num], 3, (255, 255, 0), -1)
        if dot_num == 1:
            cv2.line(img_warp, dots[dot_num - 1], dots[dot_num], (0, 255, 0), 1)
        elif dot_num == 2:
            cv2.line(img_warp, dots[dot_num - 1], dots[dot_num], (0, 255, 0), 1)
        elif dot_num == 3:
            cv2.line(img_warp, dots[dot_num - 1], dots[dot_num], (0, 255, 0), 1)
            cv2.line(img_warp, dots[0], dots[dot_num], (0, 255, 0), 1)


dot_num = -1
dots = [[0, 0], [0, 0], [0, 0], [0, 0]]

cv2.imshow('img_warp', img_warp)
cv2.setMouseCallback('img_warp', draw_circle)

while dot_num < len(dots):
    cv2.imshow('img_warp', img_warp)
    cv2.waitKey(25)

dots2 = np.float32(dots)
pts2 = np.float32([[0, 0], [500, 0], [500, 300], [0, 300]])
M = cv2.getPerspectiveTransform(dots2, pts2)

while cap.isOpened():
    if ret:
        vidout = cv2.resize(frame, (w, h))
        # out.write(vidout)

        img_result = cv2.warpPerspective(vidout, M, (500, 300))
        img_result = cv2.flip(img_result, 0)
        cv2.imshow('img_warp_new', img_result)
        cv2.waitKey(1)

    else:
        break
    ret, frame = cap.read()

cap.release()
# out.release()

cv2.waitKey(0)

cv2.destroyAllWindows()
