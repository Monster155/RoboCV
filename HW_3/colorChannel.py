import math

import cv2
import numpy as np

img = np.ones((512, 512 + 256, 3), np.uint8)
img.fill(255)


def drawCircle(value):
    for x in range(512):
        for y in range(512):
            ox = x - 256
            oy = y - 256

            h = math.atan2(ox, oy)
            if h < 0:
                h = 2 * math.pi + h
            h *= 180 / (2 * math.pi)

            s = int(math.sqrt((0 - ox) * (0 - ox) + (0 - oy) * (0 - oy)))

            v = value
            if s > 255:
                v = 0

            img[x, y] = (h, s, v)


def drawLine(hue):
    for x in range(50):
        for y in range(256):
            img[y + 256 - 128, x + 512 + 128 - 25] = (0, 0, 255 - y)


def drawResult(h, s, v):
    cv2.rectangle(img, (512 + 128 - 30, 512 - 30), (512 + 128 + 30, 512 - 90), (int(h), int(s), int(v)), cv2.FILLED)


def onClick(event, x, y, flags, param):
    global cH, cS, cV
    if event == cv2.EVENT_LBUTTONDBLCLK:
        drawCircle(cV)
        drawLine(cH)
        drawResult(cH, cS, cV)

        (h, s, v) = img[y, x]

        if x <= 512:
            drawCircle(cV)
            drawLine(h)
            drawResult(h, s, cV)
            cH = h
            cS = s
            cv2.circle(img, (x, y), 1, (255 - int(h), 255 - int(s), 255 - int(v)), cv2.FILLED)
        else:
            drawCircle(v)
            drawLine(cH)
            drawResult(cH, cS, v)
            cv2.rectangle(img, (512 + 128 - 25, y), (512 + 128 + 25, y), (255 - int(h), 255 - int(s), 255 - int(v)), cv2.FILLED)
            cV = v

        cv2.imshow("HSV Color Picker", cv2.cvtColor(img, cv2.COLOR_HSV2BGR))


cH = 0
cS = 255
cV = 255

drawCircle(255)
drawLine(0)
cv2.imshow("HSV Color Picker", cv2.cvtColor(img, cv2.COLOR_HSV2BGR))
cv2.setMouseCallback('HSV Color Picker', onClick)

while 1:
    cv2.waitKey(20)

# cv2.destroyAllWindows()
