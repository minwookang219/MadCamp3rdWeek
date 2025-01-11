<script lang="ts">
    let selectedArtist: string | null = null;
    let resultImage: string | null = null;
    let resultSection: HTMLElement;
    
    const artists = [
        { id: 'vangogh', name: '빈센트 반 고흐', style: '후기 인상주의' },
        { id: 'monet', name: '클로드 모네', style: '인상주의' },
        { id: 'picasso', name: '파블로 피카소', style: '입체파' },
        { id: 'dali', name: '살바도르 달리', style: '초현실주의' }
    ];
</script>

<main>
    <h2 class="main-title">화가의 화풍으로 변신하기</h2>
    
    <div class="artist-section">
        <h3>1단계: 화가 선택</h3>
        <div class="artist-grid">
            {#each artists as artist}
                <div 
                    class="artist-card" 
                    class:selected={selectedArtist === artist.id}
                    on:click={() => selectedArtist = artist.id}
                >
                    <h3>{artist.name}</h3>
                    <p>{artist.style}</p>
                </div>
            {/each}
        </div>
    </div>
</main>

<style>
    main {
        padding: 70px 20px;
        min-height: 100vh;
        background: #111111;
        color: #CCCCCC;
    }

    .main-title {
        font-size: 36px;
        text-align: center;
        margin-bottom: 40px;
        color: #FF6B1A;
    }

    h3 {
        font-size: 24px;
        color: #FF6B1A;
        margin-bottom: 20px;
        text-align: left;
    }

    .artist-section {
        max-width: 800px;
        margin: 0 auto 60px;
        padding: 20px;
    }

    .artist-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        margin-bottom: 20px;
    }

    .artist-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border: 2px solid #333;
        border-radius: 12px;
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
</style>
