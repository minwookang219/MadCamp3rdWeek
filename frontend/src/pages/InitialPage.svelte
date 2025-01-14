<script lang="ts">
  import { navigate } from 'svelte-routing';
  import { onMount } from 'svelte';
  let showFirstNemo = true;
  let FistUpscale = false;
  let showFullLogo = false;
  let showDarkMode = false;
  let showDownLogo = false;
  let showLogo3 = false;
  let showUpLogo3 = false;
  let showUpLogo3_5 = false;
  let showUpLogo4 = false;

  let item3Text1 = 'ㅈ';
  let item3Text2 = 'ㅅ';
  let item3Text3 = 'ㅎ';

  function changeText() {
    item3Text1 = '전'; // 원하는 텍스트로 변경
    setTimeout(() =>{
      item3Text2 = '시'; // 원하는 텍스트로 변경
    }, 500);
    setTimeout(() =>{
      item3Text3 = '회'; // 원하는 텍스트로 변경
    }, 1000);
  }


  let showTransformed = false;
  let showFinalText = false;

  function handleLogoClick2() {
    if (showFirstNemo) {
      FistUpscale = true;
      setTimeout(() => {
        showFirstNemo = false;
        showFullLogo = true;
      }, 1000);   
      setTimeout(() => {
        showDarkMode = true;
      }, 2500);  
      setTimeout(() => {
        showDownLogo = true;
        showLogo3 = true;
      }, 4500);
      setTimeout(() => {
        showUpLogo3 = true;
        showUpLogo3_5 = true;
        showUpLogo4 = true;
      }, 5000);
      setTimeout(() => {
        changeText();
      }, 6500);
    }
  }

  function goToTheme1() {
    navigate('/theme1_0');
  }
</script>

