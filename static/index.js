const canvas = document.getElementById("handwritingCanvas");
const ctx = canvas.getContext("2d");
const output = document.getElementById("output");
const image = document.getElementById("image");

let drawing = false;

// Mouse events
canvas.addEventListener("mousedown", () => {
    drawing = true;
    ctx.beginPath();
});

canvas.addEventListener("mouseup", () => {
    drawing = false;
    ctx.closePath();
    updateOutput();
});

canvas.addEventListener("mousemove", (e) => {
    if (!drawing) return;
    draw(e.clientX - canvas.getBoundingClientRect().left, e.clientY - canvas.getBoundingClientRect().top);
});

// Touch events
canvas.addEventListener("touchstart", (e) => {
    e.preventDefault();
    drawing = true;
    ctx.beginPath();
});

canvas.addEventListener("touchend", (e) => {
    e.preventDefault();
    drawing = false;
    ctx.closePath();
    updateOutput();
});

canvas.addEventListener("touchmove", (e) => {
    e.preventDefault();
    if (!drawing) return;
    const touch = e.touches[0];
    draw(touch.clientX - canvas.getBoundingClientRect().left, touch.clientY - canvas.getBoundingClientRect().top);
});

function draw(x, y) {
    ctx.lineWidth = 25;
    ctx.lineCap = "round";
    ctx.strokeStyle = "white";

    ctx.lineTo(x, y);
    ctx.stroke();
}

function updateOutput() {
    const imageData = canvas.toDataURL();
    output.value = imageData;
    image.src = imageData;
  
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    output.value = "";
    image.src = "";
}

