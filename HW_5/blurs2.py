import cv2
import numpy as np

img_orig = cv2.imread("img.png")
img_orig = cv2.resize(img_orig, (80 * 5, 45 * 5))


def noisy(image, amount):
    s_vs_p = 0.5
    out = image.copy()
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[coords] = 255
    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[coords] = 0
    return out


def on_value_change(x):
    global img
    img = noisy(img_orig, (x + 10) / 100)
    pass


img = img_orig.copy()

cv2.namedWindow('slider')
cv2.createTrackbar('Power', 'slider', 1, 80, on_value_change)

while 1:
    img_resized = cv2.resize(img, (400, 225))
    cv2.imshow('image', img_resized)
    cv2.imshow("Averaging", cv2.blur(img_resized, (5, 5)))
    cv2.imshow("Gaussian", cv2.GaussianBlur(img_resized, (5, 5), 0))
    cv2.imshow("Median", cv2.medianBlur(img_resized, 5))
    cv2.imshow("Bilateral", cv2.bilateralFilter(img_resized, 9, 75, 75))

    k = cv2.waitKey(1)
    if k == 27:  # ESC button in ASCII
        break

cv2.destroyAllWindows()

# Edge detection
img_blur = cv2.GaussianBlur(img_resized, (5, 5), 0)
# img_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# Sobel
sobelx = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, 5)
sobely = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, 5)
sobelxy = cv2.Sobel(img_blur, cv2.CV_64F, 1, 1, 5)

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel X and Y', sobelxy)

# Laplacian
laplacian = cv2.Laplacian(img_blur, cv2.CV_64F)

cv2.imshow('Laplacian', laplacian)

# Scharr
scharrX = cv2.Scharr(img_blur, cv2.CV_32F, 1, 0)
scharrY = cv2.Scharr(img_blur, cv2.CV_32F, 0, 1)

cv2.imshow('Scharr X', scharrX)
cv2.imshow('Scharr Y', scharrY)

# Canny
edges = cv2.Canny(img_blur, 100, 200)

cv2.imshow('Canny', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
