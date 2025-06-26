import cv2

# 이미지 불러오기
img = cv2.imread('../img/cat.jpg')

# 불러오기 성공했는지 확인
if img is not None:
    print("Image loaded successfully!")
    print(f"Image size: {img.shape}")

    # 이미지 표시
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 다른 형식으로 저장
    cv2.imwrite('../result/cat_copy.jpg', img)
    cv2.imwrite('../result/cat_copy.png', img)
    print("Image saved successfully!")
else:
    print("Image file not found.")