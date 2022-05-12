import cv2
import numpy as np

img = cv2.imread("img.png")
cv2.imshow("Original", img)

# Averaging -----------------------

# averaging = np.ones((5, 5), np.float32) / 25
# averaging_blur = cv2.filter2D(img, -1, averaging)

averaging_blur = cv2.blur(img, (5, 5))

cv2.imshow("Averaging Blur", averaging_blur)

# -----------------------

"""kernel_1 = np.array([[0, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]])

identity = cv2.filter2D(img, -1, kernel_1)

cv2.imshow("Identity", identity)"""

# Gaussian-----------------------

gaussian = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("Gaussian Blur", gaussian)

# Median-----------------------

median = cv2.medianBlur(img, 5)

cv2.imshow("Median Blur", median)

# Bilateral-----------------------

bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Bilateral Blur", bilateral)

# -----------------------

cv2.waitKey(0)
cv2.destroyAllWindows()
