---
layout: default
title: Laboratory Interviews
author: webstaff
---

{% case site.lang %}
{% when 'jp' %}
# 先輩インタビュー
{% when 'en' %}
# Senior Student Interviews
{% endcase %}

<style>
/* Background style similar to lab life page */
.interview-page {
  position: relative;
}

.interview-page .parallax-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
}

.interview-page .particle {
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

/* Question styles */
.interview-page .question-container {
  max-width: 900px;
  margin: 40px auto;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  padding: 25px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.interview-page .question-title {
  font-size: 22px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 2px solid #3498db;
  text-align: center;
}

/* Chat bubbles */
.interview-page .chat-container {
  margin: 20px 0;
}

.interview-page .chat-item {
  display: flex;
  margin-bottom: 25px;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease;
}

.interview-page .chat-item.left {
  flex-direction: row;
}

.interview-page .chat-item.right {
  flex-direction: row-reverse;
}

.interview-page .chat-item.appear {
  opacity: 1;
  transform: translateY(0);
}

.interview-page .avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: #3498db;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  font-weight: bold;
  flex-shrink: 0;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.interview-page .left .avatar {
  margin-right: 15px;
}

.interview-page .right .avatar {
  margin-left: 15px;
  background: #9b59b6;
}

.interview-page .bubble {
  position: relative;
  background: white;
  border-radius: 15px;
  padding: 15px 20px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  flex-grow: 1;
  max-width: 80%;
  text-align: left;
}

.interview-page .bubble::before {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  top: 15px;
}

.interview-page .left .bubble::before {
  border-right: 10px solid white;
  left: -10px;
}

.interview-page .right .bubble::before {
  border-left: 10px solid white;
  right: -10px;
}

.interview-page .name {
  font-weight: 600;
  margin-bottom: 5px;
  color: #2c3e50;
}

.interview-page .left .name {
  text-align: left;
}

.interview-page .right .name {
  text-align: right;
}

.interview-page .message {
  line-height: 1.6;
  color: #555;
  text-align: left;
}

/* Responsive design */
@media screen and (max-width: 768px) {
  .interview-page .question-container {
    padding: 15px;
    margin: 20px 10px;
  }
  
  .interview-page .bubble {
    max-width: 75%;
  }
}
</style>

<div class="interview-page">
  <!-- Parallax background -->
  <div class="parallax-bg" id="interview-parallax-bg"></div>
  
  {% include interviews.html %}
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Generate particles for parallax background
    const parallaxBg = document.getElementById('interview-parallax-bg');
    
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
    
    // Add appear class to all chat items with delay
    const chatItems = document.querySelectorAll('.chat-item');
    chatItems.forEach((item, index) => {
      setTimeout(() => {
        item.classList.add('appear');
      }, 150 * index);
    });
  });
</script>