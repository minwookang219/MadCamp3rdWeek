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
  let showLeftLogo3 = false;
  let showLeftLogo3_5 = false;
  let showLeftLogo4 = false;
  let showWideTexts = false;
  let showTitle = false;
  let showSideLine = false;
  let showSideBar = false;
  let showStartBtn = false;

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
      setTimeout(() => {
        showLeftLogo3 =true;
        showLeftLogo3_5 =true;
        showLeftLogo4 =true;
      }, 8000);
      setTimeout(() => {
        showWideTexts =true;
        showTitle =true;
      }, 8500);
      setTimeout(() => {
        showSideLine =true;
      }, 9500);
      setTimeout(() => {
        showSideBar =true;
      }, 10500);
      setTimeout(() => {
        showStartBtn =true;
      }, 12000);
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
    class:uplogo3={showUpLogo3} 
    class:leftlogo3={showLeftLogo3}>
    <div class="logo-grid3" >
      <div class="logo-row2" >
          <div class="logo-item2" >ㅁ</div>
          <div class="logo-item2" >ㅇ</div>
      </div>
      <div class="logo-row2 bottom-row2">
          <div class="logo-item3"
          class:uplogo3={showUpLogo3}
          class:leftlogo3={showLeftLogo3}>{item3Text1}</div>
          <div class="logo-item2">ㅅ</div>
      </div>
    </div>
  </div>
  <div 
    class="logo-container3-5"
    class:uplogo3-5={showUpLogo3_5} 
    class:leftlogo3-5={showLeftLogo3_5}>
    <div class="logo-grid3" >
      <div class="logo-row2" >
          <div class="logo-item2" >ㅁ</div>
          <div class="logo-item2" >ㅇ</div>
      </div>
      <div class="logo-row2 bottom-row2">
          <div class="logo-item2">ㅈ</div>
          <div class="logo-item3"
          class:uplogo3-5={showUpLogo3_5}
          class:leftlogo3-5={showLeftLogo3_5}>{item3Text2}</div>
      </div>
    </div>
  </div>
  <div 
    class="logo-container4"
    class:uplogo4={showUpLogo4}
    class:leftlogo4={showLeftLogo4}
  >
    <div class="logo-grid3" >
      <div class="logo-row2" >
          <div class="logo-item2" >ㅁ</div>
          <div class="logo-item2" >ㅇ</div>
      </div>
      <div class="logo-row2 bottom-row2">
          <div class="logo-item3"
          class:uplogo4={showUpLogo4}
          class:leftlogo4={showLeftLogo4}>{item3Text3}</div>
          <div class="logo-item2">ㅅ</div>
      </div>
    </div>
  </div>

  {/if}

  {#if showWideTexts}
    <div class="wide-texts">
      <div class="wide-text1">먹고싶다</div>
      <div class="wide-text2">치미말고 동치미</div>
      <div class="wide-text3">도 먹고싶다</div>
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
    <div class="click-guide0">
      ? 몰입 전시 ?
    </div>
    <div class="click-guide">
      Click the box
    </div>
  {/if}

  <div class="title-text1"
  class:jjajan={showSideBar}>
      <div class="black-title">몰입전시 팝업 스토어 : 전 시 회 몰입전시 팝업 스토어 : 전 시 회 몰입전시 팝업 스토어 : 전 시 회</div>
  </div>

  <div class="title-text2"
  class:jjajan={showSideBar}>
      <div class="black-title">몰입</div>
      <div class="white-title">전시 팝업 스토어 : 전 시 회</div>
  </div>

  <div class="white-side"
  class:doodoong={showTitle}>
  <div class="black-line1"
  class:jjajan={showSideLine}></div>
    <div class="side-text">
      <div>조각상 이미지 생성,</div>
      <div>화가의 화풍으로 배경 생성,</div>
      <div>나만의 오리지널 티켓 제작</div>
    </div>
  <div class="black-line2"
  class:jjajan={showSideLine}></div>
</div>

<div class="start-btn"
class:jjajan={showStartBtn}
class:clickable={showStartBtn}
on:click={goToTheme1}>시작하기 ▶</div>

  
  <div class="white-line1"
  class:jjajan={showSideLine}></div>
  <div class="white-line2"
  class:jjajan={showSideLine}></div>

  <div>
    <div class="down-eng2-1"
    class:jjajan={showSideBar}> 2025.02.15</div>
    <div class="down-eng1-1"
    class:jjajan={showSideBar}> 2025.02.15</div>
    <div class="down-eng2-2"
    class:jjajan={showSideBar}> ~2025.09.02</div>
    <div class="down-eng1-2"
    class:jjajan={showSideBar}> ~2025.09.02</div>
  </div>
  <div class="down-date1"
  class:jjajan={showSideBar}> MAD EXHIBITION's</div>
  <div class="down-date2"
  class:jjajan={showSideBar}> 1ST POP UP STORE</div>
  
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
  z-index: 9; /* 높은 레이어 설정 */
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
  transform: scale(0.3) translateY(1120px); /* 크기를 줄이고 아래로 이동 */
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
  z-index: 8; /* 낮은 레이어 설정 */
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
  transform: scale(0.3) translateY(1120px); /* 크기를 줄이고 아래로 이동 */
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
  z-index: 7; /* 낮은 레이어 설정 */
}

