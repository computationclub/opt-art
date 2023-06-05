const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");
const image = document.getElementById("source");
const sourceCanvas = document.getElementById("source-canvas");
const sourceContext = sourceCanvas.getContext("2d");
const width = canvas.width;
const height = canvas.height;
const tileSize = 10;

sourceContext.drawImage(image, 0, 0, width, height);

const main = () => {
  let t = 0;

  for (let y = 0; y < height; y += tileSize) {
    for (let x = 0; x < width; x += tileSize) {
      const tileData = sourceContext.getImageData(x, y, tileSize, tileSize).data;

      let sum = 0;
      for (let i = 0; i < tileData.length; i += 4) {
        sum += tileData[i];
        sum += tileData[i + 1];
        sum += tileData[i + 2];
      }

      const mean = sum / (tileData.length / 4 * 3);
      const t = 1 - (mean / 255);

      drawTileA(x, y, clampT(t));
    }
  }
};

const clampT = (t) => (
  Math.max(0.25, Math.min(0.75, t))
);

const drawTileA = (x, y, t) => {
  context.beginPath();
  context.moveTo(x, y);
  context.lineTo(x, y + tileSize);
  context.lineTo(x + tileSize, y + tileSize);
  context.lineTo(x + tileSize * t, y + (1 - t) * tileSize);
  context.lineTo(x, y);
  context.closePath();
  context.fill();
};

main();
