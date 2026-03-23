"""OpenCV로 Lenna.png를 그레이스케일로 읽어 창에 표시합니다."""

import os

import cv2

# 스크립트가 있는 폴더 기준으로 이미지 경로 설정 (실행 위치와 무관)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "Lenna.png")


def main() -> None:
    img = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        print("Lenna.png 파일을 이 스크립트와 같은 폴더에 두었는지 확인하세요.")
        return

    cv2.imshow("Lena (Grayscale)", img)
    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
