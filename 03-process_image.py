import os
import sys
import argparse
import numpy as np
import cv2

import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

def resize(img_path):
    """이미지 사이즈 조정
    사이즈 증가 : cv.INTER_AREA 등
    사이즈 축소 : cv2.INTER_CUBIC, cv2.INTER_LINEAR 등

    dsize : 출력 이미지 크기; ex>  (가로, 세로)
    fx : 가로 크기에 적용할 배수
    fy : 세로 크기에 적용할 배수
    """
    img = cv2.imread(img_path, flags=cv2.IMREAD_UNCHANGED)

    dsize_resized = cv2.resize(src=img, dsize=(256,256), interpolation=cv2.INTER_CUBIC)
    fx_fy_resized = cv2.resize(src=img, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    
    image_dit = {
        "dsize_resized":dsize_resized,
        "fx_fy_resized":fx_fy_resized,
    }
    show_image(image_dit)
    
def warp_affine(img_path):
    """이미지 warping
    
    M : 변환 행렬
    dsize : 출력 이미지 크기; ex>  (가로, 세로)
    """
    
    img = cv2.imread(img_path, flags=cv2.IMREAD_UNCHANGED)

    rows, cols = img.shape[:2]

    m = np.float32([[1,0,10], [0,1,20]])
    warpped = cv2.warpAffine(src=img, M=m, dsize=(rows, cols))

    image_dit = {
        "warpped":warpped,
    }
    show_image(image_dit)

def rotate_and_warp_affine(img_path):
    """이미지 rotation 과 warping
    
    M : 변환 행렬
    dsize : 출력 이미지 크기; ex>  (가로, 세로)
    """
    
    img = cv2.imread(img_path, flags=cv2.IMREAD_UNCHANGED)

    rows, cols = img.shape[:2]

    m = cv2.getRotationMatrix2D(center=(cols/2, rows/2) , angle=90 , scale=0.5)
    rotated_warpped = cv2.warpAffine(src=img, M=m, dsize=(rows, cols))

    image_dit = {
        "rotated_warpped":rotated_warpped,
    }
    show_image(image_dit)

def flip(img_path):
    """이미지 상하/좌우 대칭
    
    flipCode : + > 좌/우 ; 0 > 상/하 ; - > 좌/우 + 상/하
    """
    
    img = cv2.imread(img_path, flags=cv2.IMREAD_UNCHANGED)

    positive_flip_code = cv2.flip(img, flipCode=1)
    zero_flip_code = cv2.flip(img, flipCode=0)
    negative_flip_code = cv2.flip(img, flipCode=-1)

    image_dit = {
        "positive_flip_code":positive_flip_code,
        "zero_flip_code":zero_flip_code,
        "negative_flip_code":negative_flip_code,
    }
    show_image(image_dit)



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

    p = add_command('resize', desc='Resizing an image')
    p.add_argument( 'img_path', help='A path indicating image')

    p = add_command('warp_affine', desc='Warpping an image')
    p.add_argument( 'img_path', help='A path indicating image')

    p = add_command('rotate_and_warp_affine', desc='Rotating and warpping an image')
    p.add_argument( 'img_path', help='A path indicating image')

    p = add_command('flip', desc='Flipping an image')
    p.add_argument( 'img_path', help='A path indicating image')

    args = parser.parse_args(argv[1:] if len(argv) > 1 else ['-h'])
    func = globals()[args.command]
    del args.command
    func(**vars(args))

#----------------------------------------------------------------------------

if __name__ == "__main__":
    execute_cmdline(sys.argv)

#----------------------------------------------------------------------------
