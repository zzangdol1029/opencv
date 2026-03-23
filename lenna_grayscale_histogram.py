"""Lenna.png를 그레이스케일로 읽고 히스토그램을 계산해 창에 표시합니다."""

import os

import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "Lenna.png")

HIST_W = 512
HIST_H = 400


def draw_histogram_gray(hist: np.ndarray) -> np.ndarray:
    """256-bin 그레이 히스토그램을 막대 그래프 이미지로 그립니다."""
    hist_norm = hist.copy()
    cv2.normalize(hist_norm, hist_norm, alpha=0, beta=HIST_H - 1, norm_type=cv2.NORM_MINMAX)

    img = np.zeros((HIST_H, HIST_W), dtype=np.uint8)
    bin_w = max(1, int(round(HIST_W / 256)))
    for i in range(256):
        h_bin = int(np.clip(hist_norm[i, 0], 0, HIST_H - 1))
        x0 = i * bin_w
        x1 = min(HIST_W - 1, (i + 1) * bin_w - 1)
        cv2.rectangle(img, (x0, HIST_H - 1), (x1, HIST_H - 1 - h_bin), 255, thickness=-1)
    return img


def main() -> None:
    gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    print("그레이스케일 히스토그램 (0~255, 빈 개수 상위 5개)")
    flat = hist.flatten()
    top = np.argsort(flat)[-5:][::-1]
    for idx in top:
        print(f"  밝기 {idx}: {int(flat[idx])} 픽셀")

    hist_vis = draw_histogram_gray(hist)

    cv2.imshow("Lenna (Grayscale)", gray)
    cv2.imshow("Histogram (Grayscale)", hist_vis)
    print("\n아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
