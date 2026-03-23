"""
OpenCV로 Lenna.png를 읽어 YUV로 변환하고 Y·U·V 성분을 출력·표시합니다.

Y: 휘도(밝기), U/V: 색차(크로마). 영상 압축·전송에서 흔히 쓰는 표현입니다.
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

    # BT.601 등에 맞는 8비트 YUV 변환 (OpenCV 기본 구현)
    yuv = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(yuv)

    height, width = bgr.shape[:2]
    print("--- Lenna.png → YUV 성분 (OpenCV, COLOR_BGR2YUV) ---")
    print(f"크기: {width} x {height}, dtype: {yuv.dtype}")
    print("  Y: 휘도(밝기), U·V: 색차(크로마). 8비트 픽셀은 보통 0~255.")
    for name, ch in (
        ("Y (Luma, 휘도)", y),
        ("U (Chroma U)", u),
        ("V (Chroma V)", v),
    ):
        print(
            f"  {name}: min={int(ch.min())}, max={int(ch.max())}, "
            f"mean={ch.mean():.2f}"
        )

    cv2.imshow("Original (BGR)", bgr)
    cv2.imshow("Y channel", y)
    cv2.imshow("U channel", u)
    cv2.imshow("V channel", v)
    print("\n창이 열립니다. 아무 키나 누르면 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
