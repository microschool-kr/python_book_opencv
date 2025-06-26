import cv2
import os

# 이미지 불러오기
img = cv2.imread('../img/cat.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("=== Image Information ===")
print(f"Size: {img.shape}")
print(f"Total pixels: {img.size}")
print(f"Data type: {img.dtype}")
print(f"Darkest point: {img_gray.min()}")
print(f"Brightest point: {img_gray.max()}")
print(f"Average brightness: {img_gray.mean():.1f}")

# 파일 크기 비교
color_size = os.path.getsize('../img/cat.jpg')
cv2.imwrite('../temp_gray.jpg', img_gray)
gray_size = os.path.getsize('../temp_gray.jpg')

print(f"Color file size: {color_size} bytes")
print(f"Gray file size: {gray_size} bytes")
print(f"Size saved: {(color_size-gray_size)/color_size*100:.1f}%")