<div class="main-pages">
<div class="home-main"
  class:darkmode-back={showDarkMode}>
  <div class="logo-container1"
  class:container-large={FistUpscale}
  class:text-out={FistUpscale} 
  class:container-small={!showFirstNemo} 
  class:clickable={showFirstNemo}
  class:darkmode-logoline={showDarkMode}
  class:downscale={showDownLogo}
  on:click={handleLogoClick2}>
   ? 
  </div>
  <div 
    class="logo-container2"
    class:text-fade-in={showFullLogo}
    class:downscale={showDownLogo}>
    <div class="logo-grid">
      <div class="logo-row" >
          <div class="logo-item fade-item" 
          class:fade-in={showFullLogo}
          class:darkmode-text={showDarkMode}
          class:downscale={showDownLogo}>ㅁ</div>
          <div class="logo-item fade-item" 
          class:fade-in={showFullLogo}
          class:darkmode-text={showDarkMode}
          class:downscale={showDownLogo}>ㅇ</div>
      </div>
      <div class="logo-row">
          <div class="logo-item"
          class:darkmode-text={showDarkMode}
          class:downscale={showDownLogo}>ㅈ</div>
          <div class="logo-item"
          class:darkmode-text={showDarkMode}
          class:downscale={showDownLogo}>ㅅ</div>
      </div>
    </div>
  </div>

  {#if showLogo3}
  <div 
    class="logo-container3"
    class:uplogo3={showUpLogo3} >
    <div class="logo-grid3" >
      <div class="logo-row2" >
          <div class="logo-item2" >ㅁ</div>
          <div class="logo-item2" >ㅇ</div>
      </div>
      <div class="logo-row2 bottom-row2">
          <div class="logo-item3"
          class:uplogo3={showUpLogo3}>{item3Text1}</div>
          <div class="logo-item2">ㅅ</div>
      </div>
    </div>
  </div>
  <div 
    class="logo-container3-5"
    class:uplogo3-5={showUpLogo3_5} >
    <div class="logo-grid3" >
      <div class="logo-row2" >
          <div class="logo-item2" >ㅁ</div>
          <div class="logo-item2" >ㅇ</div>
      </div>
      <div class="logo-row2 bottom-row2">
          <div class="logo-item2">ㅈ</div>
          <div class="logo-item3"
          class:uplogo3-5={showUpLogo3_5}>{item3Text2}</div>
      </div>
    </div>
  </div>
  <div 
    class="logo-container4"
    class:uplogo4={showUpLogo4}
  >
    <div class="logo-grid3" >
      <div class="logo-row2" >
          <div class="logo-item2" >ㅁ</div>
          <div class="logo-item2" >ㅇ</div>
      </div>
      <div class="logo-row2 bottom-row2">
          <div class="logo-item3"
          class:uplogo4={showUpLogo4}>{item3Text3}</div>
          <div class="logo-item2">ㅅ</div>
      </div>
    </div>
  </div>

  {/if}


  {#if showTransformed && showFirstNemo}
          <div class="logo-item slide-in" class:fade-out={showFinalText}>
            {#if !showFinalText && showFirstNemo}ㅎ{/if}
          </div>
        {/if}
        {#if showFinalText && !showFirstNemo}
          <div class="logo-container3">
            <div class="logo-item final-text">전</div>
            <div class="logo-item final-text">시</div>
            <div class="logo-item final-text">회</div>
          </div>
        {/if}

  {#if !showFullLogo}
    <div class="click-guide">
      Click
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
.main-pages {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  position: relative;
}

.home-main {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.home-main.darkmode-back{
  background-color: #000000;
  transition: all 1s ease;
}

.logo-container1 {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff000000;
  border-radius: 4px;
  padding: 12px 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 110px;
  height: 100px;
  border: 12px solid #111111;
  transition: all 0.5s ease;
  font-size: 60px;
  z-index: 5; /* 높은 레이어 설정 */
}

.logo-container1.clickable {
  cursor: pointer;
  transition: transform 0.2s ease;
}

.logo-container1.clickable:hover {
  transform: scale(1.02);
}

.logo-container1.text-out {
  color: #ff000000;
}

.logo-container1.container-large {
  height: 350px;
  width: 350px;
  border: 28px solid #111111;
  transition: all 1.5s ease;
}

.logo-container1.darkmode-logoline {
  border: 28px solid #ffffff;
  transition: border 1s ease;
}

.logo-container1.downscale {
  transform: scale(0.3) translateY(1200px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-container1, .logo-container2 {
  position: absolute; 
}

.logo-container2 {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff000000;
  border-radius: 4px;
  padding: 12px 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 350px;
  height: 350px;
  opacity: 0;
  /* border: 28px solid #111111; */
  transition: all 1s ease;
  z-index: 4; /* 낮은 레이어 설정 */
}

.logo-container2.container-small {
  height: 200px;
  width: 600px;
}

.logo-container2.text-fade-in {
  opacity: 1;
  transition: all 1s ease;
}

.logo-container2.clickable {
  cursor: pointer;
  transition: transform 0.2s ease;
}

.logo-container2.clickable:hover {
  transform: scale(1.02);
}

.logo-container2.downscale {
  transform: scale(0.3) translateY(1200px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-grid {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  height: 100%;
  transition: all 1s ease;
  position: relative;
}


.logo-grid.transform-active {
  height: 280px;
  width: 550px;
  transition: all 1s ease;
}

.logo-grid3 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  height: 100%;
  transition: all 1s ease;
  position: relative;
}

.logo-row {
  display: flex;
  align-items: center;
  gap: 5px;
  justify-content: center;
  transition: all 1s ease;
  width: 100%;
}

.logo-row.fade-out {
  opacity: 0;
  height: 0;
  margin: 0;
  transform: translateY(-20px);
  transition: all 1s ease;
}

.logo-row2 {
  display: flex;
  align-items: center;
  gap: 5px;
  justify-content: center;
  transition: all 1s ease;
  width: 100%;
}

.bottom-row {
  /* gap: 10px;
  width: 100%; */
}

.bottom-row:has(.final-text) {
  gap: 0;
  padding: 0;
  align-items: center;
  justify-content: center;
}

.logo-container3 {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff000000;
  border-radius: 4px;
  padding: 12px 5px;
  width: 350px;
  height: 350px;
  opacity: 1;
  transition: all 1s ease;
  z-index: 3; /* 낮은 레이어 설정 */
}

.logo-container3.uplogo3 {
  transform: translateY(-120px) translateX(-190px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-container3_5 {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff0000;
  border-radius: 4px;
  padding: 12px 5px;
  width: 350px;
  height: 350px;
  opacity: 1;
  transition: all 1s ease;
  z-index: 2; /* 낮은 레이어 설정 */
}

.logo-container3-5.uplogo3-5 {
  transform: translateY(-105px) translateX(-70px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-container4 {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff000000;
  border-radius: 4px;
  padding: 12px 5px;
  width: 350px;
  height: 350px;
  opacity: 1;
  transition: all 1s ease;
  z-index: 1;
}

.logo-container4.uplogo4 {
  transform: translateY(-120px) translateX(380px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-item {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff000000;
  color: #111111;
  font-size: 160px;
  font-weight: bold;
  border-radius: 10px;
  transition: all 1s ease;
  width: calc(50% - 5px);
  height: calc(50% - 5px);
  aspect-ratio: 1;
}

.logo-item.darkmode-text {
  color: #ffffff;
  transition: all 1s ease;
}

.logo-item.downscale {
  transform: scale(0.5); /* 하위 요소도 크기 축소 */
  font-size: 320px;
  transition: transform 1s ease; /* 부드러운 전환 */
}

.logo-item:hover {
  transform: scale(1);
}

.fade-item {
  opacity: 1;
  transition: opacity 1s ease;
}

.logo-item2 {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff000000;
  color: #ff000000;
  font-size: 160px;
  font-weight: bold;
  border-radius: 10px;
  transition: all 1s ease;
  width: calc(50% - 5px);
  height: calc(50% - 5px);
  aspect-ratio: 1;
}

.logo-item3 {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ff000000;
  color: #ffffff;
  font-size: 160px;
  /* font-weight: bold; */
  font-family: 'Pretendard';
  font-weight: 900;
  border-radius: 10px;
  transition: all 1s ease;
  width: calc(50% - 5px);
  height: calc(50% - 5px);
  aspect-ratio: 1;
}

.transform-active .fade-item {
  opacity: 1; /* 이 상태로 전환될 수 있도록 설정 */
  transition: opacity 1s ease;
}

.slide-in {
  opacity: 0;
  transform: translateX(-20px);
  animation: slideIn 3s ease forwards;
  font-size: 160px;
}

.final-text {
  opacity: 0;
  animation: fadeIn 1.5s ease forwards;
  font-size: 160px;
  width: calc(50% - 5px);
  margin: 10px;
  aspect-ratio: auto;
  display: flex;
  align-items: center;
  justify-content: center;
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
  top: 70%;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0;
  animation: fadeIn 1.5s ease 1.5s forwards;
  text-align: center;
}

.description-line {
  font-size: 18px;
  margin: 8px 0;
  color: #111111;
  line-height: 1.5;
}

.highlight {
  font-size: 24px;
  font-weight: bold;
  color: #111111;
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
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.click-guide {
  position: absolute;
  top: 75%;
  left: 50%;
  transform: translateX(-50%);
  color: #111111;
  font-size: 30px;
  opacity: 0;
  animation: fadeIn 1s ease 1s forwards;
}

.initial-lefttop {
  position: absolute;
  top: 180px;
  left: 50%;
  transform: translateX(-50%);
  color: #111111;
  font-size: 25px;
  opacity: 0;
  animation: fadeIn 1s ease 1s forwards;
}
</style>
