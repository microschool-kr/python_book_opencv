import cv2

# OpenCV에 내장된 얼굴 인식 분류기 로딩
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지 불러오기
img = cv2.imread('../img/face_photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# 검출된 얼굴에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 결과 확인
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Found {len(faces)} faces!")