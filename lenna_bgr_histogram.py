"""Lenna.png를 BGR로 읽고 B·G·R 채널 히스토그램을 계산해 출력·표시합니다."""

import os

import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "Lenna.png")

HIST_W = 512
HIST_H = 400


def hist_to_polyline(hist: np.ndarray) -> np.ndarray:
    """히스토그램을 높이 HIST_H에 맞게 정규화한 뒤 polylines용 점 배열로 만듭니다."""
    hn = hist.copy()
    cv2.normalize(hn, hn, alpha=0, beta=HIST_H - 1, norm_type=cv2.NORM_MINMAX)
    pts = np.empty((256, 2), dtype=np.int32)
    for i in range(256):
        pts[i, 0] = int(i * (HIST_W - 1) / 255)
        pts[i, 1] = (HIST_H - 1) - int(np.clip(hn[i, 0], 0, HIST_H - 1))
    return pts


def main() -> None:
    bgr = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
    if bgr is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    if len(bgr.shape) != 3 or bgr.shape[2] != 3:
        print("BGR 3채널 이미지가 아닙니다.")
        return

    hist_b = cv2.calcHist([bgr], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([bgr], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([bgr], [2], None, [256], [0, 256])

    print("BGR 히스토그램 (채널별 빈 개수 최댓값이 나는 밝기)")
    for name, h in (("B", hist_b), ("G", hist_g), ("R", hist_r)):
        flat = h.flatten()
        peak = int(np.argmax(flat))
        print(f"  {name}: 밝기 {peak}에서 {int(flat[peak])} 픽셀 (최빈값)")

    hist_img = np.full((HIST_H, HIST_W, 3), 255, dtype=np.uint8)
    cv2.polylines(hist_img, [hist_to_polyline(hist_b)], False, (255, 0, 0), 2)
    cv2.polylines(hist_img, [hist_to_polyline(hist_g)], False, (0, 255, 0), 2)
    cv2.polylines(hist_img, [hist_to_polyline(hist_r)], False, (0, 0, 255), 2)

    cv2.imshow("Lenna (BGR)", bgr)
    cv2.imshow("Histogram BGR (B=파랑, G=초록, R=빨강 선)", hist_img)
    print("\n아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
