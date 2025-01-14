<script lang="ts">
  import { onMount } from 'svelte';
  import { navigate } from 'svelte-routing';
  import logoImage from '../assets/logo_images.png';
  let progress = 33.33333333; // 두 번째 단계이므로 진행률 수정
  let sculptureImage = ''; // 2D 이미지
  let sculpture3DImage = ''; // 3D 이미지
  let isLoading = false;

  const API_URL = 'http://localhost:8000';

  async function convert2Dto3D() {
    isLoading = true;
    try {
      const response = await fetch(`${API_URL}/convert-to-3d`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: sculptureImage  // 2D 이미지 전송
        }),
      });

      if (!response.ok) {
        throw new Error('3D 변환에 실패했습니다');
      }

      const data = await response.json();
      sculpture3DImage = `data:image/png;base64,${data.image}`;
    } catch (error: any) {
      console.error('Error details:', error);
      alert('3D 변환 중 오류가 발생했습니다');
    } finally {
      isLoading = false;
    }
  }

  // 이전 페이지에서 생성된 이미지 로드
  onMount(() => {
    // 여기서 이전 페이지의 이미지를 가져오는 로직 구현
    // 예: localStorage나 상태 관리 라이브러리 사용
  });

  async function handleNextPage() {
    navigate('/theme2');
  }
</script>

<main>
  <!-- 제목 -->
  <div class="title-container">
    <div class="title">3D 조각상 만들기</div>
  </div>

  <div class="content-container">
      <!-- 왼쪽: 2D 이미지 -->
      <div class="left-section">
          <h3>현재 2D 이미지</h3>
          <div class="image-preview">
              <img src={sculptureImage} alt="2D 조각상" />
          </div>
          <button class="convert-button" on:click={convert2Dto3D}>
              3D로 변환하기
          </button>
      </div>

      <!-- 오른쪽: 3D 이미지 -->
      <div class="right-section">
          <h3>3D 변환 결과</h3>
          <div class="image-preview">
               {#if isLoading}
                   <div class="loading">3D로 변환하고 있습니다...</div>
               {:else if sculpture3DImage}
                   <img src={sculpture3DImage} alt="3D 조각상" />
               {:else}
                   <div class="placeholder">
                       3D 이미지가 이곳에 표시됩니다
                   </div>
               {/if}
           </div>
           <button class="next-button" on:click={handleNextPage}>
               다음 단계로
               <span class="arrow">→</span>
           </button>
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
  /* 제목을 감싸는 컨테이너 */
  .title-container {
    position: relative;
    margin-top: 70px;
    width: 68%;
    margin-left: 16%;
    margin-right: 16%;
    background-color: var(--primary-color);
    padding: 20px;
    border: 2px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(5, 4, 4, 0.1);
    z-index: 1000;
  }

  /* 제목 텍스트 스타일 */
  .title {
    font-size: 30px;
    font-weight: bold;
    color: #333;
    text-align: center;
  }

  /* 텍스트 입력 칸 스타일 */
  .text-input-container {
    position: relative;
    width: 100%;
    margin-top: 0;
    left: 0;
  }

  .input-button-group {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-top: 8px;
  }

  .text-input-container textarea {
    flex: 1;
    min-height: 50px;
    padding: 10px;
    font-size: 16px;
    border: 2px solid #ddd;
    border-radius: 8px;
    resize: none;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    font-family: inherit;
  }

  .generate-button {
    padding: 10px 20px;
    height: 50px;
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .generate-button:hover {
    background-color: #4077d6;
  }

  .generate-button:active {
    background-color: #3567c0;
  }

  /* 추천 이름 목록 스타일 */
  .recommended-names {
    width: 80%;
    left: 10%;
    position: relative;
    margin-top: 80px;
  }

  .recommended-names h3 {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
  }

  .recommended-names ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .recommended-names li {
    font-size: 16px;
    color: #555;
    margin-bottom: 8px;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  .recommended-names li:hover {
    background-color: #e6f7ff; /* 마우스 오버 시 색상 */
    cursor: pointer;
  }

  /* 전체 진행 바 스타일 */
  .progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 50px;
    background-color: #f0f0f0; /* 바탕색 */
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
    background-color: #aff7b2; /* 진행 바 색상 */
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
    color: #000;
  }

  /* 마지막 섹션은 구분선 제거 */
  .section:last-child {
    border-right: none;
  }

  .content-container {
      display: flex;
      justify-content: space-between;
      width: 68%;
      margin: 30px 16% 0 16%;
      gap: 40px;
      flex: 1;
  }

  .left-section {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
  }

  .right-section {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
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
      font-size: 16px;
      text-align: center;
      padding: 20px;
  }

  .next-button {
      width: 80%;
      padding: 16px 28px;
      background-color: #4077d6;
      color: white;
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
      background-color: #3567c0;
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

  h3 {
    font-size: 20px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
    text-align: center;
  }

  .image-preview {
    width: 100%;
    aspect-ratio: 1.2;
    background-color: #f5f5f5;
    border: 2px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    max-height: calc(70vh - 200px);
  }

  .image-preview img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .convert-button {
    width: 80%;
    padding: 16px 28px;
    background-color: #5592fc;
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .convert-button:hover {
    background-color: #4077d6;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(64, 119, 214, 0.3);
  }

  main {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      padding: 60px 0;
      box-sizing: border-box;
  }

  
  .footer {
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
