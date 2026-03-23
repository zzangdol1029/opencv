"""
candies.png를 읽고, BGR에서 R 성분이 임계값 이상인 픽셀만 남깁니다.

과제 요건 예시: cv2.split으로 채널 분리 후 cv2.inRange로 범위 마스크 생성.
"""

import os

import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 실제 파일명은 candies.png (대소문자만 다른 Candies.png와 동일할 수 있음)
IMAGE_PATH = os.path.join(BASE_DIR, "candies.png")

# BGR에서 R은 세 번째 채널. 이 값 이상인 픽셀만 남김 (낮추면 더 많이, 올리면 더 빨간 쪽만)
RED_MIN = 150


def main() -> None:
    bgr = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
    if bgr is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    # b, g, r 각각 높이×너비 단일 채널
    b, g, r = cv2.split(bgr)
    # inRange: 채널 값이 [RED_MIN, 255] 안이면 255, 아니면 0 (이진 마스크)
    mask = cv2.inRange(r, RED_MIN, 255)
    # 마스크가 255인 위치만 원본 색 유지, 나머지는 0(검정)
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
