
import os
import sys
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.core.defchararray import center

def show_image(image_dict:dict):
    """이미지 배열을 이미지로 확인

    Args:
        image_arr (np.array): 보여줄 이미지 배열
    """
    num_img = len(image_dict.items())
    plt.style.use('seaborn-white')
    plt.figure(figsize=(20,5))
    for idx, (key, img_arr) in enumerate(image_dict.items()):
        plt.subplot(1, num_img, idx+1)
        plt.title(key)
        plt.imshow(img_arr)
    plt.show()

def draw_line(image:np.array):
    """배경 이미지에 선을 그림

    Args:
        image (np.array): 배경 이미지
    """
    cv2.line(
        image,
        pt1=(0,256), # 시작 위치
        pt2=(512,256), # 종료 위치
        color=(255,255,255), # (R,G,B)
        thickness=5 # thickness가 -1이면 색 채우기
        )

def draw_circle(image:np.array):
    """배경 이미지에 원을 그림

    Args:
        image (np.array): 배경 이미지
    """
    cv2.circle(
        image,
        center=(256,256), # 중심 위치
        radius=100, # 반지름
        color=(255,255,255),
        thickness=-1 # thickness가 -1이면 색 채우기
        )

def draw_ellipse(image:np.array):
    """배경 이미지에 타원을 그림

    Args:
        image (np.array): 배경 이미지
    """
    cv2.ellipse(
        image,
        center=(256,256), # 중심 위치
        axes=(100,50), # (중심에서 가장 긴 거리, 중심에서 가장 짧은 거리)
        angle=0, # 기울기 각도
        startAngle=0, # 그리기 시작 각도
        endAngle=90, # 그리기 종료 각도
        color=(255,255,255),
        thickness=-1 # thickness가 -1이면 색 채우기
        )

def draw_polygon(image:np.array):
    """배경 이미지에 다각형을 그림

    Args:
        image (np.array): 배경 이미지
    """
    # 좌표 배열을 3차원 배열로 변경
    points = np.array([[100,100],  [300,100], [100,200], [100,300],[200,100]], np.int32)
    points = points.reshape((-1,2,1))

    cv2.polylines(
        image,
        pts=[points], # 중심 위치
        isClosed=True, # 시작점과 종료점 연결 여부
        color=(255,255,255),
        thickness=5
        )

def draw():
    """이미지 배열에 좌표 기반 도형을 그리는 기본적인 내용을 다루는 스크립트
    """
    # 이미지 크기 및 색공간 채널 설정
    image_shape = (512, 512, 3) # 3은 RGB 색공간을 위한 값
    
    # 검정색 배경 이미지 생성
    empty_image = np.zeros(image_shape, dtype=np.uint8) # 0~255 값을 갖기 때문에 uint8 사용
    
    # 선 그리기
    line_image = empty_image.copy()
    draw_line(line_image)
    
    # 원 그리기
    circle_image = empty_image.copy()
    draw_circle(circle_image)

    # 타원 그리기
    ellipse_image = empty_image.copy()
    draw_ellipse(ellipse_image)

    # 다각형 그리기
    polygon_image = empty_image.copy()
    draw_polygon(polygon_image)

    # 이미지 순차 확인
    image_dit = {
        "line_image":line_image,
        "circle_image":circle_image,
        "ellipse_image":ellipse_image,
        "polygon_image":polygon_image,
    }
    show_image(image_dit)


#----------------------------------------------------------------------------

def execute_cmdline(argv):
    prog = argv[0]
    parser = argparse.ArgumentParser(
        prog        = prog,
        description = 'Tool for manipulating images.',
        epilog      = 'Type "%s <command> -h" for more information.' % prog)

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True
    def add_command(cmd, desc, example=None):
        epilog = 'Example: %s %s' % (prog, example) if example is not None else None
        return subparsers.add_parser(cmd, description=desc, help=desc, epilog=epilog)

    p = add_command('draw', desc="Drawing various type of polygons like 'line', 'circle' and 'rectangle'")

    args = parser.parse_args(argv[1:] if len(argv) > 1 else ['-h'])
    func = globals()[args.command]
    del args.command
    func(**vars(args))

#----------------------------------------------------------------------------

if __name__ == "__main__":
    execute_cmdline(sys.argv)

#----------------------------------------------------------------------------
