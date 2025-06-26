import cv2

# 문서 이미지 불러오기
img = cv2.imread('../img/barcode.jpg', cv2.IMREAD_GRAYSCALE)

# 다양한 이진화 방법
_, binary_fixed = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, binary_auto = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
binary_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

# 결과 비교
cv2.imshow('Original', img)
cv2.imshow('Fixed Threshold', binary_fixed)
cv2.imshow('Auto Threshold', binary_auto)
cv2.imshow('Adaptive Threshold', binary_adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Binarization completed!")