import cv2
from ultralytics import YOLO
from collections import defaultdict  # 기본값이 있는 딕셔너리

# YOLOv8 모델 로드 (사전 학습된 'yolov8n.pt' 파일 사용)
model = YOLO("yolov8n.pt")

# 웹캠 열기 (0번 웹캠)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # ret: 성공 여부, frame: 현재 캡처된 이미지
    if not ret:
        break  # 성공하지 않으면 종료

    # YOLO로 객체 탐지 (device="cpu": CPU로 연산)
    results = model(frame, device="cpu")

    # 탐지 결과를 그림 위에 나타냄
    annotated_frame = results[0].plot()

    # 탐지된 객체의 클래스별 개수 세기
    counts = defaultdict(int)
    names = results[0].names  # 클래스 이름 딕셔너리
    for box in results[0].boxes:
        class_id = int(box.cls)  # 클래스 ID 추출
        class_name = names[class_id]  # 클래스 이름 가져오기
        counts[class_name] += 1  # 개수 증가

    # 개수를 왼쪽 위에 표기
    y_offset = 30  # 첫 글자가 시작될 y 좌표
    for class_name, count in counts.items():
        text = f"{class_name}: {count}"  # 예: "person: 3"
        cv2.putText(
            annotated_frame,
            text,  # 출력할 글자
            (10, y_offset),  # 글자가 나타날 좌표 (x=10, y=y_offset)
            cv2.FONT_HERSHEY_PLAIN,  # 글씨 스타일
            1.5,  # 글씨 크기 (scale)
            (0, 255, 0),  # 글씨 색 (BGR 형식) - 연두색
            2,  # 글씨 두께
        )
        y_offset += 25  # 다음 글자가 아래로 25 픽셀 내려가도록 변경

    # 결과 화면 출력
    cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

    # 'q' 키를 누를 때 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 자원 정리
cap.release()  # 웹캠 종료
cv2.destroyAllWindows()  # 모든 창 닫기
