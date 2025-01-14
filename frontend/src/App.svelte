<!-- // src/App.svelte -->
<script lang="ts">
  import { Router, Route } from 'svelte-routing';
  import InitialPage from './pages/InitialPage.svelte';
  import Theme1_0 from './pages/Page1_0.svelte';
  import Theme1_1 from './pages/Page1_1.svelte';
  import Theme1_2 from './pages/Page1_2.svelte';
  import Theme2 from './pages/Page2.svelte';
  import Theme3 from './pages/Page3.svelte';
  import Theme4 from './pages/Page4.svelte';
  import { fade } from 'svelte/transition';
  import { cubicInOut } from 'svelte/easing';

  let initial_main = 'main page';
  let name_page1_0 = 'page 1_0';
  let name_page1_1 = 'page 1_1';
  let name_page1_2 = 'page 1_2';
  let name_page2 = 'page 2';
  let name_page3 = 'page 3';
  let name_page4 = 'page 4';
  let currentRoute = ''; // 현재 라우트 추적

  // 라우트 변경 시 실행되는 함수
    // onMount 또는 초기 렌더링 시 라우트 상태 설정
    $: currentRoute = window.location.pathname; // 현재 URL 경로 추적
</script>

<Router>
  <div class="page-container">
    <main>
      <div class="page-transition" in:fade={{duration: 300, easing: cubicInOut}}>
        <Route path="/" component={InitialPage} name={initial_main} />
        <Route path="/theme1_0" component={Theme1_0} name={name_page1_0} />
        <Route path="/theme1_1" component={Theme1_1} name={name_page1_1} />
        <Route path="/theme1_2" component={Theme1_2} name={name_page1_2} />
        <Route path="/theme2" component={Theme2} name={name_page2} />
        <Route path="/theme3" component={Theme3} name={name_page3} />
        <Route path="/theme4" component={Theme4} name={name_page4} />
      </div>
    </main>
  </div>
</Router>

<style>
  /* 글로벌 스타일을 여기에 추가할 수 있습니다 */
  :global(body) {
    --primary-color: rgba(85, 146, 252, 0.8);
    --primary-color-light: rgba(85, 146, 252, 0.1);
    --primary-color-dark: rgba(85, 146, 252, 0.5);
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
  }

  .page-container {
    position: relative;
    width: 100vw;
    height: 100vh;
    overflow-x: hidden;
  }

  .page-transition {
    position: absolute;
    width: 100%;
    height: 100%;
  }

  :global(.page-slide-out) {
    animation: slideOut 0.5s ease-in-out forwards;
  }

  :global(.page-slide-in) {
    animation: slideIn 0.5s ease-in-out forwards;
  }

  @keyframes slideOut {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(-100%);
      opacity: 0;
    }
  }

  @keyframes slideIn {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
</style>
  