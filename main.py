from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:5173",  # Vite 개발 서버 주소
    "http://172.10.7.17:5173",
    # 필요에 따라 추가 도메인
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 허용할 출처
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 서빙
app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

# 루트 경로에서 Svelte 앱 반환
@app.get("/", response_class=FileResponse)
async def main():
    return "public/index.html"

# 예시 API 엔드포인트
@app.get("/api/hello")
async def read_root():
    return {"message": "Hello from FastAPI"}
