<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { navigate } from 'svelte-routing';

  let homePage1: any;
  let homePage2: any;
  let homePage3: any;
  let mainPage: any;
  export let name: string;

  let debounceTimeout: number;

  function goToPage(pageUrl: string) {
    navigate(pageUrl);
  }

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

      if (Math.abs(closest.bounds.top) > 100) {
        closest.section.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 100);
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
    <div class="logo-container">
      <div class="logo-grid">
        <div class="logo-item">몰</div>
        <div class="logo-item">입</div>
        <div class="logo-item">전</div>
        <div class="logo-item">시</div>
      </div>
    </div>
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

  <div class="remain"></div>
</div>

<style>
.main_pages {
  display: block;
  width: 100%;
  height: 100%;
  white-space: nowrap;
  align-items: center;
  margin: 80px 0 0 0;
}

.home_main, .home_page1, .home_page2, .home_page3, .remain {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 800px;
}

.home_main {
  background-color: blue;
  margin-top: 40px;
}

.home_page1 {
  background-color: bisque;
}

.home_page2 {
  background-color: blueviolet;
}

.home_page3 {
  background-color: deeppink;
}

.remain {
  background-color: cadetblue;
  height: 400px;
}

.logo-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 300px;
  height: 300px;
  background: white;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.logo-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  width: 100%;
  height: 100%;
}

.logo-item {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #111111;
  color: white;
  font-size: 48px;
  font-weight: bold;
  border-radius: 10px;
  transition: transform 0.3s ease;
}

.logo-item:hover {
  transform: scale(1.05);
}

.home_main {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 800px;
  background-color: #111111;
}
</style>