from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import torch
from diffusers import StableDiffusionPipeline
from io import BytesIO
import base64
import time

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

logger.info("Starting the application...")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # 프론트엔드 서버
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Loading Stable Diffusion model...")
# 모델 로드
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
if torch.cuda.is_available():
    pipe = pipe.to("cuda")
    logger.info("CUDA is available. Model loaded to GPU")
else:
    logger.info("CUDA is not available. Model loaded to CPU")
logger.info("Model loaded successfully!")

class SculptureRequest(BaseModel):
    prompt: str

@app.post("/generate-sculpture")
async def generate_sculpture(request: SculptureRequest):
    try:
        start_time = time.time()
        logger.info(f"Received prompt: {request.prompt}")
        
        # 프롬프트 생성
        prompt = f"A detailed marble sculpture of {request.prompt}, classical style, museum quality, highly detailed, dramatic lighting, 3D rendering, white marble texture"
        logger.info(f"Generated full prompt: {prompt}")
        
        logger.info("Starting image generation...")
        # 이미지 생성
        image = pipe(prompt).images[0]
        logger.info("Image generation completed")
        
        logger.info("Converting image to base64...")
        # 이미지를 base64로 변환
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        end_time = time.time()
        logger.info(f"Total processing time: {end_time - start_time:.2f} seconds")
        
        return {"image": img_str}
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e)) 