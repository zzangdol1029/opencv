"""candies.png에서 HSV 색 공간으로 붉은색 캔디만 추출합니다."""

import os

import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "candies.png")

# OpenCV HSV: H 0~179, S·V 0~255. 빨강은 H가 0 근처와 179 근처 두 덩어리로 나뉩니다.
LOW_RED_H_MAX = 15
HIGH_RED_H_MIN = 155
S_MIN = 90
V_MIN = 60


def main() -> None:
    bgr = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
    if bgr is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    lower1 = np.array([0, S_MIN, V_MIN], dtype=np.uint8)
    upper1 = np.array([LOW_RED_H_MAX, 255, 255], dtype=np.uint8)
    lower2 = np.array([HIGH_RED_H_MIN, S_MIN, V_MIN], dtype=np.uint8)
    upper2 = np.array([179, 255, 255], dtype=np.uint8)

    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    mask = cv2.bitwise_or(mask1, mask2)

    extracted = cv2.bitwise_and(bgr, bgr, mask=mask)

    print("HSV 기준 붉은색 마스크 (저각도·고각도 OR). 필요하면 상단 상수로 미세 조정하세요.")
    cv2.imshow("Original", bgr)
    cv2.imshow("Red mask", mask)
    cv2.imshow("Red candies only", extracted)
    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
