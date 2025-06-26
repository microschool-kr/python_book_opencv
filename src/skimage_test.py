from skimage import io, filters
import matplotlib.pyplot as plt

# 이미지 읽기
img = io.imread('../img/cat.jpg', as_gray=True)

# 가장자리 검출
edges = filters.sobel(img)

# 결과 비교
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original')
axes[1].imshow(edges, cmap='gray')
axes[1].set_title('Edge Detection')
plt.show()