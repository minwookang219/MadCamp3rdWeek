<script lang="ts">
    import { onMount } from 'svelte';
    import html2canvas from 'html2canvas';
    import { navigate } from 'svelte-routing';
    import logoImage from '../assets/logo_images.png';
    import { resultImageStore, characterImageStore } from '../store';
    import { get } from 'svelte/store';
    let userName = '';
    let theme1Image = '';
    let theme2Image = '';
    let visitDate = '';
    let isLoading = true;
    let showTicket = false;
    let isCompleted = false;
    let ticketRef: HTMLDivElement;
    let ticketNumber = 2025;
    
    let BackgroundImage: string | null = null;
    let CharacterImage: string | null = null;
    
    onMount(() => {
        BackgroundImage = get(resultImageStore);
        CharacterImage = get(characterImageStore);
        window.scrollTo(0, 0);
        
        // 4초 후에 완료 메시지 표시
        setTimeout(() => {
            isCompleted = true;
            // 1초 후에 로딩 화면을 올리고 티켓 표시
            setTimeout(() => {
                isLoading = false;
                setTimeout(() => {
                    showTicket = true;
                }, 50);
            }, 100);
        }, 400);
    });
    async function saveTicket() {
        if (!ticketRef) return;
        
        try {
            const canvas = await html2canvas(ticketRef, {
                scale: 2,
                logging: false,
                useCORS: true,
                allowTaint: true
            });
            
            const link = document.createElement('a');
            link.download = `immersive-ticket-${ticketNumber}.png`;
            link.href = canvas.toDataURL('image/png');
            link.click();
        } catch (error) {
            console.error('티켓 저장 중 오류가 발생했습니다:', error);
        }
    }

    let issueDate = new Date().toLocaleDateString('ko-KR', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
    }).replace(/\. /g, '.').replace('.', '.');

    function goToHome() {
        navigate('/');
    }
</script>

<main>
    <!-- 로딩 화면 -->
    <div class="loading-overlay" class:slide-up={!isLoading}>
        <div class="loading-content">
            <div class="loading-spinner" class:hide={isCompleted}></div>
            <p class="loading-text" class:fade-out={isCompleted}>티켓 만드는 중...</p>
            <p class="complete-text" class:fade-in={isCompleted}>제작 완료!</p>
        </div>
    </div>
    
    <div class="ticket-container">
        {#if showTicket}
        <div class="complete-title">티켓이 발급되었어요!</div>
        <div class="ticket-wrapper">
            <div class="ticket" bind:this={ticketRef}>
                <div class="ticket-background" style="background-image: url({BackgroundImage})">
                    <div class="character-image">
                        <img src={CharacterImage} alt="Character" />
                    </div>
                    
                    <div class="ticket-info">
                        <div class="ticket-header">
                            <h1>MAD EXHIBITION</h1>
                            <span class="ticket-number">No. {ticketNumber}</span>
                        </div>

                        <div class="info-grid">
                            <div class="info-item">
                                <span class="label">방문자</span>
                                <span class="value">{userName || '이승재'}</span>
                            </div>
                            
                            <div class="info-item">
                                <span class="label">방문일</span>
                                <span class="value">{visitDate || '2025.02.19'}</span>
                            </div>
                            
                            <div class="info-item">
                                <span class="label">발매일</span>
                                <span class="value">{issueDate}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="discount-info">
                <span class="discount-icon">💡</span>
                위 티켓을 매표소 직원에게 보여주시면 90% 할인을 해드립니다
            </div>
            <div class="button-container">
                <button class="save-button" on:click={saveTicket}>
                    저장하기
                    <span class="save-icon">💾</span>
                </button>
                <button class="home-button" on:click={goToHome}>
                    홈으로 돌아가기
                    <span class="home-icon">🏠</span>
                </button>
            </div>
        </div>
        {/if}
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
    .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #111111;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        transition: transform 0.5s ease;
    }
    
    .loading-overlay.slide-up {
        transform: translateY(-100%);
    }
    
    .loading-content {
        text-align: center;
        color: white;
        position: relative;
        padding: 20px;
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
    
    .loading-text, .complete-text {
        position: relative;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        transition: all 0.3s ease;
        margin-top: 20px;
        width: 100%;
    }
    
    .loading-text {
        opacity: 1;
    }
    
    .loading-text.fade-out {
        opacity: 0;
        transform: translate(-50%, -20px);
    }
    
    .complete-text {
        opacity: 0;
        transform: translate(-50%, 20px);
    }
    
    .complete-text.fade-in {
        opacity: 1;
        transform: translateX(-50%);
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .complete-title{
        display: flex;
        position: absolute;
        z-index: 99;
        top: 6%;
        font-size: 60px;
        font-weight: 600;
        letter-spacing: 2px;
        justify-content: center;
        align-items: center;
    }

    /* 형광펜 밑줄 효과 */
    .complete-title::after {
        content: '';
        position: absolute;
        bottom: 10px; /* 텍스트에서 밑줄의 거리 */
        left: 0;
        width: 100%; /* 밑줄이 텍스트 너비를 덮도록 설정 */
        height: 20px; /* 형광펜 두께 */
        background-color: rgb(127, 187, 255); /* 형광펜 색상 (노란색) */
        z-index: -1; /* 텍스트 아래로 이동 */
        opacity: 0.7; /* 형광펜 투명도 */
        transform: skewX(-20deg); /* 약간의 기울임 효과 */
    }
    
    .ticket-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        padding: 20px;
        opacity: 0;
        transform: translateY(20px);
        transition: all 0.5s ease;
    }
    
    :global(.ticket-container:has(.ticket)) {
        opacity: 1;
        transform: translateY(0);
    }

    .ticket {
        background: #ffffff;
        width: 100%;
        min-width: 800px;
        aspect-ratio: 2.5;
        border-radius: 15px;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.4);
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 10px;
    }

    .ticket-background {
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        position: relative;
        display: flex;
        align-items: center; /* 수직 중앙 정렬 */
        justify-content: flex-start; /* 수평 왼쪽 정렬 */
        background-repeat: no-repeat;
        background-color: #111111;
        margin: 10px;
        border-radius: 4px;
    }

    .character-image {
    width: 160px; /* 고정 너비 */
    height: 160px; /* 고정 높이 */
    /* 또는 반응형을 원하시면 다음과 같이 설정할 수 있습니다:
    width: 35%;
    aspect-ratio: 1 / 1; /* 너비와 높이가 동일하게 유지 */
    overflow: hidden;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%; /* 원형을 만들기 위해 50% 설정 */
    background-color: aquamarine;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto; /* 중앙 정렬 */
    margin-right: 4px;
}

