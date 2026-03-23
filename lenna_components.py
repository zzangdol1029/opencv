"""OpenCV로 Lenna.png를 읽고 B·G·R 각 색 성분을 콘솔에 출력하고 창으로 표시합니다."""

import os

import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "Lenna.png")


def main() -> None:
    img = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
    if img is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    if len(img.shape) != 3 or img.shape[2] != 3:
        print("BGR 3채널 컬러 이미지가 아닙니다.")
        return

    b, g, r = cv2.split(img)

    h, w = img.shape[:2]
    print("--- Lenna.png 픽셀 성분 (OpenCV 기본 순서: B, G, R) ---")
    print(f"크기: {w} x {h}, dtype: {img.dtype}")
    for name, ch in (("B (파랑)", b), ("G (초록)", g), ("R (빨강)", r)):
        print(
            f"  {name}: min={int(ch.min())}, max={int(ch.max())}, "
            f"mean={ch.mean():.2f}"
        )

    cv2.imshow("Original (BGR)", img)
    cv2.imshow("B channel", b)
    cv2.imshow("G channel", g)
    cv2.imshow("R channel", r)
    print("\n창이 네 개 열립니다. 아무 키나 누르면 모두 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
