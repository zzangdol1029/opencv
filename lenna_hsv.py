"""
OpenCV로 Lenna.png를 읽어 HSV로 변환하고 H·S·V 성분을 출력·표시합니다.

HSV: 색상(Hue), 채도(Saturation), 명도(Value) — 색 범위를 잡을 때 자주 사용합니다.
"""

import os

import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "Lenna.png")


def main() -> None:
    bgr = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
    if bgr is None:
        print(f"이미지를 불러올 수 없습니다: {IMAGE_PATH}")
        return

    if len(bgr.shape) != 3 or bgr.shape[2] != 3:
        print("BGR 3채널 컬러 이미지가 아닙니다.")
        return

    # BGR → HSV (inRange 등으로 특정 색만 뽑을 때 전 단계로 많이 씀)
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    height, width = bgr.shape[:2]
    print("--- Lenna.png → HSV 성분 (OpenCV) ---")
    print(f"크기: {width} x {height}, dtype: {hsv.dtype}")
    print("  H: 0~179 (색상 각도는 2배하면 도(°)에 대응, 예: H=90 → 약 180°)")
    print("  S, V: 0~255")
    for name, ch in (
        ("H (Hue, 색상)", h),
        ("S (Saturation, 채도)", s),
        ("V (Value, 명도)", v),
    ):
        print(
            f"  {name}: min={int(ch.min())}, max={int(ch.max())}, "
            f"mean={ch.mean():.2f}"
        )

    cv2.imshow("Original (BGR)", bgr)
    cv2.imshow("H channel", h)
    cv2.imshow("S channel", s)
    cv2.imshow("V channel", v)
    print("\n창이 열립니다. 아무 키나 누르면 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
