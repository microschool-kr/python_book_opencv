import cv2

# 이미지 불러오기
img = cv2.imread('../img/cat.jpg')
height, width = img.shape[:2]

# 회전 중심점 (이미지 중앙)
center = (width // 2, height // 2)

# 90도, 180도 회전
rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_180 = cv2.rotate(img, cv2.ROTATE_180)

# 임의 각도 회전 (30도)
rotation_matrix = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated_30 = cv2.warpAffine(img, rotation_matrix, (width, height))

# 결과 확인
cv2.imshow('Original', img)
cv2.imshow('90 Degrees', rotated_90)
cv2.imshow('30 Degrees', rotated_30)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Rotation completed!")