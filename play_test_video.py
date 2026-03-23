"""
OpenCV로 test_video.mp4를 읽어 창에 재생합니다.

VideoCapture로 프레임 단위로 읽고, imshow로 연속 표시하면 동영상처럼 보입니다.
"""

import os

import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(BASE_DIR, "test_video.mp4")


def main() -> None:
    # 파일 경로 또는 카메라 인덱스(0,1,…)를 인자로 줄 수 있음
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"동영상을 열 수 없습니다: {VIDEO_PATH}")
        return

    # 초당 프레임 수 (메타데이터; 0이면 알 수 없음 → 아래에서 기본 지연 사용)
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 한 프레임당 대기 시간(ms): 실제 재생 속도에 가깝게 맞춤
    delay_ms = max(1, int(1000 / fps)) if fps and fps > 0 else 33

    print("재생 중… 창을 닫거나 'q' 키를 누르면 종료합니다.")
    while True:
        # ret: 성공 여부, frame: BGR 이미지 (numpy 배열)
        ret, frame = cap.read()
        if not ret:
            break  # 파일 끝 또는 읽기 실패
        cv2.imshow("test_video", frame)
        # & 0xFF: 플랫폼별로 상위 비트가 섞일 수 있어 ASCII 키만 비교
        if cv2.waitKey(delay_ms) & 0xFF == ord("q"):
            break

    cap.release()  # 파일/디바이스 핸들 반환
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
