# opencv
OpenCV 학습 저장소

## 코드 실행 환경

- Ubuntu 18.04
- Anaconda 4.10.1

## 아나콘다 설치

[설치 가이드](https://docs.anaconda.com/anaconda/install/linux/)
[파일 경로](https://repo.anaconda.com/archive/)
```bash
    wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh -O ~/Anaconda3-5.3.1-Linux-x86_64.sh
    bash ~/Anaconda3-5.3.1-Linux-x86_64.sh
```

## 아나콘다 환경 생성

```bash
    conda create -n opencv python=3.7
    conda activate opencv
```

## 파이썬 라이브러리 설치

### 이미지
```bash
    # OpenCV
    pip install opencv-python
    # Pillow
    pip install pillow
    # Matplotlib
    pip install matplotlib
```