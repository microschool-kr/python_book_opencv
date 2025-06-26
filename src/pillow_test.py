from PIL import Image

# 이미지 열기
img = Image.open('../img/cat.jpg')
print(f"Image size: {img.size}")
print(f"Image format: {img.format}")

# 크기 조정
resized = img.resize((256, 256))
resized.save('../result/cat_resized.jpg')
print("Image resizing completed!")