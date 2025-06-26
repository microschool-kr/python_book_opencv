import cv2

# 이미지 불러오기
img = cv2.imread('../img/city.jpg')

# 다양한 블러 효과
blur_basic = cv2.blur(img, (15, 15))
blur_gaussian = cv2.GaussianBlur(img, (15, 15), 0)
blur_median = cv2.medianBlur(img, 15)

# 결과 비교
cv2.imshow('Original', img)
cv2.imshow('Basic Blur', blur_basic)
cv2.imshow('Gaussian Blur', blur_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 결과 저장
cv2.imwrite('../result/city_blurred.jpg', blur_gaussian)
print("Blur effect applied successfully!")