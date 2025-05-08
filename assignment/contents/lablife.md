---
layout: default
title: Lab life
author: webstaff
---

{% case site.lang %}
{% when 'jp' %}
# 研究室配属後の生活
{% when 'en' %}
# Life after assignment to a laboratory
{% endcase %}

<style>
/* Timeline specific styles */
.lablife-page .parallax-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
}

.lablife-page .particle {
  position: absolute;
  border-radius: 50%;
  background: rgba(52, 152, 219, 0.1);
  animation: float 15s infinite linear !important;
}

@keyframes float {
  0% {
    transform: translateY(0) rotate(0deg);
  }
  100% {
    transform: translateY(-1000px) rotate(720deg);
  }
}

.lablife-page .timeline-container {
  max-width: 1200px;
  margin: 30px auto;
  position: relative;
  padding: 20px 0;
}

/* 中央線のスタイル修正 */
.lablife-page .center-line {
  position: absolute;
  height: 100%;
  width: 6px;
  background: linear-gradient(180deg, #3498db, #9b59b6, #e74c3c);
  left: 50%;
  transform: translateX(-50%);
  top: 0;
  z-index: 0; /* 最背面 */
  border-radius: 6px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  pointer-events: none; /* クリックイベントを通過させる */
}

/* 矢印のスタイル修正 */
.lablife-page .center-line::before {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 20px solid #e74c3c;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  animation: arrowPulse 2s infinite !important;
  z-index: 1; /* 最背面 */
  pointer-events: none; /* クリックイベントを通過させる */
}

@keyframes arrowPulse {
  0% {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
  }
  50% {
    transform: translateX(-50%) translateY(10px);
    opacity: 0.7;
  }
  100% {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
  }
}

.lablife-page .timeline-item {
  display: flex;
  justify-content: center;
  position: relative;
  margin-bottom: 80px;
  opacity: 0 !important;
  transform: translateY(50px) !important;
  transition: all 0.8s ease !important;
  padding-top: 50px; /* 日付用の上部スペース */
}

.lablife-page .timeline-item.appear {
  opacity: 1 !important;
  transform: translateY(0) !important;
}

.lablife-page .timeline-item:last-child {
  margin-bottom: 0;
}

/* 日付スタイルの修正 */
.lablife-page .timeline-date {
  position: absolute;
  width: 120px;
  height: 40px;
  background: #2c3e50;
  color: #fff;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 600;
  z-index: 10; /* 最前面 */
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.lablife-page .timeline-content {
  width: 44%;
  padding: 30px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 2; /* 中間層 */
  position: relative; /* z-indexを有効にするため */
}

.lablife-page .timeline-content:hover {
  transform: translateY(-5px) !important;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.lablife-page .timeline-content h3 {
  margin-bottom: 15px;
  color: #2c3e50;
  font-size: 20px;
}

.lablife-page .timeline-content p {
  line-height: 1.6;
  color: #555;
  margin-bottom: 15px;
}

.lablife-page .timeline-content.left {
  margin-right: auto;
  margin-left: 2%;
}

.lablife-page .timeline-content.right {
  margin-left: auto;
  margin-right: 2%;
}

/* ドットスタイルの修正 */
.lablife-page .timeline-dot {
  position: absolute;
  width: 20px;
  height: 20px;
  background: #fff;
  border: 4px solid #3498db;
  border-radius: 50%;
  left: 50%;
  top: 60px; /* 日付の下に配置 */
  transform: translateX(-50%);
  z-index: 10; /* 最前面 */
  box-shadow: 0 0 0 4px rgba(52, 152, 219, 0.3);
}

.lablife-page .timeline-detail {
  display: none;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px dashed #ddd;
  animation: fadeIn 0.5s ease !important;
  position: relative; /* z-indexの継承を防ぐ */
  z-index: 2; /* 親要素と同じz-index */
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.lablife-page .timeline-detail img {
  width: 100%;
  max-height: 300px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  margin-bottom: 15px;
}

.lablife-page .btn-more {
  display: inline-block;
  padding: 8px 15px;
  background: #3498db;
  color: #fff !important;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative; /* z-indexが効くように */
  z-index: 3; /* コンテンツ内で前面に */
}

.lablife-page .btn-more:hover {
  background: #2980b9;
  transform: scale(1.05) !important;
}

/* Responsive design */
@media screen and (max-width: 768px) {
  .lablife-page .center-line {
    left: 30px;
  }

  .lablife-page .timeline-date {
    left: 30px;
    width: 90px;
    font-size: 12px;
  }

  .lablife-page .timeline-dot {
    left: 30px;
  }

  .lablife-page .timeline-content {
    width: 80%;
    margin-left: 60px !important;
    margin-right: 0 !important;
  }

  .lablife-page .timeline-item {
    justify-content: flex-start;
  }
}
</style>

<div class="lablife-page">
  <!-- Parallax background -->
  <div class="parallax-bg" id="parallax-bg"></div>

  {% include lablife.html data="events" %}
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Generate particles for parallax background
    const parallaxBg = document.getElementById('parallax-bg');
    
    if (parallaxBg) {
      // Create particles
      for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        
        // Set random size, position, and opacity
        const size = Math.random() * 40 + 10;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.opacity = Math.random() * 0.5 + 0.1;
        
        // Set random animation delay and duration
        particle.style.animationDelay = `${Math.random() * 15}s`;
        particle.style.animationDuration = `${Math.random() * 30 + 15}s`;
        
        parallaxBg.appendChild(particle);
      }
    }
    
    // Add appear class to all timeline items immediately (bypass problematic animation)
    const timelineItems = document.querySelectorAll('.timeline-item');
    setTimeout(function() {
      timelineItems.forEach(item => {
        item.classList.add('appear');
      });
    }, 100);
    
    // Click event for detail buttons
    const moreButtons = document.querySelectorAll('.btn-more');
    
    moreButtons.forEach(button => {
      button.addEventListener('click', function() {
        const detail = this.nextElementSibling;
        
        if (detail.style.display === 'block') {
          detail.style.display = 'none';
          this.textContent = '{% if site.lang == "jp" %}詳細を見る{% else %}More details{% endif %}';
        } else {
          detail.style.display = 'block';
          this.textContent = '{% if site.lang == "jp" %}閉じる{% else %}Close{% endif %}';
        }
      });
    });
  });
</script>