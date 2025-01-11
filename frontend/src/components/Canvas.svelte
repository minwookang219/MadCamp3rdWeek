<script lang="ts">
    import { onMount } from 'svelte';
    
    export let canvasRef: HTMLCanvasElement;
    
    let isDrawing = false;
    let ctx: CanvasRenderingContext2D;
    let lastX = 0;
    let lastY = 0;
    
    onMount(() => {
        ctx = canvasRef.getContext('2d')!;
        ctx.strokeStyle = '#000000';
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
        ctx.lineWidth = 5;
        
        // 캔버스 배경을 흰색으로 설정
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvasRef.width, canvasRef.height);
    });

    function startDrawing(e: MouseEvent | TouchEvent) {
        isDrawing = true;
        const pos = getPosition(e);
        [lastX, lastY] = [pos.x, pos.y];
    }

    function draw(e: MouseEvent | TouchEvent) {
        if (!isDrawing) return;
        
        const pos = getPosition(e);
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(pos.x, pos.y);
        ctx.stroke();
        [lastX, lastY] = [pos.x, pos.y];
    }

    function stopDrawing() {
        isDrawing = false;
    }

    function getPosition(e: MouseEvent | TouchEvent) {
        const rect = canvasRef.getBoundingClientRect();
        if (e instanceof MouseEvent) {
            return {
                x: e.clientX - rect.left,
                y: e.clientY - rect.top
            };
        } else {
            const touch = e.touches[0];
            return {
                x: touch.clientX - rect.left,
                y: touch.clientY - rect.top
            };
        }
    }

    function clearCanvas() {
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvasRef.width, canvasRef.height);
    }
</script>

<div class="canvas-wrapper">
    <canvas
        bind:this={canvasRef}
        width="800"
        height="600"
        on:mousedown={startDrawing}
        on:mousemove={draw}
        on:mouseup={stopDrawing}
        on:mouseleave={stopDrawing}
        on:touchstart={startDrawing}
        on:touchmove={draw}
        on:touchend={stopDrawing}
    ></canvas>
    <div class="controls">
        <button on:click={clearCanvas}>지우기</button>
    </div>
</div>

<style>
    .canvas-wrapper {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    canvas {
        width: 100%;
        height: auto;
        touch-action: none;
        cursor: crosshair;
    }

    .controls {
        margin-top: 10px;
        padding: 10px;
    }

    button {
        padding: 8px 20px;
        background: #333;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    button:hover {
        background: #444;
    }
</style> 