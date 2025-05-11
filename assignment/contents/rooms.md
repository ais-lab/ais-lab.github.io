---
title: Research Rooms
author: webstaff
lang: jp
tags:
    - ResearchLab
    - Facilities
    - AIS Lab
---

{% case site.lang %}
{% when 'en' %}
# Research Facilities

AIS Lab. consists of four rooms, each specializing in different aspects of research. Each room is equipped with facilities suitable for that particular room, allowing comfortable research to be conducted there.
{% when 'jp' %}
# 研究施設

AIS Lab. は、研究の様々な側面に特化した4つの部屋で構成されています。それぞれの部屋には、部屋に適した設備が整っており、その部屋で快適に研究ができます。
{% endcase %}

<style>
/* Room carousel styling */
.room-carousel {
  position: relative;
  width: 100%;
  max-width: 1400px; /* カラセルの最大幅を広げる */
  margin: 40px auto;
  overflow: hidden;
  touch-action: pan-x;
}

.room-slider {
  display: flex;
  transition: transform 0.5s ease;
  width: 400%;
}

.room-slide {
  width: 25%;
  flex-shrink: 0;
  padding: 0 20px; /* パディングを少し増やす */
  box-sizing: border-box;
}

.room-card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  height: 100%;
  display: flex;
  flex-direction: column;
  max-width: 320px; /* カードの最大幅を大きく */
  margin: 0 auto;
}

.room-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.room-image {
  width: 100%;
  padding-top: 75%;
  position: relative;
}

.room-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Ensure better display on mobile */
@media (max-width: 480px) {
  .room-image {
    height: 150px;
  }
  
  .room-title {
    font-size: 1.2rem;
  }
  
  .room-description {
    font-size: 0.9rem;
  }
  
  .room-button {
    font-size: 0.9rem;
    padding: 6px 12px;
  }
}

.room-content {
  padding: 20px; /* パディングを少し増やす */
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.room-title {
  font-size: 1.3rem; /* タイトルのフォントサイズを少し大きく */
  margin-bottom: 10px;
  color: var(--primary);
}

.room-location {
  font-size: 1rem; /* 場所のフォントサイズを少し大きく */
  color: var(--text);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.room-location i {
  color: var(--primary);
}

.room-description {
  margin-bottom: 20px;
  flex-grow: 1;
  color: var(--text);
  font-size: 1rem; /* 説明文のフォントサイズを少し大きく */
  line-height: 1.5; /* 行間を追加 */
}

.room-button {
  align-self: flex-start;
  padding: 8px 16px; /* ボタンのパディングを少し大きく */
  background: var(--primary);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease;
  text-decoration: none;
  margin-top: auto;
  font-size: 1rem; /* ボタンのフォントサイズを少し大きく */
}

.room-button:hover {
  background: var(--text);
}

.carousel-nav {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.carousel-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--light-gray);
  margin: 0 5px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.carousel-dot.active {
  background: var(--primary);
}

.carousel-arrows {
  position: absolute;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  transform: translateY(-50%);
  z-index: 1;
}

.carousel-arrow {
  background: rgba(255,255,255,0.8);
  color: var(--primary);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1.2rem;
  margin: 0 10px;
  border: none;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.carousel-arrow:hover {
  background: var(--primary);
  color: white;
}

/* For tablet and smaller screens */
@media (max-width: 768px) {
  .room-slider {
    width: 100%;
    flex-wrap: wrap;
  }
  
  .room-slide {
    width: 100%;
    margin-bottom: 20px;
  }
  
  .carousel-arrows, .carousel-nav {
    display: none;
  }
}
</style>

<div class="room-carousel">
  <div class="carousel-arrows">
    <button class="carousel-arrow prev">
      <i class="fa-solid fa-chevron-left"></i>
    </button>
    <button class="carousel-arrow next">
      <i class="fa-solid fa-chevron-right"></i>
    </button>
  </div>
  
  <div class="room-slider">
    {% for room in site.data.rooms.rooms %}
    <div class="room-slide">
      <div class="room-card" onclick="window.location.href='{{ site.baseurl_root }}/{{ site.lang }}/{{ room.link }}'">
        <div class="room-image">
          <img src="{{ site.baseurl_root }}/images/{{ room.image }}" alt="{{ room.title[site.lang] }}">
        </div>
        <div class="room-content">
          <h3 class="room-title">{{ room.title[site.lang] }}</h3>
          <div class="room-location">
            <i class="fas fa-map-marker-alt"></i>
            {{ room.location[site.lang] }}
          </div>
          <p class="room-description">
            {{ room.description[site.lang] }}
          </p>
          <a href="{{ site.baseurl_root }}/{{ site.lang }}/{{ room.link }}" class="room-button">
            {% if site.lang == 'jp' %}詳細を見る{% else %}Learn More{% endif %}
          </a>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
  
  <div class="carousel-nav">
    <div class="carousel-dot active" data-slide="0"></div>
    <div class="carousel-dot" data-slide="1"></div>
    <div class="carousel-dot" data-slide="2"></div>
    <div class="carousel-dot" data-slide="3"></div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Force repaint on page load to ensure carousel is displayed correctly
  setTimeout(function() {
    document.querySelector('.room-slider').style.display = 'none';
    // Force reflow
    void document.querySelector('.room-slider').offsetHeight;
    document.querySelector('.room-slider').style.display = 'flex';
  }, 100);

  const slider = document.querySelector('.room-slider');
  const slides = document.querySelectorAll('.room-slide');
  const dots = document.querySelectorAll('.carousel-dot');
  const prevBtn = document.querySelector('.carousel-arrow.prev');
  const nextBtn = document.querySelector('.carousel-arrow.next');
  let currentSlide = 0;
  const slideCount = slides.length;
  
  // Function to update slider
  function goToSlide(n) {
    currentSlide = (n + slideCount) % slideCount;
    
    // Always apply transform
    slider.style.transform = `translateX(-${currentSlide * 25}%)`;
    
    // Update active dot
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentSlide);
    });
  }
  
  // Initialize slider
  goToSlide(0);
  
  // Event listeners
  prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
  nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));
  
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => goToSlide(i));
  });
  
  // Add touch swiping functionality for mobile
  let touchStartX = 0;
  let touchEndX = 0;
  
  slider.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });
  
  slider.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, { passive: true });
  
  function handleSwipe() {
    const swipeThreshold = 50; // Minimum swipe distance
    if (touchEndX < touchStartX - swipeThreshold) {
      // Swipe left - next slide
      goToSlide(currentSlide + 1);
    } else if (touchEndX > touchStartX + swipeThreshold) {
      // Swipe right - previous slide
      goToSlide(currentSlide - 1);
    }
  }
  
  // Always maintain slide position on resize
  window.addEventListener('resize', () => {
    goToSlide(currentSlide);
  });
});
</script>
