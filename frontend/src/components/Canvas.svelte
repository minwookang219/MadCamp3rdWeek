<script lang="ts">
    import { onMount } from 'svelte';

    export let canvasRef: HTMLCanvasElement;

    let isDrawing = false;
    let isEraserMode = false;
    let selectedColor = '#000000';
    let ctx: CanvasRenderingContext2D;
    let lastX = 0;
    let lastY = 0;

    const colors = ['#000000', '#FF0000', '#00FF00', '#0000FF', '#FFFF00'];

    onMount(() => {
        ctx = canvasRef.getContext('2d')!;
        ctx.strokeStyle = selectedColor;
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
        ctx.lineWidth = 5;

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

        if (isEraserMode) {
            ctx.strokeStyle = 'white';
            ctx.lineWidth = 10;
        } else {
            ctx.strokeStyle = selectedColor;
            ctx.lineWidth = 5;
        }

        ctx.stroke();
        [lastX, lastY] = [pos.x, pos.y];
    }

    function stopDrawing() {
        isDrawing = false;
    }

    function getPosition(e: MouseEvent | TouchEvent) {
        const rect = canvasRef.getBoundingClientRect();
        const scaleX = canvasRef.width / rect.width;
        const scaleY = canvasRef.height / rect.height;

        if (e instanceof MouseEvent) {
            return {
                x: (e.clientX - rect.left) * scaleX,
                y: (e.clientY - rect.top) * scaleY,
            };
        } else {
            const touch = e.touches[0];
            return {
                x: (touch.clientX - rect.left) * scaleX,
                y: (touch.clientY - rect.top) * scaleY,
            };
        }
    }

    function clearCanvas() {
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvasRef.width, canvasRef.height);
    }

    function toggleEraserMode() {
        isEraserMode = !isEraserMode;
    }

    function selectColor(color: string) {
        selectedColor = color;
        isEraserMode = false;
    }
</script>

<div class="canvas-wrapper">
    <canvas
        bind:this={canvasRef}
        width="800"
        height="600"
        style="width: 100%; height: 100%;"
        on:mousedown={startDrawing}
        on:mousemove={draw}
        on:mouseup={stopDrawing}
        on:mouseleave={stopDrawing}
        on:touchstart={startDrawing}
        on:touchmove={draw}
        on:touchend={stopDrawing}
    ></canvas>
    <div class="mode-indicator">
        현재 상태: {isEraserMode ? '지우개' : '펜'}
    </div>
    <div class="top-controls">
        <div class="color-palette">
            {#each colors as color}
                <div
                    class="color-circle"
                    style="background-color: {color}; border: {color === selectedColor ? '2px solid #333' : 'none'}"
                    on:click={() => selectColor(color)}
                ></div>
            {/each}
        </div>
    </div>
    <div class="bottom-controls">
        <button class="mode-button" on:click={toggleEraserMode}>
            {isEraserMode ? '펜 모드' : '지우개 모드'}
        </button>
        <button class="clear-button" on:click={clearCanvas}>전체 지우기</button>
    </div>
</div>

<style>
    .canvas-wrapper {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
    }

    canvas {
        width: 100%;
        height: auto;
        touch-action: none;
        cursor: crosshair;
        border: 2px solid #ccc;
        border-radius: 8px;
    }

    .top-controls {
        position: absolute;
        top: 10px;
        right: 10px;
    }

    .bottom-controls {
        position: absolute;
        bottom: 20px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        padding: 0 20px;
    }

    .color-palette {
        display: flex;
        gap: 10px;
    }

    .color-circle {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease;
    }

    .color-circle:hover {
        transform: scale(1.2);
    }

    .mode-button, .clear-button {
        padding: 8px 20px;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 14px;
    }

    .mode-button {
        background: #4A90E2;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
    }

    .mode-button:hover {
        background: #357ABD;
    }

    .clear-button {
        background: #333;
        margin-left: auto;
        margin-right: 10px;
    }

    .clear-button:hover {
        background: #444;
    }

    .mode-indicator {
        position: absolute;
        top: 10px;
        left: 10px;
        padding: 8px 16px;
        background: rgba(0, 0, 0, 0.7);
        color: white;
        border-radius: 4px;
        font-size: 14px;
        pointer-events: none;
        transition: all 0.3s ease;
    }
</style>
