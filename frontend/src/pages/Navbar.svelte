<!-- // src/lib/Navbar.svelte -->
<script lang="ts">
    import { Link } from 'svelte-routing';
  </script>
  
  <div class="nav-link">
    <nav>
      <Link to="/">Home</Link>
      <Link to="/theme1">Theme1</Link>
      <Link to="/theme2">Theme2</Link>
      <Link to="/theme3">Theme3</Link>
    </nav>
  </div>
  
  <style>
    .nav-links {
      /* 필요한 스타일을 추가하세요 */
    }
    
    nav {
      padding: 0;
      margin: 0;
      align-items: center;
      position: absolute;
      justify-content: space-around;
      display: flex;
      top: 0;
      left: 0;
      width: 100%;
      background-color: transparent;
      z-index: 1000;
    }
  
    a {
      color: white; /* 링크 색상 예시 */
      text-decoration: none;
      padding: 1rem;
    }
  
    a:hover {
      background-color: rgba(255, 255, 255, 0.1); /* 호버 효과 예시 */
    }
  </style>
  