.logo-container3.uplogo3 {
  transform: translateY(-120px) translateX(-190px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-container3.leftlogo3 {
  transform: translateY(-350px) translateX(-650px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-container3-5 {
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
  z-index: 6; /* 낮은 레이어 설정 */
}

.logo-container3-5.uplogo3-5 {
  transform: translateY(-120px) translateX(-80px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-container3-5.leftlogo3-5 {
  transform: translateY(-150px) translateX(-825px); /* 크기를 줄이고 아래로 이동 */
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
  z-index: 5;
}

.logo-container4.uplogo4 {
  transform: translateY(-120px) translateX(380px); /* 크기를 줄이고 아래로 이동 */
  transition: transform 1s ease; /* 애니메이션 부드럽게 */
}

.logo-container4.leftlogo4 {
  transform: translateY(50px) translateX(-650px); /* 크기를 줄이고 아래로 이동 */
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

@keyframes fadeInFromLeft {
  0% {
    transform: translateX(0); /* 화면 밖 왼쪽에서 시작 */
    background-color: transparent;
    color: transparent;
  }
  50% {
    background-color: black; /* 배경 등장 */
    color: transparent; /* 글자는 여전히 투명 */
  }
  100% {
    transform: translateX(0); /* 원래 위치 */
    background-color: black; /* 배경 유지 */
    color: white; /* 글자 등장 */
  }
}

.wide-texts{
  padding: 0px;
  padding-right: 480px;
  padding-bottom: 0px;
  margin: 0px;
  z-index: 4;
  font-weight: 800;
}

.wide-text1{
  padding: 0px;
  padding-bottom: 40px;
  margin: 0px;
  margin-left: 140px;
  line-height: 1;
  display: flex;
  justify-content: left;
  align-items: center;
  background: #ff000000;
  color: #ffffff;
  font-size: 160px;
  z-index: 4;
  animation: fadeInFromLeft 1s ease-in-out forwards; /* 애니메이션 추가 */
  animation-delay: var(0s); /* 각 텍스트에 시간 차이를 두기 위해 변수 사용 */

}
.wide-text2{
  line-height: 1;
  padding: 0px;
  padding-bottom: 40px;
  margin: 0px;
  margin-left: 140px;
  display: flex;
  justify-content: left;
  align-items: center;
  background: #ff000000;
  color: #ffffff;
  font-size: 160px;
  z-index: 4;
  animation: fadeInFromLeft 2s ease-in-out forwards; /* 애니메이션 추가 */
  animation-delay: var(0.5s); /* 각 텍스트에 시간 차이를 두기 위해 변수 사용 */

}
.wide-text3{
  line-height: 1;
  padding: 0px;
  padding-bottom: 100px;
  margin: 0px;
  margin-left: 140px;
  display: flex;
  justify-content: left;
  align-items:first baseline;
  background: #ff000000;
  color: #ffffff;
  font-size: 160px;
  z-index: 4;
  animation: fadeInFromLeft 3s ease-in-out forwards; /* 애니메이션 추가 */
  animation-delay: var(1s); /* 각 텍스트에 시간 차이를 두기 위해 변수 사용 */

}

.white-side{
  position: absolute; /* 위치를 절대값으로 설정 */
  right: 0; /* 화면의 오른쪽 끝에 붙이기 */
  top: 0; /* 화면의 위쪽 끝에 붙이기 */
  width:23.8%;
  height:100%;
  background-color: #ffffff;
  display: flex;
  justify-content: left;
  align-items: center;
  opacity: 0;
  z-index: 21;
}

.white-side.doodoong{
  opacity: 1;
  transition: opacity 1s ease;
}

.side-text{
  font-size: 32px;
  display: flex;
  flex-direction: column; /* 세로 정렬 */
  justify-content: flex-start; /* 수직 방향으로 시작 지점 정렬 */
  align-items: flex-start; /* 가로 방향으로 왼쪽 정렬 */
  padding: 16px; /* 여백 추가 */
  margin-bottom: 80px;
}

.side-text > div {
  font-weight: 800;
  margin-bottom: 60px;
}

.title-text1{
  display: flex;
  position: absolute; /* 위치를 절대값으로 설정 */
  left: -180px; /* 화면의 오른쪽 끝에 붙이기 */
  top: 10px; /* 화면의 위쪽 끝에 붙이기 */
  width: 100%;
  z-index: 22;
  opacity: 0;
  
}

.title-text1.jjajan{
  opacity: 1;
  transition: opacity 1s ease;
}

.title-text2{
  display: flex;
  position: absolute; /* 위치를 절대값으로 설정 */
  right: 0; /* 화면의 오른쪽 끝에 붙이기 */
  top: 10px; /* 화면의 위쪽 끝에 붙이기 */
  width: 27.8%;
  z-index: 22;
  opacity: 0;
}

.title-text2.jjajan{
  opacity: 1;
  transition: opacity 1s ease;
}

.white-title {
  font-weight: 800;
  font-size: 38px;
  color: #000000;
}
.black-title {
  font-weight: 800;
  font-size: 38px;
  color: #ffffff;
}

.white-line1 {
  position: absolute; /* z-index를 적용하려면 position 속성이 필요 */
  top: 7%;
  width: 100%;
  height: 2px;
  background-color: #ffffff;
  margin: 10px ;
  z-index: 20;
  opacity: 0;
}

.black-line2 {
  position: absolute; /* z-index를 적용하려면 position 속성이 필요 */
  top: 80%;
  width: 100%;
  height: 2px;
  background-color: #000000;
  margin-top: 10px ;
  z-index: 23;
  opacity: 0;
}
.white-line2 {
  position: absolute; /* z-index를 적용하려면 position 속성이 필요 */
  top: 80%;
  width: 100%;
  height: 2px;
  background-color: #ffffff;
  margin: 10px ;
  z-index: 20;
  opacity: 0;
}
.black-line1 {
  position: absolute; /* z-index를 적용하려면 position 속성이 필요 */
  top: 7%;
  width: 100%;
  height: 2px;
  background-color: #000000;
  margin-top: 10px ;
  z-index: 23;
  opacity: 0;
}

.down-date1{
  position: absolute;
  font-size: 72px;
  top: 80%;
  left: 1%;
  width: 45%;
  color:aquamarine;
  font-weight: 900;
  z-index: 25;
  letter-spacing: 6px; /* 글자 간격 (px 단위) */
  opacity: 0;
}
.down-date2{
  position: absolute;
  font-size: 72px;
  top: 89%;
  left: 1%;
  width: 45%;
  color: aquamarine;
  font-weight: 900;
  z-index: 25;
  letter-spacing: 6px; /* 글자 간격 (px 단위) */
  opacity: 0;
}
.down-eng1-1{
  position: absolute;
  font-size: 72px;
  top: 80%;
  left: 43%;
  width: 45%;
  color: #ffffff;
  z-index: 25;
  letter-spacing: -1px; /* 글자 간격 (px 단위) */
  opacity: 0;
}
.down-eng1-2{
  position: absolute;
  font-size: 72px;
  top: 80%;
  left: 65.4%;
  width: 45%;
  color: #ff55ff;
  z-index: 25;
  letter-spacing: -1px; /* 글자 간격 (px 단위) */
  opacity: 0;
}
.down-eng2-1{
  position: absolute;
  font-size: 72px;
  top: 89%;
  left: 43%;
  width: 45%;
  color: #ffffff;
  z-index: 25;
  letter-spacing: -1px; /* 글자 간격 (px 단위) */
  opacity: 0;
}
.down-eng2-2{
  position: absolute;
  font-size: 72px;
  top: 89%;
  left: 65.4%;
  width: 45%;
  color: #ff55ff;
  z-index: 25;
  letter-spacing: -1px; /* 글자 간격 (px 단위) */
  opacity: 0;
}

.start-btn{
  position: absolute;
  top: 73%;
  right: 7%;
  font-size: 48px;
  color: #000000;
  z-index: 30;
  font-weight: 600;
  opacity: 0;
}

.start-btn.clickable {
  cursor: pointer;
  transition: transform 0.2s ease;
}

.start-btn.clickable:hover {
  transform: scale(1.02);
}

.start-btn.jjajan, .white-line1.jjajan, .white-line2.jjajan,
.black-line1.jjajan, .black-line2.jjajan, .down-date1.jjajan, 
.down-date2.jjajan, .down-eng1-1.jjajan, .down-eng1-2.jjajan,
.down-eng2-1.jjajan, .down-eng2-2.jjajan {
  opacity: 1; /* 이 상태로 전환될 수 있도록 설정 */
  transition: opacity 1s ease;
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

.click-guide0 {
  position: absolute;
  font-weight: 800;
  top: 10%;
  left: 50%;
  transform: translateX(-50%);
  color: #111111;
  font-size: 100px;
  opacity: 0;
  animation: fadeIn 1s ease 1s forwards;
}
.click-guide {
  position: absolute;
  font-weight: 500;
  top: 75%;
  left: 50%;
  transform: translateX(-50%);
  color: #111111;
  font-size: 30px;
  opacity: 0;
  animation: fadeIn 1s ease 1s forwards;
}
</style>
