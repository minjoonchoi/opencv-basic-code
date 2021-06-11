# opencv
OpenCV 학습 저장소

## 코드 실행 환경

- Ubuntu 18.04
- Anaconda 4.10.1

## 아나콘다 설치

- [설치 가이드](https://docs.anaconda.com/anaconda/install/linux/)
- [Archive 파일 url](https://repo.anaconda.com/archive/)
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

```bash
    # OpenCV
    pip install opencv-python
    # Pillow
    pip install pillow
    # Matplotlib
    pip install matplotlib
    # Numpy
    pip install numpy
```

## 스크립트에서 확인할 수 있는 함수들

1. 01-handle_image.py
    - load_image_by_pillow(path:str) : 이미지 파일을 PIL로 로드
    - load_image_by_cv2(path:str) : 이미지 파일을 OpenCV로 로드
    - save_image_by_cv2(path:str, image_arr:np.array) : 이미지 배열을 해당경로에 이미지파일로 저장
    - convert_channel(image_arr, flag:int=cv2.COLOR_RGB2BGR) : 이미지 배열의 컬러 채널을 flag에 맞게 변경
    - convert_pil_image_to_np_array(image:Image) : Image 객체를 Numpy 배열로 변경
    - check_arr(image_arr:np.array) : 이미지 배열 color 채널 출력
    - show_image(image_dict:dict) : 이미지 배열을 이미지로 확인

2. 02-handle_polygon.py
    - show_image(image_dict:dict) : 이미지 배열을 이미지로 확인
    - draw_line(image:np.array) : 배경 이미지에 선을 그림
    - draw_circle(image:np.array) : 배경 이미지에 원을 그림
    - draw_ellipse(image:np.array) : 배경 이미지에 타원을 그림
    - draw_polygon(image:np.array) : 배경 이미지에 다각형을 그림
