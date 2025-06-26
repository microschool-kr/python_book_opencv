import cv2

# 컬러 이미지 불러오기
img_color = cv2.imread('../img/cat.jpg')

# 흑백으로 변환
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# 흑백을 다시 컬러로 변환 (시각적으로만)
img_gray_3ch = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

print(f"Color image: {img_color.shape}")
print(f"Grayscale image: {img_gray.shape}")
print(f"Gray to color: {img_gray_3ch.shape}")

# 결과 비교
cv2.imshow('Color', img_color)
cv2.imshow('Grayscale', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 저장
cv2.imwrite('../result/cat_gray.jpg', img_gray)
print("Color conversion completed!")