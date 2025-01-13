<script lang="ts">
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    let showFullLogo = true;
    let showTransformed = false;
    let showFinalText = false;
  
    function handleLogoClick() {
      if (showFullLogo) {
        showFullLogo = false;
        setTimeout(() => {
          showTransformed = true;
          setTimeout(() => {
            showFinalText = true;
          }, 2000);
        }, 1000);   
      }
    }
  
    function goToTheme1() {
      navigate('/theme1_0');
    }
  </script>
  
  <div class="main_pages">
    <div class="home_main">
      <div class="logo-container" 
           class:container-small={!showFullLogo} 
           class:clickable={showFullLogo}
           on:click={handleLogoClick}>
        <div class="logo-grid" class:transform-active={!showFullLogo}>
          <div class="logo-row" class:fade-out={!showFullLogo}>
            {#if showFullLogo}
              <div class="logo-item fade-item">ㅁ</div>
              <div class="logo-item fade-item">ㅇ</div>
            {/if}
          </div>
          <div class="logo-row bottom-row">
            {#if !showFinalText}
              <div class="logo-item">ㅈ</div>
              <div class="logo-item">ㅅ</div>
            {/if}
            {#if showTransformed}
              <div class="logo-item slide-in" class:fade-out={showFinalText}>
                {#if !showFinalText}ㅎ{/if}
              </div>
            {/if}
            {#if showFinalText}
              <div class="logo-item final-text">전</div>
              <div class="logo-item final-text">시</div>
              <div class="logo-item final-text">회</div>
            {/if}
          </div>
        </div>
      </div>
      {#if showFullLogo}
        <div class="initial_lefttop">
            몰입전시 온라인 팝업스토어
        </div>
        <div class="click-guide">
          로고를 눌러 시작하세요
        </div>
        
      {/if}
      {#if showFinalText}
        <div class="description-container">
          <p class="description-line">
            <span class="highlight">전</span>통과 현대를 아우르는
          </p>
          <p class="description-line">
            <span class="highlight">시</span>대를 대표하는 작품들을
          </p>
          <p class="description-line">
            <span class="highlight">회</span>상하다
          </p>
        </div>
        <div class="start-button-container">
          <button class="start-button" on:click={goToTheme1}>
            시작하기
          </button>
        </div>
      {/if}
    </div>
  </div>
  


  <style>
  .main_pages {
    display: block;
    width: 100%;
    height: 100%;
    white-space: nowrap;
    align-items: center;
  }
  
  .home_main {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 1000px;
  }
  
  .home_main {
    background-color: black;
  }
  
  .logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    background: white;
    border-radius: 10px;
    padding: 10px;

    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 500px;
    height: 500px;
    transition: all 0.5s ease;
  }
  
  .logo-container:has(.logo-grid.transform-active) {
    height: 280px;
    width: 550px;
    transition: all 1.0s ease;
  }
  
  .logo-grid {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
    height: 100%;
    position: relative;
    transition: all 1.5s ease;
    padding: 20px;
  }
  
  .logo-grid.transform-active {
    grid-template-columns: repeat(3, 1fr);
  }
  
  .fade-item {
    opacity: 1;
    transition: opacity 0.5s ease;
  }
  
  .transform-active .fade-item {
    opacity: 0;
  }
  
  .slide-in {
    opacity: 0;
    transform: translateX(-20px);
    animation: slideIn 1.5s ease forwards;
    font-size: 160px;
  }
  
  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateX(-20px);
    }
    to {
      opacity: 1;
      transform: translateX(0);
    }
  }
  
  .logo-item {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #111111;
    color: white;
    font-size: 160px;
    font-weight: bold;
    border-radius: 10px;
    transition: all 0.3s ease;
    width: calc(50% - 5px);
    aspect-ratio: 1;
  }
  
  .logo-item:hover {
    transform: scale(1);
  }
  
  .logo-row {
    display: flex;
    gap: 10px;
    transition: all 0.5s ease;
    justify-content: center;
  }
  
  .logo-row.fade-out {
    opacity: 0;
    height: 0;
    margin: 0;
    transform: translateY(-20px);
  }
  
  .bottom-row {
    display: flex;
    gap: 10px;
    justify-content: center;
    width: 100%;
  }
  
  .bottom-row:has(.final-text) {
    gap: 0;
    padding: 0;
  }
  
  .container-small {
    height: 200px;
    width: 600px;
  }
  
  .final-text {
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
    font-size: 160px;
    width: calc(50% - 5px);
    margin: 10px;
    aspect-ratio: auto;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  
  .description-container {
    position: absolute;
    top: calc(50% + 200px);
    left: 50%;
    transform: translateX(-50%);
    opacity: 0;
    animation: fadeIn 1.5s ease 0.5s forwards;
  }
  
  .description-line {
    text-align: left;
    font-size: 18px;
    margin: 8px 0;
    color: white;
    line-height: 1.5;
  }
  
  .highlight {
    font-size: 24px;
    font-weight: bold;
    color: white;
  }
  
  .start-button-container {
    position: fixed;
    bottom: 40px;
    right: 40px;
    opacity: 0;
    animation: fadeIn 1.5s ease 1s forwards;
  }
  
  .start-button {
    padding: 15px 30px;
    font-size: 18px;
    background-color: white;
    color: black;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: bold;
  }
  
  .start-button:hover {
    background-color: #f0f0f0;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2);
  }
  
  .clickable {
    cursor: pointer;
    transition: transform 0.3s ease;
  }
  
  .clickable:hover {
    transform: scale(1.02);
  }
  
  .click-guide {
    position: absolute;
    top: calc(50% + 280px);
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 40px;
    opacity: 0;
    animation: fadeIn 1s ease 1s forwards;
  }

  .initial_lefttop {
    position: absolute;
    top: 80px;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 18px;
    opacity: 0;
    animation: fadeIn 1s ease 1s forwards;
  }
  </style>