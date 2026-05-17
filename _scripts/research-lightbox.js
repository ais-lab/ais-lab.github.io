{
  const createLightbox = () => {
    const overlay = document.createElement("div");
    overlay.className = "research-lightbox";
    overlay.innerHTML = `
      <div class="research-lightbox-dialog" role="dialog" aria-modal="true">
        <button class="research-lightbox-close" type="button" aria-label="Close">×</button>
        <div class="research-lightbox-media"></div>
      </div>
    `;

    document.body.appendChild(overlay);
    return overlay;
  };

  const openLightbox = (overlay, src, type) => {
    const mediaSlot = overlay.querySelector(".research-lightbox-media");
    mediaSlot.innerHTML = "";

    if (type === "video") {
      const video = document.createElement("video");
      video.src = src;
      video.controls = true;
      video.autoplay = true;
      video.loop = true;
      video.playsInline = true;
      mediaSlot.appendChild(video);
    } else {
      const img = document.createElement("img");
      img.src = src;
      img.alt = "";
      mediaSlot.appendChild(img);
    }

    overlay.classList.add("is-open");
    document.body.style.overflow = "hidden";
  };

  const closeLightbox = (overlay) => {
    overlay.classList.remove("is-open");
    document.body.style.overflow = "";
  };

  const setup = () => {
    const overlay = createLightbox();

    document.addEventListener("click", (event) => {
      const trigger = event.target.closest(".research-lightbox-trigger");
      if (trigger) {
        event.preventDefault();
        openLightbox(overlay, trigger.dataset.lightboxSrc, trigger.dataset.lightboxType);
        return;
      }

      if (event.target.classList.contains("research-lightbox")) {
        closeLightbox(overlay);
      }

      if (event.target.closest(".research-lightbox-close")) {
        closeLightbox(overlay);
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && overlay.classList.contains("is-open")) {
        closeLightbox(overlay);
      }
    });
  };

  window.addEventListener("load", setup);
}
