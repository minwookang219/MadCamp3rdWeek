<script lang="ts">
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    import Canvas from '../components/Canvas.svelte';

    import vangoghImage from '../assets/images_tab2/vangogh.webp';
    import monetImage from '../assets/images_tab2/monet.webp';
    import picassoImage from '../assets/images_tab2/picasso.webp';
    import daliImage from '../assets/images_tab2/dali.webp';
    import logoImage from '../assets/logo_images.png';

    let selectedArtist: string | null = null;
    let resultImage: string | null = null;
    let canvasRef: HTMLCanvasElement;
    
    const artists = [
        { id: 'vangogh', name: '빈센트 반 고흐', style: '후기 인상주의', image: vangoghImage },
        { id: 'dali', name: '살바도르 달리', style: '초현실주의', image: daliImage },
        { id: 'picasso', name: '파블로 피카소', style: '입체파', image: picassoImage },
        { id: 'monet', name: '클로드 모네', style: '인상주의', image: monetImage }
    ];

    let progress = 66.66666667; // 세 번째 단계이므로 진행률 66.67%
    let showScrollButton = true;
    
    async function handleTransform() {
        if (!selectedArtist || !canvasRef) return;

        resultImage = canvasRef.toDataURL('image/png');
        setTimeout(() => {
            const resultContainer = document.querySelector('.result-container');
            if (resultContainer) {
                resultContainer.scrollIntoView({ behavior: 'smooth' });
            }
        }, 100);
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
    <div class="scroll-container">
        <div class="scroll-section">
            <div class="section-divider"></div>
            <section class="description-section">
                <h1>화가의 화풍으로 변신하기</h1>
                <div class="artist-images">
                    {#each artists as artist, i}
                        <img src={artist.image} alt={artist.name} class="artist-title-image" style="animation-delay: {i * 1}s;"/>
                    {/each}
                </div>
                <div class="scroll-guide">
                    <span class="scroll-text">아래로 스크롤하세요</span>
                    <span class="scroll-arrow">↓</span>
                </div>
            </section>
        </div>

        <div class="scroll-section">
            <section class="function-section">
                <div class="help-text">
                    그림을 그린 후, 원하는 화가의 화풍으로 변환해드립니다
                </div>
                
                <div class="content-layout">
                    <div class="left-panel">
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
            <div class="section">조각상 만들기</div>
            <div class="section">배경 꾸미기</div>
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

    h1 {
        font-size: 64px;
        color: rgb(0, 0, 0);
        text-align: center;
        margin-bottom: 40px;
    }

    .help-text {
        font-size: 32px;
        color: #000000;
        text-align: center;
        font-weight: 600;
        padding: 20px;
        letter-spacing: 1px;
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
        background: var(--primary-color-light);
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
        background-color: #f0f0f0;
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
        background-color: #aff7b2;
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
        color: #000;
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
        margin: 20px auto;
        gap: 40px;
    }

    .left-panel, .right-panel {
        display: flex;
        flex-direction: column;
        gap: 20px;
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

</style>
