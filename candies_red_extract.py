"""candies.png를 읽고, BGR에서 R 성분이 임계값 이상인 픽셀만 남깁니다 (split + inRange)."""

import os

import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 실제 파일명은 candies.png (대소문자만 다른 Candies.png와 동일할 수 있음)
IMAGE_PATH = os.path.join(BASE_DIR, "candies.png")

# Red(BGR의 세 번째 채널)가 이 값 이상인 픽셀만 추출 — 필요에 따라 숫자만 바꾸면 됩니다.
RED_MIN = 150


def main() -> None:
    bgr = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
    if bgr is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    b, g, r = cv2.split(bgr)
    # R 채널만 검사: RED_MIN ~ 255 범위 → 마스크 (0 또는 255)
    mask = cv2.inRange(r, RED_MIN, 255)
    # 마스크가 255인 위치만 원본 색 유지, 나머지는 검정
    extracted = cv2.bitwise_and(bgr, bgr, mask=mask)

    print(f"R >= {RED_MIN} 인 픽셀만 표시합니다. (cv2.split → R 채널, cv2.inRange)")
    cv2.imshow("Original (BGR)", bgr)
    cv2.imshow("R channel", r)
    cv2.imshow("Mask (R in range)", mask)
    cv2.imshow("Extracted (red-strong only)", extracted)
    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
