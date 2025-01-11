<!-- // src/routes/About.svelte -->
<script lang="ts">
    // 이미지 import
    import sculpture1 from '../assets/images_tab1/statue_1.webp';
    import sculpture2 from '../assets/images_tab1/statue_2.webp';
    import sculpture3 from '../assets/images_tab1/statue_3.webp';
    import sculpture4 from '../assets/images_tab1/statue_4.webp';
    import sculpture5 from '../assets/images_tab1/statue_5.webp';

    // 슬라이더 애니메이션을 위한 변수
    let isHovered = false;

    // 파일 업로드와 결과 이미지를 위한 상태
    let uploadedImage: string | null = null;
    let resultImage: string | null = null;
    let isProcessing = false;
    let progressMessage = '';

    // API URL 설정
    const API_URL = 'http://localhost:8000/convert-image';  // 백엔드 URL

    // 파일 업로드 처리
    async function handleFileUpload(event: Event) {
        const target = event.target as HTMLInputElement;
        const file = target.files?.[0];
        if (file) {
            try {
                isProcessing = true;
                progressMessage = '이미지 업로드 중...';
                
                // 업로드된 이미지 미리보기
                const reader = new FileReader();
                reader.onload = (e) => {
                    uploadedImage = e.target.result;
                };
                reader.readAsDataURL(file);

                // FormData 생성
                const formData = new FormData();
                formData.append('file', file);

                progressMessage = '조각상으로 변환 중...';
                
                // API 호출
                const response = await fetch(API_URL, {
                    method: 'POST',
                    body: formData,
                });

                if (!response.ok) {
                    throw new Error('이미지 변환에 실패했습니다');
                }

                // 응답 처리
                const result = await response.blob();
                resultImage = URL.createObjectURL(result);
                progressMessage = '변환 완료!';
            } catch (error) {
                console.error('Error:', error);
                progressMessage = '오류가 발생했습니다: ' + error.message;
            } finally {
                isProcessing = false;
            }
        }
    }

    // 컴포넌트가 제거될 때 URL 정리
    import { onDestroy } from 'svelte';
    onDestroy(() => {
        if (resultImage) {
            URL.revokeObjectURL(resultImage);
        }
    });
</script>

