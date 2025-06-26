import matplotlib.pyplot as plt
from PIL import Image

# 이미지 불러오기
img = Image.open('../img/cat.jpg')

# 이미지 표시
plt.figure(figsize=(8, 6))
plt.imshow(img)
plt.title('Image Display with matplotlib')
plt.axis('off')
plt.show()
print("matplotlib image display completed!")