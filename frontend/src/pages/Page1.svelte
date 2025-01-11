<!-- // src/routes/Home.svelte -->
<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { navigate } from 'svelte-routing';
  let homePage1: any;
  let homePage2: any;
  let homePage3: any;
  let mainPage: any;
  export let name: string;

  function goToPage(pageUrl: string) {
    navigate(pageUrl);
  }

  let debounceTimeout: number;

function handleScroll() {
  clearTimeout(debounceTimeout);
  debounceTimeout = window.setTimeout(() => {
    const sections = [mainPage, homePage1, homePage2, homePage3];
    const scrollY = window.scrollY;
    const closest = sections.reduce((closest, section) => {
      const bounds = section.getBoundingClientRect();
      const distance = Math.abs(bounds.top + scrollY - scrollY);
      const closestDistance = Math.abs(closest.bounds.top + scrollY - scrollY);
      return distance < closestDistance ? { section, bounds } : closest;
    }, { section: sections[0], bounds: sections[0].getBoundingClientRect() });

    if (Math.abs(closest.bounds.top) > 100) { // 임계값 설정
      closest.section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }, 100); // 100ms 지연
}

onMount(() => {
  window.addEventListener('scroll', handleScroll, { passive: true });
});

onDestroy(() => {
  window.removeEventListener('scroll', handleScroll);
  clearTimeout(debounceTimeout);
});
</script>

<div class="main_pages">
  <div class="home_main" bind:this={mainPage}>
    {name}
  </div>

  <div>
  <button class="home_page1" bind:this={homePage1} on:click={() => goToPage('/theme1')}>
    {name}
  </button>
  <button class="home_page2" bind:this={homePage2} on:click={() => goToPage('/theme2')}>
    {name}
  </button>
  <button class="home_page3" bind:this={homePage3} on:click={() => goToPage('/theme3')}>
    {name}
  </button>
</div>
  <div class="remain">

  </div>
</div>


<style>
  .main_pages{
    display: block;
    width: 100%;
    height: 100%;
    white-space: nowrap;
    align-items: center;
    background-color: aquamarine;
    margin: 80px 0 0 0;
    
  }
  .home_main{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 800px;
    background-color:blue;
    margin-top: 40px;
  }
  .home_page1{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 800px;
    background-color:bisque;
    border-radius: 0%;
  }
  .home_page2{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 800px;
    background-color:blueviolet;
    border-radius: 0%;
  }
  .home_page3{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 800px;
    background-color:deeppink;
    border-radius: 0%;
  }

  .remain{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 400px;
    background-color:cadetblue;
    border-radius: 0%;
  }
</style>