<main>
    <div class="section-divider"></div>
    
    <section class="description-section">
        <!-- 상단 슬라이더 -->
        <div class="slider-container top" 
            role="region"
            aria-label="상단 이미지 슬라이더"
            on:mouseenter={() => isHovered = true}
            on:mouseleave={() => isHovered = false}>
            <div class="slider" class:paused={isHovered}>
                <!-- 첫 번째 세트 -->
                <img src={sculpture1} alt="sculpture 1">
                <img src={sculpture2} alt="sculpture 2">
                <img src={sculpture3} alt="sculpture 3">
                <img src={sculpture4} alt="sculpture 4">
                <img src={sculpture5} alt="sculpture 5">
                <!-- 순환을 위한 복제 세트 -->
                <img src={sculpture1} alt="sculpture 1">
                <img src={sculpture2} alt="sculpture 2">
                <img src={sculpture3} alt="sculpture 3">
                <img src={sculpture4} alt="sculpture 4">
                <img src={sculpture5} alt="sculpture 5">
            </div>
        </div>
        
        <h1>조각미남</h1>

        <!-- 하단 슬라이더 -->
        <div class="slider-container bottom" 
            role="region"
            aria-label="하단 이미지 슬라이더"
            on:mouseenter={() => isHovered = true}
            on:mouseleave={() => isHovered = false}>
            <div class="slider" class:paused={isHovered}>
                <!-- 첫 번째 세트 -->
                <img src={sculpture1} alt="sculpture 1">
                <img src={sculpture2} alt="sculpture 2">
                <img src={sculpture3} alt="sculpture 3">
                <img src={sculpture4} alt="sculpture 4">
                <img src={sculpture5} alt="sculpture 5">
                <!-- 순환을 위한 복제 세트 -->
                <img src={sculpture1} alt="sculpture 1">
                <img src={sculpture2} alt="sculpture 2">
                <img src={sculpture3} alt="sculpture 3">
                <img src={sculpture4} alt="sculpture 4">
                <img src={sculpture5} alt="sculpture 5">
            </div>
        </div>
    </section>

    <div class="section-divider"></div>

    <section class="function-section">
        <div class="help-text">
            사진을 첨부하시면, 조각상으로 바꿔드립니다
        </div>
        <div class="image-processing-container">
            <div class="upload-section">
                <h3>사진 업로드</h3>
                <div class="upload-area" class:has-image={uploadedImage}>
                    {#if uploadedImage}
                        <img src={uploadedImage} alt="uploaded" />
                    {:else}
                        <label for="file-upload" class="upload-label">
                            <span class="upload-icon">+</span>
                            <span>클릭하여 사진 업로드</span>
                        </label>
                        <input 
                            type="file" 
                            id="file-upload" 
                            accept="image/*" 
                            on:change={handleFileUpload}
                            style="display: none;"
                        />
                    {/if}
                </div>
            </div>

            <div class="arrow">→</div>

            <div class="result-section">
                <h3>변환된 조각상</h3>
                <div class="result-area">
                    {#if isProcessing}
                        <div class="loading">
                            <div class="spinner"></div>
                            <p>{progressMessage}</p>
                        </div>
                    {:else if resultImage}
                        <img src={resultImage} alt="result" />
                    {:else}
                        <div class="placeholder">
                            여기에 변환된 이미지가 표시됩니다
                        </div>
                    {/if}
                </div>
            </div>
        </div>
    </section>
</main>



<style>
    :global(body) {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    main {
        padding: 0;
    }

    .description-section {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative;
        padding: 0;
        margin: 0;
        overflow: hidden;
    }

    .description-section h1 {
        font-size: 150px;
        font-weight: bold;
        margin-bottom: 80px;
        margin-top: 80px;
        color: #000000;
        padding: 30px 60px;
        white-space: nowrap;
        position: relative;
        z-index: 10;
        text-shadow: 
            3px 3px 0 #FF8C42,
            6px 6px 0 rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
        letter-spacing: 5px;
    }

    .description-section h1:hover {
        transform: scale(1.02) translateY(-5px);
    }


    .section-divider {
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            #000 50%, 
            transparent 100%
        );
        margin: 0;
        opacity: 0.5;
    }

    .slider-container {
        width: 100%;
        overflow: hidden;
        padding: 20px 0;
    }

    .slider-container.top {
        position: absolute;
        top: 30px;
        z-index: 1;
    }

    .slider-container.bottom {
        position: absolute;
        bottom: 30px;
        z-index: 1;
    }

    .slider-container.top .slider {
        animation: scroll 20s linear infinite reverse;
    }

    .slider-container.bottom .slider {
        animation: scroll 20s linear infinite;
    }

    .slider {
        display: flex;
        gap: 20px;
        animation: scroll 20s linear infinite reverse;
    }

    .slider.paused {
        animation-play-state: paused;
    }

    @keyframes scroll {
        0% {
            transform: translateX(calc(-300px * 5 - 20px * 5));
        }
        100% {
            transform: translateX(0);
        }
    }

    .slider img {
        width: 300px;
        height: 400px;
        object-fit: cover;
        border-radius: 10px;
        flex-shrink: 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .slider img:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }

    .slider-container::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(90deg, 
            rgba(255,255,255,0.8) 0%, 
            rgba(255,255,255,0) 10%, 
            rgba(255,255,255,0) 90%, 
            rgba(255,255,255,0.8) 100%);
        pointer-events: none;
    }

    .function-section {
        height: 100vh;
        padding: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 40px;
    }

    .help-text {
        font-size: 32px;
        color: #333;
        text-align: center;
        font-weight: 600;
        padding: 20px;
        letter-spacing: 1px;
    }

    .image-processing-container {
        display: flex;
        justify-content: space-around;
        align-items: flex-start;
        width: 100%;
        padding: 0px;
        gap: 0px;
    }

    .upload-section, .result-section {
        flex: 1;
        max-width: 600px;
    }

    h3 {
        font-size: 24px;
        margin-bottom: 20px;
        color: #333;
    }

    .upload-area, .result-area {
        width: 100%;
        height: 600px;
        border: 3px dashed #ccc;
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(255, 255, 255, 0.5);
        overflow: hidden;
    }

    .upload-area.has-image {
        border-style: solid;
    }

    .upload-label {
        display: flex;
        flex-direction: column;
        align-items: center;
        cursor: pointer;
        padding: 20px;
    }

    .upload-icon {
        font-size: 72px;
        margin-bottom: 20px;
        color: #666;
    }

    .upload-label span:not(.upload-icon) {
        font-size: 24px;
        font-weight: 500;
    }

    .upload-area img, .result-area img {
        min-width: 300px;
        min-height: 400px;
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }

    .placeholder, .loading {
        color: #666;
        font-size: 24px;
        text-align: center;
    }

    .loading {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }

    .spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #f3f3f3;
        border-top: 5px solid #FF8C42;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .loading p {
        color: #666;
        font-size: 24px;
        text-align: center;
        margin: 0;
    }

    .result-area {
        position: relative;
    }

    .result-area img {
        transition: opacity 0.3s ease;
    }

    .result-area.processing img {
        opacity: 0.5;
    }

    .arrow {
        font-size: 70px;
        color: #666;
        font-weight: bold;
        align-self: center;
        margin-top: 40px;
        transform: scale(1.5);
    }
</style>

