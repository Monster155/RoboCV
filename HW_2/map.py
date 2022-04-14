import cv2

img = cv2.imread('map.png')
scale = img.shape[0] / img.shape[1]
img = cv2.resize(img, (960, int(960 * scale)))


def draw_circle(event, x, y, flags, param):
    global is_not_first, last_pos, total_length
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if is_not_first:
            cv2.line(img, last_pos, (x, y), (255, 255, 0), 3)
            total_length += ((((x - last_pos[0]) ** 2) + ((y - last_pos[1]) ** 2)) ** 0.5)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        last_pos = (x, y)
        is_not_first = 1


is_not_first = 0
total_length = 0
last_pos = (0, 0)

cv2.imshow('img_warp', img)
cv2.setMouseCallback('img_warp', draw_circle)

while (1):
    cv2.imshow('img_warp', img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:  # ESC button in ASCII
        break

real_total_length = 555 / 175.82377541163197 * total_length
cv2.putText(img, "Total Length: " + str(round(real_total_length, 2)) + "m", (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
            (0, 0, 255), 2)
cv2.circle(img, last_pos, 5, (0, 255, 0), cv2.FILLED)
cv2.imshow('img_warp', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
