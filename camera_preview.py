"""OpenCV로 기본 카메라 영상을 읽어 창에 표시합니다."""

import cv2

# 내장·USB 카메라가 여러 대일 때 0, 1, … 로 바꿔 시도
CAMERA_INDEX = 0


def main() -> None:
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print(f"카메라를 열 수 없습니다. 인덱스 {CAMERA_INDEX}를 확인하세요.")
        return

    print("실시간 미리보기 중입니다. 'q' 키를 누르면 종료합니다.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽지 못했습니다.")
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
