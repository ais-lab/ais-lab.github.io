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
  padding: 0 15px;
  box-sizing: border-box;
  max-width: 400px;
  margin: 0 auto;
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
  min-height: 550px;
}

.room-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.room-image-container {
  width: 100%;
  padding-top: 75%; /* 4:3のアスペクト比を維持 */
  position: relative;
  overflow: hidden;
}

.room-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.room-content {
  padding: 30px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.room-title {
  font-size: 1.6rem;
  margin-bottom: 15px;
  color: var(--primary);
}

.room-description {
  margin-bottom: 25px;
  flex-grow: 1;
  color: var(--text);
  line-height: 1.6;
  font-size: 1.05rem;
}

.room-location {
  margin-bottom: 20px;
  color: var(--text);
  font-size: 1rem;
  line-height: 1.4;
}

.room-button {
  align-self: flex-start;
  padding: 10px 20px;
  background: var(--primary);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  margin-top: auto;
  font-size: 1rem;
}

.room-button:hover {
  background: var(--primary);
  opacity: 0.8;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.room-button:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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

@media (max-width: 768px) {
  .room-slider {
    width: 100%;
    flex-wrap: wrap;
  }
  
  .room-slide {
    width: 100%;
    margin-bottom: 20px;
    max-width: 100%;
  }
  
  .room-card {
    min-height: 500px;
  }
  
  .room-content {
    padding: 25px;
  }
  
  .room-title {
    font-size: 1.4rem;
  }
  
  .room-description {
    font-size: 1rem;
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
        <div class="room-image-container">
          <img src="{{ site.baseurl_root }}/images/{{ room.image }}" alt="{{ room.title[site.lang] }}" class="room-image">
        </div>
        <div class="room-content">
          <h3 class="room-title">{{ room.title[site.lang] }}</h3>
          <p class="room-description">{{ room.description[site.lang] }}</p>
          <p class="room-location"><strong>{% if site.lang == 'jp' %}場所：{% else %}Location:{% endif %}</strong> {{ room.location[site.lang] }}</p>
          <a href="{{ site.baseurl_root }}/{{ site.lang }}/{{ room.link }}" class="room-button">
            {% if site.lang == 'jp' %}詳細を見る{% else %}Learn More{% endif %}
          </a>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
  
  <div class="carousel-nav">
    {% for room in site.data.rooms.rooms %}
    <div class="carousel-dot {% if forloop.first %}active{% endif %}" data-slide="{{ forloop.index0 }}"></div>
    {% endfor %}
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Force repaint on page load to ensure carousel is displayed correctly
  setTimeout(function() {
    document.querySelector('.room-slider').style.display = 'none';
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
  
  function goToSlide(n) {
    currentSlide = (n + slideCount) % slideCount;
    slider.style.transform = `translateX(-${currentSlide * 25}%)`;
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentSlide);
    });
  }
  
  goToSlide(0);
  
  prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
  nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));
  
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => goToSlide(i));
  });
  
  let isSwiping = false;
  let startX = 0;
  let currentX = 0;

  slider.addEventListener('touchstart', (e) => {
    isSwiping = true;
    startX = e.touches[0].clientX;
    currentX = startX;
  }, { passive: true });

  slider.addEventListener('touchmove', (e) => {
    if (!isSwiping) return;
    currentX = e.touches[0].clientX;
    const diff = currentX - startX;
    const maxDiff = slider.offsetWidth * 0.3;
    const limitedDiff = Math.max(Math.min(diff, maxDiff), -maxDiff);
    slider.style.transform = `translateX(calc(-${currentSlide * 25}% + ${limitedDiff}px))`;
  }, { passive: true });

  slider.addEventListener('touchend', () => {
    if (!isSwiping) return;
    isSwiping = false;
    const diff = currentX - startX;
    const threshold = slider.offsetWidth * 0.1;
    if (Math.abs(diff) > threshold) {
      if (diff > 0) {
        goToSlide(currentSlide - 1);
      } else {
        goToSlide(currentSlide + 1);
      }
    } else {
      goToSlide(currentSlide);
    }
  }, { passive: true });

  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      goToSlide(currentSlide);
    }, 250);
  });
});
</script>

