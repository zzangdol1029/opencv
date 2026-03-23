# OpenCV CV Lab

OpenCV를 이용한 **이미지·영상 처리** 실습 코드 모음입니다. (기존: 3주차 실습 자료)

## 요구 사항

- Python 3.9+
- `opencv-python` (아래 설치 참고)

```bash
pip install -r requirements.txt
```

## 포함 스크립트

| 파일 | 설명 |
|------|------|
| `read_lenna.py` | Lenna 그레이스케일 표시 |
| `lenna_components.py` | BGR 채널 분리·통계 |
| `lenna_hsv.py` / `lenna_yuv.py` | 색 공간 변환 및 채널 표시 |
| `lenna_grayscale_histogram.py` | 그레이 히스토그램 |
| `lena_grayscale_histogram.py` | 위 스크립트 실행 별칭 |
| `lenna_bgr_histogram.py` | BGR 히스토그램 |
| `candies_red_extract.py` | BGR R 채널 `inRange` 추출 |
| `candies_red_hsv.py` / `candies_blue_hsv.py` | HSV 색 범위로 캔디 추출 |
| `play_test_video.py` | `test_video.mp4` 재생 |
| `camera_preview.py` | 웹캠 실시간 미리보기 |

## 데이터

`Lenna.png`, `candies.png`, `test_video.mp4` 등은 실습용 샘플 자료입니다.

## 라이선스

교육·실습 목적으로 자유롭게 사용하세요.
