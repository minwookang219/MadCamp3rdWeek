document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    const clearBtn = document.getElementById('clearBtn');
    const convertBtn = document.getElementById('convertBtn');
    const brushSize = document.getElementById('brushSize');
    const resultImage = document.getElementById('resultImage');
    const loadingSpinner = document.getElementById('loadingSpinner');

    // Canvas 크기 설정
    canvas.width = 512;
    canvas.height = 512;
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // 기본 그리기 설정
    ctx.strokeStyle = 'black';
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.lineWidth = 5;

    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;

    function draw(e) {
        if (!isDrawing) return;
        
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
        
        [lastX, lastY] = [e.offsetX, e.offsetY];
    }

    canvas.addEventListener('mousedown', (e) => {
        isDrawing = true;
        [lastX, lastY] = [e.offsetX, e.offsetY];
    });

    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', () => isDrawing = false);
    canvas.addEventListener('mouseout', () => isDrawing = false);

    clearBtn.addEventListener('click', () => {
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    });

    convertBtn.addEventListener('click', async () => {
        loadingSpinner.style.display = 'block';
        const imageData = canvas.toDataURL('image/png');
        
        try {
            const response = await fetch('/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ image: imageData })
            });
            
            const data = await response.json();
            
            if (data.success) {
                resultImage.src = data.image;
                resultImage.style.display = 'block';
            } else {
                alert('Error converting image: ' + data.error);
            }
        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            loadingSpinner.style.display = 'none';
        }
    });

    brushSize.addEventListener('input', (e) => {
        ctx.lineWidth = e.target.value;
    });
}); 