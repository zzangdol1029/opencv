"""OpenCV로 test_video.mp4를 읽어 창에 재생합니다."""

import os

import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(BASE_DIR, "test_video.mp4")


def main() -> None:
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"동영상을 열 수 없습니다: {VIDEO_PATH}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    delay_ms = max(1, int(1000 / fps)) if fps and fps > 0 else 33

    print("재생 중… 창을 닫거나 'q' 키를 누르면 종료합니다.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("test_video", frame)
        if cv2.waitKey(delay_ms) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
