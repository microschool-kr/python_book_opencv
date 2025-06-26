import cv2
from ultralytics import YOLO

# YOLOv8 모델 로드
model = YOLO("yolov8n.pt")

# 웹캠 열기 (0번 카메라)
cap = cv2.VideoCapture(0)

# 웹캠 해상도를 낮게 설정하여 처리 속도 향상
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 너비 640픽셀로 설정
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 높이 480픽셀로 설정

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 객체 탐지 수행
    results = model(frame, device="cpu")

    # 결과 시각화 (bounding box 등 그리기)
    annotated_frame = results[0].plot()

    # 결과 프레임 화면에 표시
    cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
