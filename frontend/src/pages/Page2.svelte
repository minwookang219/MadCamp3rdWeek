<script lang="ts">
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    import Canvas from '../components/Canvas.svelte';
    import vangoghImage from '../assets/images_tab2/vangogh.webp';
    import monetImage from '../assets/images_tab2/monet.webp';
    import picassoImage from '../assets/images_tab2/picasso.webp';
    import daliImage from '../assets/images_tab2/dali.webp';
    import logoImage from '../assets/logo_images.png';
    import { resultImageStore } from '../store'; // Import store
    
    let isLoading = false;
    let selectedArtist: string | null = null;
    let resultImage: string | null = null;
    let canvasRef: HTMLCanvasElement;
    
    const artists = [
        { id: 'vangogh', name: '별이 빛나는 밤에 - 빈센트 반 고흐', style: '후기 인상주의', image: vangoghImage },
        { id: 'dali', name: '살바도르 달리', style: '초현실주의', image: daliImage },
        { id: 'picasso', name: '파블로 피카소', style: '입체파', image: picassoImage },
        { id: 'monet', name: '클로드 모네', style: '인상주의', image: monetImage }
    ];

    let progress = 66.66666667; // 세 번째 단계이므로 진행률 66.67%
    let showScrollButton = true;
    
    async function handleTransform() {
    if (!selectedArtist || !canvasRef) {
        alert('화가와 그림을 모두 선택해주세요');
        return;
    }

    isLoading = true;
    try {
            // Canvas의 이미지를 Blob으로 변환
            const contentBlob = await new Promise<Blob | null>(resolve => {
                canvasRef.toBlob(resolve, 'drawing.jpg');
            });

            if (!contentBlob) {
                alert('그림을 캔버스에서 가져올 수 없습니다.');
                return;
            }

            const artist = artists.find(a => a.id === selectedArtist);
            if (!artist) {
                alert('선택한 화가 정보를 찾을 수 없습니다.');
                return;
            }

            const styleResponse = await fetch(artist.image);
            if (!styleResponse.ok) {
                throw new Error('화풍 이미지를 가져오는 데 실패했습니다.');
            }
            const styleBlob = await styleResponse.blob();

            const formData = new FormData();
            formData.append('content', contentBlob, 'drawing.jpg');
            formData.append('style', styleBlob, `${artist.id}.jpg`);

            const response = await fetch('http://127.0.0.1:8001/transform2', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('이미지 처리 중 오류가 발생했습니다');
            }

            const resultBlob = await response.blob();
            resultImage = URL.createObjectURL(resultBlob);
            resultImageStore.set(resultImage);

            const resultContainer = document.querySelector('.result-container');
            if (resultContainer) {
                resultContainer.scrollIntoView({ behavior: 'smooth' });
            }
        } catch (error) {
            console.error('Error:', error);
            const errorMessage = error instanceof Error ? error.message : '알 수 없는 오류가 발생했습니다';
            alert('이미지 처리 중 오류가 발생했습니다: ' + errorMessage);
        } finally {
            isLoading = false;
        }
}

    onMount(() => {
        window.scrollTo(0, 0);
        
        window.addEventListener('scroll', () => {
            const functionSection = document.querySelector('.function-section');
            if (functionSection) {
                const rect = functionSection.getBoundingClientRect();
                showScrollButton = rect.top > window.innerHeight;
            }
        });
    });

    function scrollToBottom() {
        const functionSection = document.querySelector('.function-section');
        if (functionSection) {
            functionSection.scrollIntoView({ behavior: 'smooth' });
        }
    }
</script>

