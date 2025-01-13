<script lang="ts">
    import { onMount } from 'svelte';
    import html2canvas from 'html2canvas';
    import backgroundImage from '../assets/image_background.jpg';
    import characterImage from '../assets/image_character.jpg';
    
    let userName = '';
    let theme1Image = '';
    let theme2Image = '';
    let visitDate = '';
    let isLoading = true;
    let showTicket = false;
    let isCompleted = false;
    let ticketRef: HTMLDivElement;
    let ticketNumber = Math.floor(Math.random() * 90000) + 10000;
    
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

    onMount(() => {
        window.scrollTo(0, 0);
        // 4초 후에 완료 메시지 표시
        setTimeout(() => {
            isCompleted = true;
            // 1초 후에 로딩 화면을 올리고 티켓 표시
            setTimeout(() => {
                isLoading = false;
                setTimeout(() => {
                    showTicket = true;
                }, 500);
            }, 1000);
        }, 4000);
    });
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
        <div class="ticket-wrapper">
            <div class="ticket" bind:this={ticketRef}>
                <div class="ticket-background" style="background-image: url({backgroundImage})">
                    <div class="character-image">
                        <img src={characterImage} alt="Character" />
                    </div>
                    
                    <div class="ticket-info">
                        <div class="ticket-header">
                            <h1>IMMERSIVE EXHIBITION</h1>
                            <span class="ticket-number">No. {ticketNumber}</span>
                        </div>

                        <div class="info-grid">
                            <div class="info-item">
                                <span class="label">방문자</span>
                                <span class="value">{userName || '홍길동'}</span>
                            </div>
                            
                            <div class="info-item">
                                <span class="label">방문일</span>
                                <span class="value">{visitDate || '2024.03.21'}</span>
                            </div>
                            
                            <div class="info-item">
                                <span class="label">발매일</span>
                                <span class="value">{issueDate}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="save-button-container">
                <button class="save-button" on:click={saveTicket}>
                    저장하기
                    <span class="save-icon">💾</span>
                </button>
            </div>
        </div>
        {/if}
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
    }
    
    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #FF6B1A;
        border-top: 5px solid transparent;
        border-radius: 50%;
        margin: 0 auto 20px;
        animation: spin 1s linear infinite;
    }
    
    .loading-content p {
        font-size: 24px;
        font-weight: bold;
        color: #FF6B1A;
    }
    
    .loading-spinner.hide {
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .loading-text, .complete-text {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        transition: all 0.3s ease;
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
        background: white;
        width: 100%;
        max-width: 600px;
        aspect-ratio: 1.8;
        border-radius: 15px;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.4);
        position: relative;
        overflow: hidden;
    }

    .ticket-background {
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        position: relative;
        display: flex;
        background-repeat: no-repeat;
    }

    .character-image {
        width: 35%;
        height: 50%;
        position: relative;
        top: 25%;
        bottom: 25%;
        overflow: hidden;
        border-right: 2px solid rgba(255, 255, 255, 0.3);
    }

    .character-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .ticket-info {
        width: 65%;
        padding: 20px;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(5px);
        margin-left: auto;
        color: white;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
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
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
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
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }

    .ticket::before {
        content: '';
        position: absolute;
        top: -8px;
        left: 0;
        right: 0;
        height: 16px;
        background-image: linear-gradient(45deg, transparent 33.333%, #ffffff 33.333%, #ffffff 66.667%, transparent 66.667%),
            linear-gradient(-45deg, transparent 33.333%, #ffffff 33.333%, #ffffff 66.667%, transparent 66.667%);
        background-size: 16px 32px;
        background-position: 0 0;
        background-repeat: repeat-x;
        transform: rotate(180deg);
    }

    .ticket::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        right: 0;
        height: 16px;
        background-image: linear-gradient(45deg, transparent 33.333%, #111111 33.333%, #111111 66.667%, transparent 66.667%),
            linear-gradient(-45deg, transparent 33.333%, #111111 33.333%, #111111 66.667%, transparent 66.667%);
        background-size: 16px 32px;
        background-position: 0 0;
        background-repeat: repeat-x;
    }

    .ticket-background::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(90deg, 
            rgba(0, 0, 0, 0.1) 0%, 
            rgba(0, 0, 0, 0) 50%
        );
        pointer-events: none;
    }

    :global(body) {
        background: #111111;
        margin: 0;
        padding: 0;
    }

    .save-button-container {
        position: fixed;
        bottom: 100px;
        right: 100px;
        z-index: 10;
    }
    
    .save-button {
        padding: 12px 24px;
        background: #FF6B1A;
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
        background: #ff8142;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
    }
    
    .save-icon {
        font-size: 20px;
    }

    .ticket-wrapper {
        position: relative;
        width: 100%;
        max-width: 600px;
        margin-bottom: 80px;
    }
</style>
