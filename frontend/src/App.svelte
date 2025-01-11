<!-- // src/App.svelte -->
<script lang="ts">
  import { Router, Route } from 'svelte-routing';
  import Navbar from './pages/Navbar.svelte';
  import Home from './pages/Page1.svelte';
  import Theme1 from './pages/Page2.svelte';
  import Theme2 from './pages/Page3.svelte';
  import Theme3 from './pages/Page4.svelte';

  let name = 'lee';
</script>

<Router>
  <Navbar/>
  
  <Route path="/" component={Home} name={name} />
  <Route path="/theme1" component={Theme1} />
  <Route path="/theme2" component={Theme2} />
  <Route path="/theme3" component={Theme3} />
</Router>

<style>
  /* 글로벌 스타일을 여기에 추가할 수 있습니다 */
</style>
