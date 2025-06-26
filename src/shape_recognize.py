import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('../img/shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이진화
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 윤곽선 찾기
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 도형 분류
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            shape = "Rectangle"
        else:
            shape = "Circle"

        cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
        cv2.putText(img, shape, (contour[0][0][0], contour[0][0][1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow('Shape Classification', img)
cv2.waitKey(0)
cv2.destroyAllWindows()