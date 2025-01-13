<script lang="ts">
    import { onMount } from 'svelte';
    import Canvas from '../components/Canvas.svelte';

    import vangoghImage from '../assets/images_tab2/vangogh.webp';
    import monetImage from '../assets/images_tab2/monet.webp';
    import picassoImage from '../assets/images_tab2/picasso.webp';
    import daliImage from '../assets/images_tab2/dali.webp';

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

    async function handleTransform() {
        if (!selectedArtist || !canvasRef) return;

        const imageData = canvasRef.toDataURL('image/png');
        
        try {
            const response = await fetch('/api/transform', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    image: imageData,
                    artist: selectedArtist
                })
            });

            if (!response.ok) throw new Error('변환 실패');
            
            const data = await response.json();
            resultImage = data.transformedImage;
        } catch (error) {
            console.error('Error:', error);
            alert('이미지 변환 중 오류가 발생했습니다.');
        }
    }

    onMount(() => {
        window.scrollTo(0, 0);
    });
</script>

<main>
    <div class="section-divider"></div>
    
    <section class="description-section">
        <h1>화가의 화풍으로 변신하기</h1>
        <div class="artist-images">
            {#each artists as artist, i}
                <img src={artist.image} alt={artist.name} class="artist-title-image" style="animation-delay: {i * 1}s;"/>
            {/each}
        </div>
    </section>

    <div class="section-divider"></div>

    <section class="function-section">
        <div class="help-text">
            그림을 그린 후, 원하는 화가의 화풍으로 변환해드립니다
        </div>
        
        <div class="canvas-container">
            <Canvas bind:canvasRef={canvasRef} />
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

        <button 
            class="transform-button" 
            disabled={!selectedArtist} 
            on:click={handleTransform}
        >
            화풍 변환하기
        </button>

        {#if resultImage}
            <div class="result-container">
                <h2>변환 결과</h2>
                <img src={resultImage} alt="변환된 이미지" />
            </div>
        {/if}
    </section>

    <div class="progress-bar">
        <div class="progress" style={`width: ${progress}%;`}></div>
        <div class="progress-sections">
            <div class="section">조각상 만들기</div>
            <div class="section">배경 꾸미기</div>
            <div class="section">티켓 마무리</div>
        </div>
    </div>
</main>

<style>
    :global(body) {
        background: #111111;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    main {
        padding: 0;
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
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative;
        padding: 0;
        margin: 0;
    }

    h1 {
        font-size: 64px;
        color: #CCCCCC;
        text-align: center;
        margin-bottom: 40px;
    }

    .help-text {
        font-size: 32px;
        color: #CCCCCC;
        text-align: center;
        font-weight: 600;
        padding: 20px;
        letter-spacing: 1px;
    }

    .artist-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
        max-width: 1000px;
        margin: 40px auto;
        padding: 0 20px;
    }

    .artist-card {
        display: flex;
        align-items: center;
        gap: 20px;
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border: 2px solid #333;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .artist-card:hover {
        background: rgba(255, 107, 26, 0.1);
        transform: translateY(-2px);
    }

    .artist-card.selected {
        background: rgba(255, 107, 26, 0.2);
        border-color: #FF6B1A;
    }

    .artist-image {
        width: 120px;
        height: 120px;
        object-fit: cover;
        border-radius: 8px;
    }

    .artist-info {
        flex: 1;
    }

    .artist-card h3 {
        font-size: 24px;
        color: #FF6B1A;
        margin: 0 0 10px 0;
    }

    .artist-card p {
        font-size: 18px;
        color: #CCCCCC;
        margin: 0;
    }

    .canvas-container {
        width: 100%;
        max-width: 800px;
        margin: 40px auto;
        background: white;
        border-radius: 12px;
        overflow: hidden;
    }

    .transform-button {
        display: block;
        margin: 40px auto;
        padding: 15px 40px;
        font-size: 20px;
        background: #FF6B1A;
        color: white;
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
        background: #ff8142;
        transform: translateY(-2px);
    }

    .result-container {
        max-width: 800px;
        margin: 40px auto;
        text-align: center;
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
</style>
