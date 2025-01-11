from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from colorsys import rgb_to_hsv, hsv_to_rgb

def enhance_drawing(image):
    # 이미지 향상
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)  # 대비 증가
    
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.3)  # 선명도 증가
    
    return image

def apply_pixel_art_effect(image, pixel_size=8, colors=32):
    # 이미지 크기 조정
    width, height = image.size
    new_width = width // pixel_size
    new_height = height // pixel_size
    
    # 이미지 리사이즈 및 색상 수 감소
    small = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    small = small.convert('P', palette=Image.Palette.ADAPTIVE, colors=colors)
    
    # 다시 원래 크기로 확대
    output = small.resize((width, height), Image.Resampling.NEAREST)
    
    return output

def add_artistic_effects(image):
    # 이미지를 RGB 모드로 변환
    image = image.convert('RGB')
    
    # 약간의 블러 효과 추가
    blurred = image.filter(ImageFilter.GaussianBlur(radius=1))
    
    # 색상 보정
    enhancer = ImageEnhance.Color(blurred)
    image = enhancer.enhance(1.2)  # 채도 증가
    
    # 밝기 조정
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.1)  # 밝기 약간 증가
    
    return image

def add_background_effect(image, style='gradient'):
    width, height = image.size
    background = Image.new('RGB', (width, height), 'white')
    
    if style == 'gradient':
        # 그라데이션 배경 생성
        for y in range(height):
            for x in range(width):
                r = int(255 * (1 - y/height))  # 상단에서 하단으로 그라데이션
                g = int(200 * (1 - y/height))
                b = int(255 * (x/width))  # 좌측에서 우측으로 그라데이션
                background.putpixel((x, y), (r, g, b))
    
    # 원본 이미지와 배경 블렌딩
    return Image.blend(background, image, 0.85)

def convert_to_pixel_art(image):
    # 1. 그림 향상
    enhanced = enhance_drawing(image)
    
    # 2. 픽셀 아트 효과 적용
    pixelated = apply_pixel_art_effect(enhanced)
    
    # 3. 예술적 효과 추가
    artistic = add_artistic_effects(pixelated)
    
    # 4. 배경 효과 추가
    final = add_background_effect(artistic)
    
    return final 