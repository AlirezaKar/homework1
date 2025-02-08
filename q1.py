import cv2 as cv
import numpy as np

img = cv.imread("image.jpg")
cv.imshow("Normal", img)
k = cv.waitKey(0)
# cv.destroyAllWindows()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
j = cv.waitKey(0)
# cv.destroyAllWindows()

# sift = cv.SIFT_create()
# kp1, des1 = sift.detectAndCompute(img, None)
# kp2, des2 = sift.detectAndCompute(gray, None)
# bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)
# matches = bf.match(des1, des2)
# matches = sorted(matches, key=lambda x: x.distance)

# img_matches = cv.drawMatches(img, kp1, gray, kp2, matches[:50], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# cv.waitKey(0)
# cv.destroyAllWindows()

# src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
# dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
# H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

# h1, w1 = img.shape[:2]
# h2, w2 = gray.shape[:2]

# pts = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
# dst = cv.perspectiveTransform(pts, H)
# gray_warped = cv.warpPerspective(gray, H, (w1 + w2, h1))
# gray_warped[0:h1, 0:w1] = img

# result = gray_warped
# cv.imshow('Result', result)
# cv.waitKey(0)
# cv.destroyAllWindows()