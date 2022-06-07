import numpy as np
import cv2

imageTarget = cv2.imread("box.jpeg")
imageTarget = cv2.resize(imageTarget, [400, int(400 * imageTarget.shape[0] / imageTarget.shape[1])])

videoCamera = cv2.VideoCapture(0)
videoTarget = cv2.VideoCapture("movie.mp4")

hT, wT, cT = imageTarget.shape

sift = cv2.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

kp1, dsc1 = sift.detectAndCompute(imageTarget, None)
# imageTarget = cv2.drawKeypoints(imageTarget, kp1, None)

while True:
    videoCameraSuccess, videoCameraImage = videoCamera.read()
    videoTargetSuccess, videoTargetImage = videoTarget.read()
    if not videoTargetSuccess:
        videoTarget = cv2.VideoCapture("movie.mp4")
        videoTargetSuccess, videoTargetImage = videoTarget.read()

    videoCameraImage = cv2.resize(videoCameraImage, [wT, hT])
    videoTargetImage = cv2.resize(videoTargetImage, [wT, hT])

    kp2, dsc2 = sift.detectAndCompute(videoCameraImage, None)
    # videoCameraImage = cv2.drawKeypoints(videoCameraImage, kp2, None)

    matches = bf.match(dsc1, dsc2)
    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:300]

    imgFeatures = cv2.drawMatches(imageTarget, kp1, videoCameraImage, kp2, good_matches, None)

    if len(good_matches) > 30:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        matrix, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        pts = np.float32([[0, 0], [0, hT], [wT, hT], [wT, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)
        dst += (wT, 0)

        imgFeatures = cv2.polylines(imgFeatures, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

        imgWarp = cv2.warpPerspective(videoTargetImage, matrix, [wT, hT])

        dst -= (wT, 0)
        newMask = np.zeros([hT, wT], np.uint8)
        cv2.fillPoly(newMask, [np.int32(dst)], (255, 255, 255))

        newMaskInv = cv2.bitwise_not(newMask)
        bitwise = cv2.bitwise_and(videoCameraImage, videoCameraImage, mask=newMaskInv)
        result = cv2.bitwise_or(bitwise, imgWarp)

        # warpAndMask = np.concatenate((imgWarp, newMask), axis=1)
        # imgFeatures = np.concatenate((imgFeatures, warpAndMask), axis=0)
        cv2.imshow("RESULT", result)
        cv2.imshow("Image Warp", imgWarp)
        cv2.imshow("Mask", newMask)
        cv2.imshow("Image Features", imgFeatures)
        cv2.imshow("Bitwise", bitwise)

    # cv2.imshow("Image Target", imageTarget)
    # cv2.imshow("Video Camera", videoCameraImage)
    # cv2.imshow("Video Target", videoTargetImage)

    cv2.waitKey(5)