<main>
    {#if isLoading}
        <div class="loading-overlay">
            <div class="loading-content">
                <div class="loading-spinner"></div>
                <p>화풍 변환 중...</p>
            </div>
        </div>
    {/if}

    <div class="scroll-container">

        <div class="scroll-section">
            <section class="function-section">
                
                <div class="content-layout">
                    <div class="left-panel">
                        <div class="select-image">
                            닮고 싶은 화풍을 고르세요
                        </div>
                        <div class="artist-grid">
                            {#each artists as artist}
                                <div 
                                    class="artist-card" 
                                    class:selected={selectedArtist === artist.id}
                                    on:click={() => selectedArtist = artist.id}
                                    on:keypress={() => selectedArtist = artist.id}
                                    role="button"
                                    tabindex="0"
                                >
                                    <img src={artist.image} alt={artist.name} class="artist-image"/>
                                    <div class="artist-info">
                                        <h3>{artist.name}</h3>
                                        <p>{artist.style}</p>
                                    </div>
                                </div>
                            {/each}
                        </div>
                    </div>
                    
                    <div class="right-panel">
                        <div class="canvas-container">
                            <Canvas bind:canvasRef={canvasRef} />
                        </div>
                        <button 
                            class="transform-button" 
                            disabled={!selectedArtist} 
                            on:click={handleTransform}
                        >
                            화풍 변환하기
                        </button>
                    </div>
                </div>

                {#if resultImage}
                    <div class="result-container">
                        <h2>변환 결과</h2>
                        <img src={resultImage} alt="변환된 이미지" />
                        <button class="page-button" on:click={() => navigate('/theme3')}>
                            다음 단계로
                            <span class="arrow">→</span>
                        </button>
                    </div>
                {/if}
            </section>
        </div>
    </div>

    <div class="progress-bar">
        <div class="progress" style={`width: ${progress}%;`}></div>
        <div class="progress-sections">
            <div class="section1">66.6%</div>
            <div class="section">티켓 마무리</div>
        </div>
    </div>

    
  <div class="footer">
    <div class="footer-content">
        <img src={logoImage} alt="전시회 로고" class="footer-logo" />
        <div class="footer-text">
            몰입전시회 팝업스토어 "전시회"
        </div>
    </div>
</div>
</main>

<style>
    :global(body) {
        background: #111111;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
        overflow-y: hidden;
    }

    main {
        padding: 0;
        height: 100vh;
        overflow: hidden;
        background: #000000;
    }

    .section-divider {
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            #CCCCCC 50%, 
            transparent 100%
        );
        margin: 0;
        opacity: 0.5;
    }

    .description-section {
        height: 100vh;
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .select-image {
        font-size: 32px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 12px;
        padding-left: 48px;
        font-weight: 600;
    }

    .artist-grid {
        display: flex;
        flex-direction: column;
        gap: 15px;
        width: 100%;
    }

    .artist-card {
        width: calc(100% - 10px);
        margin: 0 auto;
        padding: 30px;
        display: flex;
        align-items: center;
        gap: 15px;
        background: #ffffff;
        border: 2px solid #333;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .artist-card:hover {
        background: var(--primary-color-dark);
        transform: translateY(-2px);
    }

    .artist-card.selected {
        background: var(--primary-color);
        border-color: black;
    }

    .artist-image {
        width: 80px;
        height: 80px;
        object-fit: cover;
        border-radius: 8px;
    }

    .artist-info {
        flex: 1;
    }

    .artist-card h3 {
        font-size: 20px;
        color: #000000;
        margin: 0 0 10px 0;
    }

    .artist-card p {
        font-size: 16px;
        color: #000000;
        margin: 0;
    }

    .canvas-container {
        width: 80%;
        margin: 0 auto;
        background: white;
        border-radius: 12px;
        overflow: hidden;
    }

    .transform-button {
        width: 80%;
        margin: 0 auto;
        padding: 15px 30px;
        font-size: 20px;
        background: var(--primary-color-dark);
        color: black;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .transform-button:disabled {
        background: #666;
        cursor: not-allowed;
    }

    .transform-button:hover:not(:disabled) {
        background: var(--primary-color);
        transform: translateY(-2px);
    }

    .result-container {
        max-width: 800px;
        margin: 40px auto 80px;
        text-align: center;
        scroll-margin-top: 100px;
    }

    .result-container h2 {
        color: #CCCCCC;
        margin-bottom: 20px;
    }

    .result-container img {
        max-width: 100%;
        border-radius: 12px;
    }

    .artist-images {
        display: flex;
        gap: 20px;
        margin-top: 20px;
        flex-wrap: wrap;
        justify-content: center;
    }

    .artist-title-image {
        width: 400px;
        height: 400px;
        object-fit: cover;
        border-radius: 8px;
        opacity: 0;
        transform: scale(0.8);
        animation: fadeIn 0.5s forwards;
    }

    @keyframes fadeIn {
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    .progress-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 50px;
        background-color: #000000;
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 10px;
    }

    .progress {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        background-color: #ff55ff;
        z-index: 1;
        transition: width 0.3s ease;
    }

    .progress-sections {
        display: flex;
        width: 100%;
        height: 100%;
        position: relative;
        z-index: 2;
    }

    .section {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #FFFFFF;
    }
    .section1 {
        flex: 2;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #000000;
    }

    .section:last-child {
        border-right: none;
    }

    .scroll-guide {
        position: absolute;
        bottom: 40px;
        left: 47%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
        color: #CCCCCC;
        animation: bounce 2s infinite;
    }

    .scroll-text {
        font-size: 18px;
        font-weight: 500;
        opacity: 0.9;
    }

    .scroll-arrow {
        font-size: 24px;
        font-weight: bold;
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-10px);
        }
        60% {
            transform: translateY(-5px);
        }
    }

    .page-button {
        display: block;
        margin: 40px auto;
        padding: 16px 28px;
        background-color: #4077d6;
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.2s ease;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;
    }

    .page-button:hover {
        background-color: #3567c0;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(64, 119, 214, 0.3);
    }

    .next-button .arrow,
    .page-button .arrow {
        font-size: 20px;
        transition: transform 0.2s ease;
    }

    .next-button:hover .arrow,
    .page-button:hover .arrow {
        transform: translateX(4px);
    }

    .scroll-container {
        height: 100vh;
        overflow-y: scroll;
        scroll-snap-type: y mandatory;
        scroll-snap-stop: always;
        scrollbar-width: none;  /* Firefox */
        -ms-overflow-style: none;  /* IE and Edge */
    }

    .scroll-container::-webkit-scrollbar {
        display: none;  /* Chrome, Safari, Opera */
    }

    .scroll-section {
        height: 100vh;
        scroll-snap-align: start;
        position: relative;
        overflow-y: auto;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }

    .scroll-section::-webkit-scrollbar {
        display: none;
    }

    .function-section {
        min-height: 100vh;
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 80px 0;
        box-sizing: border-box;
        overflow-y: visible;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }

    .function-section::-webkit-scrollbar {
        display: none;
    }

    .content-layout {
        display: flex;
        width: 90%;
        max-width: 1600px;
        /* margin: 20px auto; */
    }

    .left-panel {
        display: flex;
        flex-direction: column;
        gap: 18px;
        text-align: center;
        justify-content: center;
    }
    .right-panel {
        display: flex;
        flex-direction: column;
        gap: 18px;
        margin-right: -100px;
        padding-bottom: 40px;
    }

    .left-panel {
        flex: 3;  /* 30% */
        min-width: 300px;
    }

    .right-panel {
        flex: 7;  /* 70% */
    }

    .footer {
        bottom: 20px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        z-index: 100;
    }

    .footer-content {
        display: flex;
        align-items: center;
        gap: 12px;
        background: rgba(255, 255, 255, 0.1);
        padding: 12px 24px;
        border-radius: 12px;
        backdrop-filter: blur(5px);
    }

    .footer-logo {
        height: 40px;
        width: auto;
        object-fit: contain;
    }

    .footer-text {
        color: black;
        font-size: 16px;
        font-weight: 500;
        letter-spacing: 0.5px;
    }

    .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }

    .loading-content {
        text-align: center;
        color: white;
        background: rgba(255, 255, 255, 0.1);
        padding: 40px;
        border-radius: 16px;
        box-shadow: 0 4px 32px rgba(0, 0, 0, 0.2);
    }

    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #ffffff;
        border-top: 5px solid transparent;
        border-radius: 50%;
        margin: 0 auto 20px;
        animation: spin 1s linear infinite;
    }

    .loading-content p {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        margin: 0;
        white-space: nowrap;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

</style>
