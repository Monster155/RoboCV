import cv2

img = cv2.imread('img.jpg')
height, width, channels = img.shape
scale = height / width
img = cv2.resize(img, (960, int(960 * scale)))
height, width, channels = img.shape

x = 5
y = 5

pieceX = int(width / x)
pieceY = int(height / y)

for i in range(0, x):
    for j in range(0, y):
        x1 = i * pieceX
        x2 = (i + 1) * pieceX
        if x2 > width:
            x2 = width

        y1 = j * pieceY
        y2 = (j + 1) * pieceY
        if y2 > height:
            y2 = height
        # cv2.imshow('image' + str(i) + ':' + str(j), img[y1:y2, x1:x2])
        cv2.imwrite('D:/Projects/PyCharmProjects/Projects/crop/cropped/image' + str(i) + '-' + str(j) + '.jpg',
                    img[y1:y2, x1:x2])

cv2.imshow('image', img)
cv2.waitKey(0)
