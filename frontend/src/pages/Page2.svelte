<!-- // src/routes/About.svelte -->
<script>
    // 이미지 import
    import sculpture1 from '../assets/images_tab1/statue_1.webp';
    import sculpture2 from '../assets/images_tab1/statue_2.webp';
    import sculpture3 from '../assets/images_tab1/statue_3.webp';
    import sculpture4 from '../assets/images_tab1/statue_4.webp';
    import sculpture5 from '../assets/images_tab1/statue_5.webp';

    // 슬라이더 애니메이션을 위한 변수
    let isHovered = false;
</script>

<main>
    <div class="section-divider"></div>
    
    <section class="description-section">
        <!-- 상단 슬라이더 -->
        <div class="slider-container top" 
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
        <h2>기능 구현 영역</h2>
        <h2>
        <!-- 여기에 기능 구현 관련 컴포넌트들이 들어갈 예정입니다 -->
         
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
        min-height: 100vh;
        padding: 20px;
    }
</style>

