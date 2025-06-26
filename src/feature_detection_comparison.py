import cv2
import numpy as np

# 건물 이미지 불러오기
img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. 에지 검출
edges = cv2.Canny(gray, 100, 200)

# 2. 코너 검출
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
img_corners = img.copy()
if corners is not None:
    for corner in corners:
        x, y = int(corner[0][0]), int(corner[0][1])
        cv2.circle(img_corners, (x, y), 5, (0, 0, 255), -1)

# 3. 윤곽선 검출 (이진화 필요)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# 결과 확인
cv2.imshow('Original', img)
cv2.imshow('Edges', edges)
cv2.imshow('Corners', img_corners)
cv2.imshow('Contours', img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Detected corners: {len(corners) if corners is not None else 0}")
print(f"Detected contours: {len(contours)}")