import torch
from diffusers import StableDiffusionXLPipeline
from diffusers.utils import make_image_grid
from PIL import Image
import os

# 출력 디렉토리 생성
output_dir = "generated_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 모델 및 파이프라인 설정
MODEL_NAME = "stabilityai/stable-diffusion-xl-base-1.0"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# SDXL 파이프라인 로드
pipeline = StableDiffusionXLPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True,
).to(device)

# LoRA 가중치 로드
pipeline.load_lora_weights("./sd_lora")

def process_image(pipeline, input_path, output_path):
    # 입력 이미지 로드
    input_image = Image.open(input_path)
    
    # 이미지 크기 조정
    width, height = input_image.size
    target_size = 1024
    if width > height:
        new_width = target_size
        new_height = int(height * target_size / width)
    else:
        new_height = target_size
        new_width = int(width * target_size / height)
    input_image = input_image.resize((new_width, new_height))
    
    # 얼굴에만 집중하는 단순한 프롬프트
    prompt = ("face only, exact same facial features as input, "
             "pure white plaster cast of face, "
             "clean white background, "
             "centered face, front view, "
             "perfect white plaster material")

    negative_prompt = ("body part, neck, hair, shoulders, clothes, "
                      "color, texture, pattern, "
                      "background detail, decoration, "
                      "anything below neck, anything above forehead")
    
    # 이미지 생성
    output_image = pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        image=input_image,
        strength=0.55,       # 원본 얼굴 특징을 더욱 보존
        guidance_scale=6.5,  # 프롬프트 영향력 더 감소
        num_inference_steps=60,
    ).images[0]
    
    # 결과 저장
    output_image.save(output_path, quality=100)
    print(f"Generated and saved: {output_path}")

# 입력 파일들과 출력 파일명 설정
input_files = ['g1']

# 각 입력 파일에 대해 처리
for idx, file_prefix in enumerate(input_files, 1):
    # 입력 파일 경로 (여러 확장자 시도)
    for ext in ['.jpg', '.jpeg', '.png']:
        input_path = f"{file_prefix}{ext}"
        if os.path.exists(input_path):
            output_path = os.path.join(output_dir, f"{file_prefix}_plaster_bust{ext}")
            try:
                process_image(pipeline, input_path, output_path)
            except Exception as e:
                print(f"Error processing {input_path}: {str(e)}")
            break
    else:
        print(f"No valid image file found for {file_prefix}")

# 그리드 이미지도 저장
inference_prompt = "human statue"
images = pipeline(
    inference_prompt,
    num_images_per_prompt=3,
    num_inference_steps=50,
).images

# 개별 이미지 저장
for idx, image in enumerate(images):
    output_path = os.path.join(output_dir, f"grid_image_{idx+1}.png")
    image.save(output_path, quality=100)
    print(f"Saved grid image: {output_path}")

# 그리드 이미지 생성 및 저장
grid_image = make_image_grid(images, rows=1, cols=3)
grid_path = os.path.join(output_dir, "grid_combined.png")
grid_image.save(grid_path, quality=100)
print(f"Saved combined grid image: {grid_path}")

print(f"\nAll images have been saved to the '{output_dir}' directory")
