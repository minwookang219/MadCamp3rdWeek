from flask import Flask, render_template, request, jsonify
import torch
from PIL import Image
import io
import base64
import numpy as np
from diffusers import StableDiffusionImg2ImgPipeline

app = Flask(__name__)

# 모델 로드 시 메모리 최적화 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Stable Diffusion 모델 로드 with 메모리 최적화
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,  # float16으로 변경
    variant="fp16",
    revision="fp16",
    use_safetensors=True
).to(device)

# 메모리 최적화 설정
pipe.enable_attention_slicing()
pipe.enable_sequential_cpu_offload()
torch.cuda.empty_cache()  # GPU 캐시 비우기

def colorize_sketch(image):
    # 이미지 크기 조정 (메모리 사용량 감소)
    max_size = 512
    width, height = image.size
    if width > max_size or height > max_size:
        ratio = max_size / max(width, height)
        new_size = (int(width * ratio), int(height * ratio))
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # 이미지 전처리
    image = image.convert('RGB')
    
    # Stable Diffusion 설정 최적화
    prompt = "beautiful digital art, vibrant colors, artistic coloring"
    negative_prompt = "grayscale, black and white, monochrome"
    
    try:
        # 메모리 효율적인 이미지 생성
        with torch.no_grad():  # 메모리 사용량 감소
            colored_image = pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                image=image,
                strength=0.7,
                guidance_scale=7.5,
                num_inference_steps=30,  # 스텝 수 감소
            ).images[0]
        
        return colored_image
    
    except Exception as e:
        print(f"Error in colorize_sketch: {str(e)}")
        return image  # 에러 발생 시 원본 이미지 반환

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        # 받은 이미지 데이터 처리
        image_data = request.json['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)
        
        # PIL Image로 변환
        image = Image.open(io.BytesIO(image_bytes))
        
        # 스케치 채색
        colored_image = colorize_sketch(image)
        
        # 결과 이미지를 base64로 인코딩
        buffered = io.BytesIO()
        colored_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # 메모리 정리
        torch.cuda.empty_cache()
        
        return jsonify({'success': True, 'image': f'data:image/png;base64,{img_str}'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 