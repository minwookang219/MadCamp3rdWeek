<script lang="ts">
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    // 진행률 (0~100 사이의 값)
    let progress = 33.33333333; // 예: 현재 진행률 50%
    let sculptureText = ''; // 사용자가 입력한 텍스트를 저장
    let sculptureImage = ''; // 서버에서 받아올 이미지 URL을 저장할 변수
    let isLoading = false;
  
    // 추천 이름 목록
    let recommendedNames: string[] = [
      '슈퍼마리오의 쿠파',
      '평화의 상징',
      '아이폰15',
      '뚝배기 불고기',
      '자유의 여신상'
    ];
  
    const HUGGING_FACE_API_KEY = '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';
    console.log('Full env:', import.meta.env);
  
    async function generateSculpture() {
      if (!sculptureText.trim()) return;
      
      isLoading = true;
      try {
        console.log('API Key:', HUGGING_FACE_API_KEY);
        console.log('Sending request with prompt:', sculptureText);
        
        let retries = 0;
        const maxRetries = 3;
        
        while (retries < maxRetries) {
          const response = await fetch('https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-1', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${HUGGING_FACE_API_KEY}`,
            },
            body: JSON.stringify({
              inputs: `A simple marble sculpture of ${sculptureText}, white marble texture, simple lighting`,
            }),
          });
    
          if (!response.ok) {
            const errorData = await response.text();
            console.error('Response not OK:', response.status, errorData);
            
            // 모델 로딩 중인 경우
            if (response.status === 503) {
              const errorJson = JSON.parse(errorData);
              const waitTime = Math.ceil(errorJson.estimated_time || 20);
              console.log(`Waiting ${waitTime} seconds for model to load...`);
              await new Promise(resolve => setTimeout(resolve, waitTime * 1000));
              retries++;
              continue;
            }
            
            throw new Error('이미지 생성에 실패했습니다');
          }
    
          const blob = await response.blob();
          sculptureImage = URL.createObjectURL(blob);
          break;
        }
        
        if (retries >= maxRetries) {
          throw new Error('모델 로딩 시간이 너무 오래 걸립니다. 나중에 다시 시도해주세요.');
        }
      } catch (error: any) {
        console.error('Error details:', {
          message: error.message,
          stack: error.stack,
          error
        });
        alert('이미지 생성 중 오류가 발생했습니다');
      } finally {
        isLoading = false;
      }
    }
  
    function handleRecommendedClick(name: string) {
      sculptureText = name;
      generateSculpture();
    }
  
    async function handleNextPage() {
      navigate('/theme1_2');
    }
  </script>
  
  <main>
    <!-- 제목 -->
    <div class="title-container">
      <div class="title">조각상 만들기</div>
    </div>
  
    <div class="content-container">
        <!-- 왼쪽: 텍스트 입력 영역 -->
        <div class="left-section">
            <!-- 텍스트 입력 칸 -->
            <div class="text-input-container">
                <label for="sculpture-input">조각상 이름을 적어보세요</label>
                <div class="input-button-group">
                    <textarea 
                        id="sculpture-input"
                        bind:value={sculptureText}
                        placeholder="여기에 입력하세요..."
                    ></textarea>
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
                <h3>추천 이름 목록</h3>
                <ul>
                    {#each recommendedNames as name}
                        <li on:click={() => handleRecommendedClick(name)}>{name}</li>
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
                        조각상이 이곳에 표시됩니다
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
  </main>
  
  <style>
    /* 제목을 감싸는 컨테이너 */
    .title-container {
      position: relative;
      margin-top: 98px;
      width: 68%; /* 전체 너비에서 좌우 여백을 뺀 너비 */
      margin-left: 16%; /* 왼쪽 여백 */
      margin-right: 16%; /* 오른쪽 여백 */
      background-color: rgba(128, 128, 128, 0.8);
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
      background-color: #5592fc;
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
        margin: 64px 16% 0 16%;
        gap: 40px;
    }

    .left-section {
        flex: 1;
    }

    .right-section {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
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
  </style>
  