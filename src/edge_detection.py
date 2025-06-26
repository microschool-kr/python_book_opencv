import cv2

# 건물 이미지 불러오기
img = cv2.imread('../img/architecture.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 다양한 임계값으로 에지 검출
edges_weak = cv2.Canny(gray, 50, 100)
edges_medium = cv2.Canny(gray, 100, 200)
edges_strong = cv2.Canny(gray, 150, 300)

# 결과 확인
cv2.imshow('Original', img)
cv2.imshow('Weak Edges', edges_weak)
cv2.imshow('Medium Edges', edges_medium)
cv2.imshow('Strong Edges', edges_strong)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 최적 결과 저장
cv2.imwrite('../result/architecture_edges.jpg', edges_medium)
print("Edge detection completed!")