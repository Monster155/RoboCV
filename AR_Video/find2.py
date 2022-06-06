import numpy as np
import cv2

img1 = cv2.imread('chess.png')
img2 = cv2.imread('test3.jpg')
img1 = cv2.resize(img1, (int(img1.shape[1] / 2), int(img1.shape[0] / 2)))
img2 = cv2.resize(img2, (int(img2.shape[1] / 2), int(img2.shape[0] / 2)))

sift = cv2.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

matches = bf.match(descriptors1, descriptors2)
matches = sorted(matches, key=lambda x: x.distance)
good_matches = matches[:100]

src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
matchesMask = mask.ravel().tolist()

h, w = img1.shape[:2]
pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

dst = cv2.perspectiveTransform(pts, M)
dst += (w, 0)

img3 = cv2.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, None)
img3 = cv2.polylines(img3, [np.int32(dst)], True, (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow("result", img3)

#

img_t = cv2.imread("tiger.jpeg")
img_t = cv2.resize(img_t, (int(img_t.shape[1] / 2), int(img_t.shape[0] / 2)))
points2 = np.float32([
    [img_t.shape[1], 0],
    [0, 0],
    [0, img_t.shape[0]],
    [img_t.shape[1], img_t.shape[0]]
])

M = cv2.getPerspectiveTransform(points2, dst)
img_pers_t = cv2.warpPerspective(img_t, M, [img3.shape[1], img3.shape[0]])

cv2.imshow("tiger", img_pers_t)

cont = np.array(dst, np.int32).reshape((-1, 1, 2))
mask = np.zeros(img_pers_t.shape, dtype=img_pers_t.dtype)
mask = cv2.fillPoly(mask, [cont], (255))
cv2.imshow("mask", mask)

for i in range(0, img_pers_t.shape[0]):
    for j in range(0, img_pers_t.shape[1]):
        if mask[i, j][0] != 0:
            img3[i, j] = img_pers_t[i, j]
cv2.imshow("res", img3)

cv2.waitKey(0)
