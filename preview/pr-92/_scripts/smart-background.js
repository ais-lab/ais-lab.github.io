// sample the center pixel of an <img> and return 'rgb(r,g,b)'
function sampleCenterColor(img) {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    // draw at natural size so pixel coord is accurate
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    ctx.drawImage(img, 0, 0);
    const [r, g, b] = ctx.getImageData(0, 0, 1, 1).data;
    return `rgb(${r}, ${g}, ${b})`;
  }

  // once an image has loaded, pick its center‐pixel color
  function applyBg(img, container) {
    // if (!img.naturalWidth) return;  // not loaded yet
    const color = sampleCenterColor(img);
    
    // create new child <div class="portrait-background"/>
    const bg = document.createElement('div');
    bg.className = 'portrait-background';
    bg.style.backgroundColor = color;

    // add it as img's child
    container.appendChild(bg);
  }

  // wire up on DOM ready
  window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.portrait-image').forEach(container => {
        const url = getComputedStyle(container).backgroundImage
                        .slice(5, -2); // strip url("...")
      
        const img = new Image();
        img.src = url;
        img.onload = () => {
          console.log('background loaded');
          applyBg(img, container);   // now safe to sample on canvas, etc.
        };
        img.onerror = () => {
          console.log('bg failed');
          // fallback logic…
        };
      });
  });