import cv2
import numpy as np

# 전역 변수 (클릭한 점들을 저장)
clicked_points = []
img_copy = None

def mouse_click(event, x, y, flags, param):
    """마우스 클릭 이벤트 처리 함수"""
    global clicked_points, img_copy
    
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 클릭
        if len(clicked_points) < 4:
            clicked_points.append([x, y])
            print(f"Point {len(clicked_points)}: ({x}, {y})")
            
            # 클릭한 점에 원 그리기 (빨간색)
            cv2.circle(img_copy, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('Card Image - Click 4 corners', img_copy)

def transform_card():
    """카드를 정면으로 변환하는 함수"""
    global clicked_points, img_copy
    
    # 이미지 불러오기
    img = cv2.imread('../img/card.jpg')
    if img is None:
        print("이미지를 찾을 수 없습니다. 파일 경로를 확인하세요.")
        return
    
    img_copy = img.copy()
    height, width = img.shape[:2]
    
    print("=== 카드 정면 변환 프로그램 ===")
    print("1. 카드의 네 꼭지점을 시계방향으로 클릭하세요")
    print("   (왼쪽 위 → 오른쪽 위 → 오른쪽 아래 → 왼쪽 아래)")
    print("2. 4개 점을 모두 클릭하면 자동으로 변환됩니다")
    print("3. ESC 키를 누르면 종료합니다")
    
    # 이미지 창 생성 및 마우스 이벤트 연결
    cv2.imshow('Card Image - Click 4 corners', img_copy)
    cv2.setMouseCallback('Card Image - Click 4 corners', mouse_click)
    
    # 사용자가 4개 점을 클릭할 때까지 대기
    while len(clicked_points) < 4:
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC 키
            print("프로그램을 종료합니다.")
            cv2.destroyAllWindows()
            return
    
    print("\n4개 점이 모두 선택되었습니다. 변환을 시작합니다...")
    
    # 클릭한 점들을 numpy 배열로 변환
    src_points = np.float32(clicked_points)
    
    # 변환될 목표 사각형 크기 설정 (카드 비율 고려)
    card_width = 400   # 변환 후 카드 가로 크기
    card_height = 250  # 변환 후 카드 세로 크기
    
    # 목표 사각형의 꼭지점 (정면에서 본 카드 모양)
    dst_points = np.float32([
        [0, 0],                           # 왼쪽 위
        [card_width, 0],                  # 오른쪽 위
        [card_width, card_height],        # 오른쪽 아래
        [0, card_height]                  # 왼쪽 아래
    ])
    
    # 원근 변환 행렬 계산
    transform_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    
    # 원근 변환 수행
    transformed = cv2.warpPerspective(img, transform_matrix, (card_width, card_height))
    
    # 결과 비교 표시
    cv2.imshow('Original (with points)', img_copy)
    cv2.imshow('Transformed Card', transformed)
    
    # 결과 저장
    cv2.imwrite('../result/card_transformed.jpg', transformed)
    print("변환된 카드가 '../result/card_transformed.jpg'로 저장되었습니다.")
    
    print("\n아무 키나 누르면 프로그램이 종료됩니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 프로그램 실행
if __name__ == "__main__":
    transform_card()