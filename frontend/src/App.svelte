<!-- // src/App.svelte -->
<script lang="ts">
  import { Router, Route, LOCATION } from 'svelte-routing';
  import Navbar from './pages/Navbar.svelte';
  import InitialPage from './pages/InitialPage.svelte';
  import Theme1 from './pages/Page2.svelte';
  import Theme2 from './pages/Page3.svelte';
  import Theme3 from './pages/Page4.svelte';

  let initial_main = 'main page';
  let name_page1 = 'page 1';
  let name_page2 = 'page 2';
  let name_page3 = 'page 3';

  let currentRoute = ''; // 현재 라우트 추적

  // 라우트 변경 시 실행되는 함수
    // onMount 또는 초기 렌더링 시 라우트 상태 설정
    $: currentRoute = window.location.pathname; // 현재 URL 경로 추적
</script>

<Router>
  {#if currentRoute !== '/'}
    <Navbar />
  {/if}
  <Route path="/" component={InitialPage} name={initial_main} />
  <Route path="/theme1" component={Theme1} name={name_page1} />
  <Route path="/theme2" component={Theme2} name={name_page2} />
  <Route path="/theme3" component={Theme3} name={name_page3} />
</Router>

<style>
  /* 글로벌 스타일을 여기에 추가할 수 있습니다 */
</style>
