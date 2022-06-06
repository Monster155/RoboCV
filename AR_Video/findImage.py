import cv2

sift = cv2.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, True)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    suc, img1 = cap.read()
    img2 = cv2.imread('chess.png')

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

    matches = bf.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)

    img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:300], img2, 2)
    cv2.imshow('SIFT', img3)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
