"""candies.png에서 HSV로 파란색 캔디만 추출합니다. (힌트: H 100~140)"""

import os

import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "candies.png")

BLUE_H_MIN = 100
BLUE_H_MAX = 140
S_MIN = 80
V_MIN = 60


def main() -> None:
    bgr = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
    if bgr is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    lower = np.array([BLUE_H_MIN, S_MIN, V_MIN], dtype=np.uint8)
    upper = np.array([BLUE_H_MAX, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)
    extracted = cv2.bitwise_and(bgr, bgr, mask=mask)

    print(f"HSV 파랑 구간: H [{BLUE_H_MIN}, {BLUE_H_MAX}], S≥{S_MIN}, V≥{V_MIN}")
    cv2.imshow("Original", bgr)
    cv2.imshow("Blue mask", mask)
    cv2.imshow("Blue candies only", extracted)
    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
