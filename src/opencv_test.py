import cv2

# 이미지 불러오기
img = cv2.imread('../img/cat.jpg')

# OpenCV 정보 확인
print(f"OpenCV version: {cv2.__version__}")
print(f"Image size: {img.shape}")

# 이미지 표시
cv2.imshow('OpenCV Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()