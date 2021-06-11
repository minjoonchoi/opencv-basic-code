import os
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

def load_image_by_pillow(path:str):
    """이미지 파일을 PIL로 로드

    Args:
        path (str): 이미지 파일 경로

    Returns:
        Image: 이미지 객체
    """
    return Image.open(path)

def load_image_by_cv2(path:str):
    """이미지 파일을 OpenCV로 로드

    Args:
        path (str): 이미지 파일 경로

    Raises:
        FileExistsError: [description]

    Returns:
        [type]: [description]
    """
    if not os.path.exists(path):
        raise FileExistsError(f'Image file not exists : {path}')
    return cv2.imread(path, flags=cv2.IMREAD_UNCHANGED)

def save_image_by_cv2(path:str, image_arr:np.array):
    """이미지 배열을 해당경로에 이미지파일로 저장

    Args:
        path (str): 이미지가 저장될 경로
        image_arr (np.array): 저장할 이미지 배열
    """
    cv2.imwrite(path, image_arr)

def convert_channel(image_arr, flag:int=cv2.COLOR_RGB2BGR):
    """이미지 배열의 컬러 채널을 flag에 맞게 변경
    Args:
        image_arr (np.array)): 이미지 배열
        flag (int): cv2 이미지 flag

    Returns:
        np.array: 순서 변경된 배열

    Args:
        image_arr ([type]): [description]

    Returns:
        [type]: [description]
    """
    return cv2.cvtColor(image_arr, flag)

def convert_pil_image_to_np_array(image:Image):
    """Image 객체를 Numpy 배열로 변경

    Args:
        image (Image): Image 객체

    Returns:
        np.array: 이미지 배열
    """
    image_arr = np.asarray(image)
    return image_arr

def check_arr(image_arr:np.array):
    """이미지 배열 color 채널 출력

    Args:
        image_arr (np.array): 이미지 배열
    """
    print('-'*50)
    print('이미지 배열 형태 : ', image_arr.shape, sep='\n')
    for channel_idx in range(image_arr.shape[-1]):
        print('-'*50)
        print(f'{channel_idx} 채널 : ', image_arr[:,:,channel_idx], sep='\n')
    print('-'*50)

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


def main():
    """이미지 배열에 관련된 기본적인 내용을 다루는 스크립트
    라이브러리 별로 이미지 배열의 색공간 순서가 다르기 때문에 인지하고 사용해야한다.
    OpenCV : BGR
    Matplotlib : RGB
    Image : RGB
    """
    image_path = './iu.jpg'

    # PIL로 이미지 로드
    image = load_image_by_pillow(image_path)

    # 이미지 배열로 전환
    pil_image_arr = convert_pil_image_to_np_array(image)
    
    # 이미지 배열 색공간 순서 BGR로 변경
    pil_bgr_image_arr = convert_channel(pil_image_arr, flag=cv2.COLOR_RGB2BGR)
    
    # OpenCV로 이미지 로드 
    cv2_image_arr = load_image_by_cv2(image_path)
    
    # 이미지 배열 색공간 순서 RGB로 변경
    cv2_rgb_image_arr = convert_channel(cv2_image_arr, flag=cv2.COLOR_BGR2RGB)

    # 이미지 배열을 파일로 저장
    save_image_by_cv2('./new_iu.jpg', cv2_rgb_image_arr)

    # 이미지 순차 확인
    image_dit = {
        "pil_image_arr":pil_image_arr,
        "pil_bgr_image_arr":pil_bgr_image_arr,
        "cv2_image_arr":cv2_image_arr,
        "cv2_rgb_image_arr":cv2_rgb_image_arr
    }
    show_image(image_dit)

if __name__ == '__main__':
    """파이썬 커맨드로 스크립트를 실행시킬 때만 실행되는 if 블럭
    example : python 01-handle_image.py
    """
    main()