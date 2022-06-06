import cv2

sift = cv2.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, True)

img1 = cv2.imread('test2.jpg')
img2 = cv2.imread('chess.png')
img1 = cv2.resize(img1, (int(img1.shape[1] / 2), int(img1.shape[0] / 2)))
img2 = cv2.resize(img2, (int(img2.shape[1] / 2), int(img2.shape[0] / 2)))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

matches = bf.match(descriptors_1, descriptors_2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:300], img2, 2)
cv2.imshow('SIFT', img3)

cv2.waitKey(0)
