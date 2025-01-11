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
      position: fixed;
      justify-content: space-around;
      display: flex;
      top: 0;
      left: 0;
      width: 100%;
      height: 70px;
      background-color: #333;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      z-index: 1000;
    }
  
    nav a {
      color: #FF8C42;
      text-decoration: none;
      padding: 1.5rem;
      font-weight: 500;
      font-size: 18px;
    }
  
    nav a:hover {
      background-color: rgba(255, 140, 66, 0.1);
      color: #ffa76a;
    }
  </style>
  