.character-image img {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%; /* 이미지도 원형으로 */
}

    .ticket-info {
        width: 65%;
        padding: 20px;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(5px);
        margin-left: auto;
        color: white;
        border-radius: 4px;

    }

    .ticket-header {
        margin-bottom: 30px;
        border-bottom: 2px solid rgba(255, 255, 255, 0.6);
        padding-bottom: 15px;
    }

    .ticket-header h1 {
        font-size: 24px;
        color: white;
        margin: 0;
        margin-bottom: 10px;
    }

    .ticket-number {
        font-size: 14px;
        color: rgba(255, 255, 255, 0.9);
    }

    .info-grid {
        display: grid;
        gap: 20px;
    }

    .info-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 10px;
        border-bottom: 1px dashed rgba(255, 255, 255, 0.4);
    }

    .info-item .label {
        color: rgba(255, 255, 255, 0.8);
        font-size: 14px;
    }

    .info-item .value {
        color: white;
        font-weight: bold;
        font-size: 16px;

    }


    .ticket::before,
.ticket::after {
    content: '';
    position: absolute;
    top: 0;
    width: 20px;
    height: 100%;
    background-size: 20px 40px;  /* 반원 하나의 크기 (가로x세로) */
    background-repeat: repeat-y;  /* 세로 방향으로 반복 */
    transform: none;
}

.ticket::before {  /* 왼쪽 반원 */
    left: -10px;
    background-image: radial-gradient(
        circle at 0 20px,  /* 원의 중심점 위치 (x y) */
        transparent 0,     /* 중심에서 0px까지는 투명 */
        transparent 10px,  /* 10px까지도 투명 */
        white 10px,       /* 10px부터는 흰색 시작 */
        white 20px        /* 20px까지 흰색 유지 */
    );
}

.ticket::after {   /* 오른쪽 반원 */
    right: -10px;
    background-image: radial-gradient(
        circle at 20px 20px,  /* 원의 중심점을 오른쪽에 위치 */
        transparent 0,
        transparent 10px,
        white 10px,
        white 20px
    );
}

    .ticket-background::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
    }

    :global(body) {
        background: #111111;
        margin: 0;
        padding: 0;
    }

    .button-container {
        position: fixed;
        bottom: 120px;
        right: 100px;
        z-index: 10;
        display: flex;
        gap: 16px;
    }
    
    .save-button {
        padding: 12px 24px;
        background: var(--primary-color);
        backdrop-filter: blur(5px);
        border: none;
        border-radius: 8px;
        color: white;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    .save-button:hover {
        background: var(--primary-color-dark);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(85, 146, 252, 0.3);
    }
    
    .save-icon {
        font-size: 20px;
    }

    .home-button {
        padding: 12px 24px;
        background: var(--primary-color-light);
        backdrop-filter: blur(5px);
        border: none;
        border-radius: 8px;
        color: black;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }

    .home-button:hover {
        background: var(--primary-color);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(85, 146, 252, 0.3);
    }

    .home-icon {
        font-size: 20px;
    }

    .ticket-wrapper {
        position: relative;
        width: 50%;
        margin-bottom: 40px;
    }

    .discount-info {
        text-align: center;
        color: var(--primary-color);
        font-size: 18px;
        font-weight: 500;
        margin-top: 24px;
        padding: 16px;
        background: rgba(85, 146, 252, 0.1);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
    }

    .discount-icon {
        font-size: 24px;
    }

    .footer {
        position: fixed;
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
    }

    .footer-logo {
        height: 40px;
        width: auto;
        object-fit: contain;
    }

    .footer-text {
        color: white;
        font-size: 16px;
        font-weight: 500;
        letter-spacing: 0.5px;
    }

    .footer {
        position: fixed;
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
