"""
OpenCV로 Lenna.png를 그레이스케일로 읽어 창에 표시합니다.

- cv2.imread: 파일 → numpy 배열(이미지)
- cv2.imshow / waitKey / destroyAllWindows: GUI 창에 표시하고 키 입력 대기
"""

import os

import cv2

# 스크립트 파일이 있는 폴더 = 기준 경로 (터미널에서 다른 폴더에 있어도 이미지를 찾을 수 있음)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "Lenna.png")


def main() -> None:
    # IMREAD_GRAYSCALE(=0): 컬러여도 읽을 때 1채널(흑백)로 변환
    img = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        print("Lenna.png 파일을 이 스크립트와 같은 폴더에 두었는지 확인하세요.")
        return

    # 첫 번째 인자: 창 제목(문자열), 두 번째: 표시할 이미지 배열
    cv2.imshow("Lena (Grayscale)", img)
    print("아무 키나 누르면 창이 닫힙니다.")
    # waitKey(0): 키 입력이 있을 때까지 무한 대기 (밀리초를 주면 그 시간만 대기)
    cv2.waitKey(0)
    # 열린 모든 HighGUI 창 해제
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
