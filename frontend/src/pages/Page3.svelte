<!-- // src/routes/About.svelte -->

<script lang="ts">
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    
    let progress = 100; // 마지막 단계
    let userName = '';
    let showPhoneInput = false;
    let phoneNumber = '';
    let theme1Image = ''; // theme1의 최종 이미지
    let theme2Image = ''; // theme2의 최종 이미지

    function handleNameSubmit() {
        if (userName.trim()) {
            showPhoneInput = true;
        } else {
            alert('이름을 입력해주세요.');
        }
    }

    function handlePhoneSubmit() {
        if (!phoneNumber.match(/^\d{3}-\d{4}-\d{4}$/)) {
            alert('올바른 전화번호를 입력해주세요.');
        }
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

<main>
    <div class="title-container">
        <div class="title">티켓 만들기</div>
    </div>

    <div class="content-container">
        <!-- 좌측: 사용자 정보 입력 -->
        <div class="left-section">
            <div class="input-group">
                <label for="name">이름을 입력해주세요</label>
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

            {#if showPhoneInput}
                <div class="input-group">
                    <label for="phone">전화번호를 입력해주세요</label>
                    <input 
                        type="tel" 
                        id="phone" 
                        value={phoneNumber}
                        on:input={handlePhoneInput}
                        placeholder="010-0000-0000"
                        pattern="[0-9]{3}-[0-9]{4}-[0-9]{4}"
                        required
                    />
                    <button class="submit-button" on:click={handlePhoneSubmit}>
                        확인
                    </button>
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
                        <img src={theme1Image} alt="조각상" />
                    </div>
                    <div class="image-item">
                        <h3>그림 작품</h3>
                        <img src={theme2Image} alt="그림" />
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 진행 바 -->
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
    .title-container {
        position: relative;
        margin-top: 98px;
        width: 68%;
        margin-left: 16%;
        margin-right: 16%;
        background-color: rgba(128, 128, 128, 0.8);
        padding: 20px;
        border: 2px solid #ddd;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(5, 4, 4, 0.1);
        z-index: 1000;
    }

    .title {
        font-size: 30px;
        font-weight: bold;
        color: #333;
        text-align: center;
    }

    .content-container {
        display: flex;
        justify-content: space-between;
        width: 68%;
        margin: 64px 16% 0 16%;
        gap: 40px;
    }

    .left-section, .right-section {
        width: 100%;
        background: rgba(255, 255, 255, 0.1);
        padding: 32px;
        border-radius: 12px;
    }

    .input-group {
        margin-bottom: 24px;
    }

    label {
        display: block;
        color: #CCCCCC;
        margin-bottom: 12px;
        font-size: 20px;
        text-align: center;
    }

    input {
        width: 100%;
        padding: 16px;
        border: 2px solid #333;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.1);
        color: black;
        font-size: 18px;
        text-align: center;
        margin-bottom: 16px;
    }

    input:focus {
        border-color: #FF6B1A;
        outline: none;
    }

    /* 진행 바 스타일 */
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

    :global(body) {
        background: #111111;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    .submit-button {
        width: 100%;
        padding: 16px;
        background: #FF6B1A;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .submit-button:hover {
        background: #ff8142;
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
        margin-top: 32px;
        text-align: center;
    }

    .images-container h2 {
        color: #CCCCCC;
        font-size: 24px;
        margin-bottom: 24px;
    }

    .images-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 24px;
        margin-top: 16px;
    }

    .image-item {
        text-align: center;
    }

    .image-item h3 {
        color: #CCCCCC;
        font-size: 18px;
        margin-bottom: 12px;
    }

    .image-item img {
        width: 100%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
</style>
