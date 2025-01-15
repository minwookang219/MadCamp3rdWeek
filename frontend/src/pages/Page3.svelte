<!-- // src/routes/About.svelte -->

<script lang="ts">
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    import logoImage from '../assets/logo_images.png';
    import { resultImageStore, characterImageStore } from '../store';
    import { get } from 'svelte/store';
    let progress = 98; // 마지막 단계
    let userName = '';
    let showPhoneInput = false;
    let phoneNumber = '';
    let showDateInput = false;
    let visitDate = '';
    let isFormCompleted = false;
    let BackgroundImage: string | null = null;
    let CharacterImage: string | null = null;

    onMount(() => {
        BackgroundImage = get(resultImageStore);
        CharacterImage = get(characterImageStore);
        window.scrollTo(0, 0);
    });

    function handleNameSubmit() {
        if (userName.trim()) {
            showPhoneInput = true;
        } else {
            alert('이름을 입력해주세요.');
        }
    }

    function handlePhoneSubmit() {
        showDateInput = true;
    }

    function handleDateSubmit() {
        if (!visitDate) {
            alert('방문일자를 선택해주세요.');
        } else {
            isFormCompleted = true;
        }
    }

    function handleCreateTicket() {
        navigate('/theme4');
    }

    function formatPhoneNumber(value: string) {
        const numbers = value.replace(/[^\d]/g, '');
        if (numbers.length <= 3) return numbers;
        if (numbers.length <= 7) return numbers.slice(0, 3) + '-' + numbers.slice(3);
        return numbers.slice(0, 3) + '-' + numbers.slice(3, 7) + '-' + numbers.slice(7, 11);
    }

    function handlePhoneInput(event: Event) {
        const input = event.target as HTMLInputElement;
        input.value = formatPhoneNumber(input.value);
        phoneNumber = input.value;
    }

    onMount(() => {
        window.scrollTo(0, 0);
    });
</script>

