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

## 예제 스크립트

1. 01-handle_image.py
```
    usage: 01-handle_image.py [-h] {pillow_img,cv2_img} ...

    Tool for manipulating images.

    positional arguments:
    {pillow_img,cv2_img}
        pillow_img          Handling an image by using pillow
        cv2_img             Handling an image by using opencv

    optional arguments:
    -h, --help            show this help message and exit
```

2. 02-handle_polygon.py
```
    usage: 02-handle_polygon.py [-h] {draw} ...

    Tool for manipulating images.

    positional arguments:
    {draw}
        draw      Drawing various type of polygons like 'line', 'circle' and 'rectangle'

    optional arguments:
    -h, --help  show this help message and exit
```

3. 03-process_image.py
```
    usage: 03-process_image.py [-h] {resize,warp_affine,rotate_and_warp_affine,flip} ...

    Tool for manipulating images.

    positional arguments:
    {resize,warp_affine,rotate_and_warp_affine,flip}
        resize              Resizing an image
        warp_affine         Warpping an image
        rotate_and_warp_affine
                            Rotating and warpping an image
        flip                Flipping an image

    optional arguments:
    -h, --help            show this help message and exit
```