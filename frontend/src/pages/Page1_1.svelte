<script lang="ts">
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    import logoImage from '../assets/logo_images.png';
    import { characterImageStore } from '../store';
    // 진행률 (0~100 사이의 값)
    let progress = 33.33333333; // 예: 현재 진행률 50%
    let sculptureText = ''; // 사용자가 입력한 텍스트를 저장
    let sculptureImage = ''; // 서버에서 받아올 이미지 URL을 저장할 변수
    let isLoading = false;
  
    // 추천 이름 목록
    let recommendedNames: string[] = [
      'Apple',
      'Steak',
      'House',
      'Horse',
      'Banana',
      'Bed',
      'Chair',
      'Iphone15',
      'Android',
      'Python',
      'Money',
      'Bitcoin',
      'Sunglasses',
      'Spider man',
      'Moon',
      'Money',
      'Bitcoin',
      'Sunglasses',
      'Spider man',
      'Moon',
      'Money',
      'Bitcoin',
      'Sunglasses',
      'Spider man',
      'Moon',
    ];
  
    console.log('Full env:', import.meta.env);
  
    async function generateSculpture() {
      if (!sculptureText.trim()) return;
      
      isLoading = true;
      try {
        const response = await fetch('http://127.0.0.1:8001/generate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            prompt: `A detailed marble sculpture of ${sculptureText} with no background, ${sculptureText} is a character, color is white`
          })
        });
    
        if (!response.ok) {
          throw new Error('조각상 생성에 실패했습니다');
        }
    
        const data = await response.json();
        
        // Base64 이미지를 URL로 변환
        if (data.images && data.images.length > 0) {
          sculptureImage = `data:image/jpeg;base64,${data.images[0]}`;
          characterImageStore.set(sculptureImage); // store에 이미지 저장
        } else {
          throw new Error('이미지 생성 결과가 없습니다');
        }
      } catch (error) {
        console.error('Error:', error);
        const errorMessage = error instanceof Error ? error.message : '알 수 없는 오류가 발생했습니다';
        alert('조각상 생성 중 오류가 발생했습니다: ' + errorMessage);
      } finally {
        isLoading = false;
      }
    }
  
    function handleRecommendedClick(name: string) {
      sculptureText = name; // 이름만 입력하고 자동 생성은 하지 않음
    }
  
    async function handleNextPage() {
      // 현재 페이지에 슬라이드 아웃 효과 적용
      document.querySelector('main')?.classList.add('page-slide-out');
      
      // 애니메이션이 완료된 후 페이지 전환
      setTimeout(() => {
        navigate('/theme2_0');
      }, 500);
    }
  
    onMount(() => {
      // 페이지 로드 시 슬라이드 인 효과 적용
      document.querySelector('main')?.classList.add('page-slide-in');
    });
  </script>
  
  <main class="main">
  
    <div class="content-container">
        <!-- 왼쪽: 텍스트 입력 영역 -->
        <div class="left-section">
            <!-- 텍스트 입력 칸 -->
            <div class="text-input-container">
                <div class="input-title">생성할 단어 입력</div>
                <div class="input-button-group">
                  <input 
                  type="text" 
                  id="sculpture-input"
                  bind:value={sculptureText}
                  placeholder="Write in English..."
              />
                    <button class="generate-button" on:click={generateSculpture}>
                        {#if isLoading}
                            생성 중...
                        {:else}
                            생성하기
                        {/if}
                    </button>
                </div>
            </div>

            <!-- 추천 이름 목록 -->
            <div class="recommended-names">
                <h3> |추천 이름 목록| </h3>
                <ul>
                    {#each recommendedNames as name}
                        <li 
                            on:click={() => handleRecommendedClick(name)}
                            class="recommended-item"
                        >
                            {name}
                        </li>
                    {/each}
                </ul>
            </div>
        </div>

        <!-- 오른쪽: 조각상 이미지 영역 -->
        <div class="right-section">
            <div class="sculpture-preview">
                {#if isLoading}
                    <div class="loading">이미지를 생성하고 있습니다...</div>
                {:else if sculptureImage}
                    <img src={sculptureImage} alt="생성된 조각상" />
                {:else}
                    <div class="placeholder">
                        생성된 사진이 이 곳에 표시됩니다.
                    </div>
                {/if}
            </div>
            <button class="next-button" on:click={handleNextPage}>
                다음 단계로 
                <span class="arrow">»</span>
            </button>
        </div>
    </div>
  
    <!-- 진행 바 -->
    <div class="progress-bar">
      <div class="progress" style={`width: ${progress}%;`}></div>
      <div class="progress-sections">
        <div class="section1">33%</div>
        <div class="section">배경 꾸미기</div>
        <div class="section">티켓 마무리</div>
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
      padding: 0%;
      margin: 0%;
    }

    .input-title {
      font-size: 36px;
      font-weight: bold;
      color: #ffffff;
      text-align: center;
      letter-spacing: 6px; /* 글자 간격 설정 */
    }
  
    /* 텍스트 입력 칸 스타일 */
    .text-input-container {
      position: relative;
      width: 100%;
      margin-top: 0;
      left: 0;
      border-radius: 8px;
      padding: 10px;

    }
  
    .input-button-group {
      display: flex;
      gap: 10px;
      align-items: flex-start;
      margin-top: 8px;
      padding-left: 100px;
      padding-right: 100px;
    }
  
    .input-button-group input {
    flex: 3;
    padding: 12px; /* 여유 있는 내부 여백 */
    font-size: 18px; /* 텍스트 크기 */
    border: 2px solid #ddd;
    border-radius: 8px;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    font-family: inherit;
    outline: none; /* 포커스 아웃라인 제거 */
    transition: border-color 0.2s ease;
}

.input-button-group input:focus {
    border-color: aquamarine; /* 포커스 시 테두리 색 변경 */
    box-shadow: 0 0 5px aquamarine;
}

.input-button-group input::placeholder {
    color: #aaa; /* 플레이스홀더 색상 */
    font-size: 16px; /* 플레이스홀더 크기 */
    font-weight: 600;
}
  
    .generate-button {
      flex: 1;
      padding: 10px 20px;
      height: 51px;
      background-color: aquamarine;
      color: #000000;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.2s;
    }
  
    .generate-button:hover {
      background-color: rgb(112, 228, 189);
    }
  
    .generate-button:active {
      background-color: rgb(98, 203, 168);
    }
  
    /* 추천 이름 목록 스타일 */
    .recommended-names ul {
      display: grid; /* 그리드 레이아웃 적용 */
      grid-template-columns: repeat(5, 1fr); /* 두 개의 열로 구성 */
      gap: 10px; /* 항목 간격 */
      padding: 0;
      margin: 0;
    }
  
    .recommended-names h3 {
      font-size: 32px;
      font-weight: bold;
      color: #ffffff;
      margin-bottom: 10px;
      letter-spacing: 3px; /* 글자 간격 설정 */
    }
  
    .recommended-names ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
  
    .recommended-names li {
      font-size: 16px;
      font-weight: 600;
      color: #555;
      margin-bottom: 8px;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 8px;
      background-color: #f9f9f9;
      transition: all 0.2s ease;
    }
  
    .recommended-names li:hover {
      background-color: rgb(196, 255, 235);
      cursor: pointer;
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    /* 전체 진행 바 스타일 */
    .progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 50px;
      background-color: #000000; /* 바탕색 */
      z-index: 9999; /* 항상 상단에 표시 */
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 10px; /* 좌우 여백 */
    }
  
    /* 진행된 부분 스타일 */
    .progress {
      position: absolute;
      top: 0;
      left: 0;
      height: 100%;
      background-color: aquamarine; /* 진행 바 색상 */
      z-index: 1;
      transition: width 0.3s ease; /* 부드러운 애니메이션 */
    }
  
    /* 진행 바의 세로 3등분 섹션 */
    .progress-sections {
      display: flex;
      width: 100%;
      height: 100%;
      position: relative;
      z-index: 2; /* 진행 바 위에 표시 */
    }
  
    /* 각 섹션 스타일 */
    .section {
      flex: 1; /* 3등분 */
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 16px;
      font-weight: bold;
      color: #ffffff;
    }
    .section1 {
      flex: 1; /* 3등분 */
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 16px;
      font-weight: bold;
      color: #000000;
    }
  
    /* 마지막 섹션은 구분선 제거 */
    .section:last-child {
      border-right: none;
    }
  
    .content-container {
        display: flex;
        justify-content: space-between;
        width: 80%;
        margin: 50px 12% 0 12%;
        padding-top: 90px;
        padding-bottom: 65px;
        gap: 40px;
    }

    .left-section {
        flex: 4;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 20px;
    }

    .right-section {
        flex: 2;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        gap: 0px;
    }

    .sculpture-preview {
        width: 80%;
        aspect-ratio: 1;
        background-color: #f5f5f5;
        border: 2px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
    }

    .sculpture-preview img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    .sculpture-preview .placeholder {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #666;
        font-size: 20px;
        text-align: center;
    }

    .next-button {
        width: 80%;
        padding: 24px 28px;
        background-color: aquamarine;
        color: #000000;
        border: none;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.2s ease;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;
    }

    .next-button:hover {
        background-color: rgb(94, 193, 160);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(64, 119, 214, 0.3);
    }

    .next-button:active {
        transform: translateY(0);
    }

    .next-button .arrow {
        font-size: 20px;
        transition: transform 0.2s ease;
    }

    .next-button:hover .arrow {
        transform: translateX(4px);
    }

    .loading {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #666;
        font-size: 16px;
        text-align: center;
        background-color: rgba(0, 0, 0, 0.05);
    }

    .footer {
        bottom: 30px;
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
        color: rgb(0, 0, 0);
        font-size: 16px;
        font-weight: 500;
        letter-spacing: 0.5px;
        color: white;
    }
  </style>
  