<main class="main">
    <div class="title-container">
        <div class="title">3. 티켓 마무리</div>
        <div class="title2">이름, 전화번호, 방문일을 적고, 만든 티켓을 확인해요!</div>
    </div>

    <div class="content-container">
        <!-- 좌측: 사용자 정보 입력 -->
        <div class="left-section">
            <div class="input-group">
                <label for="name">이름을 입력해주세요</label>
                <div class="input-button-wrapper">
                    <input 
                        type="text" 
                        id="name" 
                        bind:value={userName}
                        placeholder="이름"
                        required
                    />
                    <button class="submit-button" on:click={handleNameSubmit}>
                        확인
                    </button>
                </div>
            </div>

            {#if showPhoneInput}
                <div class="input-group">
                    <label for="phone">전화번호를 입력해주세요</label>
                    <div class="input-button-wrapper">
                        <input 
                            type="tel" 
                            id="phone" 
                            value={phoneNumber}
                            on:input={handlePhoneInput}
                            placeholder="010-0000-0000"
                            required
                        />
                        <button class="submit-button" on:click={handlePhoneSubmit}>
                            확인
                        </button>
                    </div>
                </div>
            {/if}

            {#if showDateInput}
                <div class="input-group">
                    <label for="date">방문일을 선택해주세요</label>
                    <div class="input-button-wrapper">
                        <input 
                            type="date" 
                            id="date" 
                            bind:value={visitDate}
                            min={new Date().toISOString().split('T')[0]}
                            required
                        />
                        <button class="submit-button" on:click={handleDateSubmit}>
                            확인
                        </button>
                    </div>
                </div>
            {/if}
        </div>

        <!-- 우측: 이미지 미리보기 -->
        <div class="right-section">
            <div class="images-container fade-in">
                <h2>나의 작품들</h2>
                <div class="images-grid">
                    <div class="image-item">
                        <h3>조각상 작품</h3>
                        <img src={CharacterImage} alt="조각상" />
                    </div>
                    <div class="image-item">
                        <h3>배경</h3>
                        <img src={BackgroundImage} alt="그림" />
                    </div>
                </div>
            </div>

            {#if isFormCompleted}
                <div class="ticket-button-container fade-in">
                    <button class="ticket-button" on:click={handleCreateTicket}>
                        티켓 만들기
                        <span class="arrow">→</span>
                    </button>
                </div>
            {/if}
        </div>


    </div>
    
    <hr class="black-line">
    <hr class="black-line2">

    <!-- 진행 바 -->
    <div class="progress-bar">
        <div class="progress" style={`width: ${progress}%;`}></div>
        <div class="progress-sections">
            <div class="section"></div>
            <div class="section">99.9%</div>
            <div class="section"></div>
        </div>
    </div>

    <div class="footer">
        <div class="footer-content">
            <img src={logoImage} alt="전시회 로고" class="footer-logo" />
            <div class="footer-text">
                몰입전시 팝업스토어 "전시회"
            </div>
        </div>
    </div>

</main>

<style>
    .main {
        background-color: #000000;
        padding-bottom: 350px;
    }

    .title-container {
        position: relative;
        margin-top: 50px;
        width: 100%;
        margin-left: 0%;
        margin-right: 0%;
        padding: 20px;
        background-color: #000000;
        z-index: 1000;
    }

    .title {
        font-size: 76px;
        font-weight: bold;
        color: #FF8A01;
        text-align: center;
        letter-spacing: 8px;
    }
    .title2 {
        font-size: 18px;
        font-weight: 400;
        color: #FF8A01;
        text-align: center;
        letter-spacing: 6px;
        padding-top: 8px;
    }

    .content-container {
        display: flex;
        justify-content: space-between;
        width: 68%;
        margin: 32px 16% 0 16%;
        gap: 64px;
    }

    .left-section {
    flex: 3;
    width: 100%;
    background-color: #000000;
    border: 2px solid #FF8A01; /* 두께, 스타일, 색상 */
    padding: 32px;
    border-top-left-radius: 0px;     /* 왼쪽 상단 모서리 반경 */
    border-top-right-radius: 16px;    /* 오른쪽 상단 모서리 반경 */
    border-bottom-right-radius: 16px; /* 오른쪽 하단 모서리 반경 */
    border-bottom-left-radius: 0px;  /* 왼쪽 하단 모서리 반경 */
}

.right-section {
    flex: 7;
    width: 100%;
    background-color: #FF8A01;
    border: 2px solid #000000; /* 두께, 스타일, 색상 */
    padding: 32px;
    padding-top: 8px;
    border-top-left-radius: 16px;     /* 왼쪽 상단 모서리 반경 */
    border-top-right-radius: 0px;    /* 오른쪽 상단 모서리 반경 */
    border-bottom-right-radius: 0px; /* 오른쪽 하단 모서리 반경 */
    border-bottom-left-radius: 16px;  /* 왼쪽 하단 모서리 반경 */
}

    .black-line {
        width: 100%;
        position: absolute;
        top: 4.5%;
        border: 4px solid #FF8A01; /* 두께, 스타일, 색상 */
        padding: 0px;
        border-radius: 12px;
        z-index: 2000;
    }
    .black-line2 {
        width: 100%;
        position: absolute;
        top: 21.5%;
        border: 2px solid #FF8A01; /* 두께, 스타일, 색상 */
        padding: 0px;
        z-index: 2000;
    }

    .input-group {
        margin-bottom: 24px;
        width: 100%;
        
    }

    label {
        display: block;
        color: #FF8A01;
        font-weight: 600;
        margin-bottom: 12px;
        font-size: 20px;
        text-align: center;
        width: 100%;
    }

    input {
        width: 60%;
        padding: 16px;
        border: 2px solid #FF8A01;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.1);
        color: #FF8A01;
        font-size: 18px;
        text-align: center;
        margin-bottom: 16px;
        cursor: pointer;
    }

    input[type="date"] {
        padding: 14px 16px;
        text-align: center;
        font-family: inherit;
    }

    input[type="date"]::-webkit-calendar-picker-indicator {
        cursor: pointer;
        font-size: 18px;
        padding: 4px;
    }

    input:focus {
        border-color: var(--primary-color);
        outline: none;
    }

    /* 진행 바 스타일 */
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
        background-color: #FF8A01;
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

    :global(body) {
        background: #111111;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    .submit-button {
        width: 100px;
        padding: 16px 0;
        background: #FF8A01;
        color: black;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        height: 56px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .submit-button:hover {
        background: #FF8A01;
        transform: translateY(-2px);
    }

    .fade-in {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeIn 0.3s ease forwards;
    }

    @keyframes fadeIn {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .images-container {
        margin-top: 8px;
        text-align: center;
        width: 100%;
        background-color: #FF000000;
    }

    .images-container h2 {
        color: #000000;
        font-size: 32px;
        margin-bottom: 16px;
    }

    .images-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        margin-top: 16px;
        align-items: center;
    }

    .image-item {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: start;
        justify-content: left;
        padding-left: 12px;
    }

    .image-item h3 {
        color: #000000;
        font-size: 20px;
        margin-bottom: 20px;
        padding-left: 12px;
    }

    .image-item img {
        width: 80%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        object-fit: contain;
    }

    .ticket-button-container {
        display: flex;
        margin-top: 40px;
        text-align: center;
        align-items: end;
        justify-content: end;
    }

    .ticket-button {
        padding: 20px 4px;
        background: #FF8A01;
        color: black;
        border-radius: 12px;
        font-size: 24px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: end;
        justify-content: end;
        gap: 12px;
    }

    .ticket-button:hover {
        background: #FF8A01;
        transform: translateY(-2px) scale(1.04);
        border: 2px solid #FF8A01; /* 두께, 스타일, 색상 */
    }

    .ticket-button .arrow {
        font-size: 24px;
        transition: transform 0.2s ease;
    }

    .ticket-button:hover .arrow {
        transform: translateX(4px);
    }

    .input-button-wrapper {
        display: flex;
        gap: 12px;
        justify-content: flex-start;
        width: 100%;
        background-color: #000000;
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
