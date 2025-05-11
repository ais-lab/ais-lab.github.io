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

<div class="rooms-tabs" role="tablist" aria-label="{% if site.lang == 'jp' %}研究室の部屋{% else %}Research Rooms{% endif %}">
  <div class="tabs-nav">
    {% for room in site.data.rooms.rooms %}
    <button class="tab-button {% if forloop.first %}active{% endif %}" 
            id="tab-btn-{{ forloop.index0 }}" 
            data-tab="{{ forloop.index0 }}"
            role="tab"
            aria-selected="{% if forloop.first %}true{% else %}false{% endif %}"
            aria-controls="panel-{{ forloop.index0 }}">
      {{ room.title[site.lang] }}
    </button>
    {% endfor %}
  </div>
  
  <div class="tabs-content">
    {% for room in site.data.rooms.rooms %}
    <div class="tab-panel {% if forloop.first %}active{% endif %}" 
         id="panel-{{ forloop.index0 }}" 
         data-tab="{{ forloop.index0 }}"
         role="tabpanel"
         aria-labelledby="tab-btn-{{ forloop.index0 }}"
         {% unless forloop.first %}hidden{% endunless %}>
      <div class="room-card">
        <div class="room-image">
          <img src="{{ site.baseurl_root }}/images/{{ room.image }}" alt="{{ room.title[site.lang] }}">
        </div>
        <div class="room-content">
          <h3 class="room-title">{{ room.title[site.lang] }}</h3>
          <div class="room-location">
            <i class="fas fa-map-marker-alt" aria-hidden="true"></i>
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
</div>

<style>
.rooms-tabs {
  max-width: 800px;
  margin: 25px auto;
}

.tabs-nav {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 12px;
  border-bottom: 2px solid var(--light-gray);
  position: relative;
  gap: 3px;
}

.tab-button {
  padding: 8px 14px;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 0.95rem;
  position: relative;
  color: var(--text);
  transition: all 0.3s ease;
  border-radius: 4px 4px 0 0;
}

.tab-button:hover {
  color: var(--primary);
  background-color: rgba(0,0,0,0.03);
}

.tab-button:focus {
  outline: 2px solid var(--primary);
  outline-offset: -2px;
}

.tab-button.active {
  color: var(--primary);
  font-weight: bold;
  background-color: rgba(0,0,0,0.05);
}

.tab-button.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: var(--primary);
}

.tab-panel {
  display: none;
  animation: fadeIn 0.5s ease forwards;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.tab-panel.active {
  display: block;
}

.room-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 3px 12px rgba(0,0,0,0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  max-width: 600px;
}

.room-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

.room-image {
  width: 100%;
  position: relative;
  padding-top: 75%; /* 4:3の比率 */
}

.room-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.room-content {
  padding: 16px;
}

.room-title {
  font-size: 1.2rem;
  margin-bottom: 8px;
  color: var(--primary);
}

.room-location {
  font-size: 0.95rem;
  color: var(--text);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.room-location i {
  color: var(--primary);
}

.room-description {
  margin-bottom: 16px;
  color: var(--text);
  font-size: 0.95rem;
  line-height: 1.4;
}

.room-button {
  display: inline-block;
  padding: 6px 14px;
  background: var(--primary);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
}

.room-button:hover {
  background: var(--text);
  transform: translateY(-2px);
}

.room-button:active {
  transform: translateY(0);
}

/* モバイル対応の強化 */
@media (max-width: 768px) {
  .tabs-nav {
    justify-content: center;
    gap: 2px;
  }
  
  .tab-button {
    padding: 7px 10px;
    font-size: 0.85rem;
    flex: 1 0 auto;
    text-align: center;
  }
  
  .room-content {
    padding: 12px;
  }
  
  .room-title {
    font-size: 1.1rem;
  }
  
  .room-description {
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .tabs-nav {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 4px;
  }
  
  .tab-button {
    padding: 5px 8px;
    font-size: 0.8rem;
  }
  
  .room-button {
    width: 100%;
    text-align: center;
    padding: 6px 10px;
    font-size: 0.85rem;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabPanels = document.querySelectorAll('.tab-panel');
  
  // タブ切り替え機能
  function activateTab(tabIndex) {
    // すべてのタブとパネルから active クラスを削除
    tabButtons.forEach(btn => {
      btn.classList.remove('active');
      btn.setAttribute('aria-selected', 'false');
    });
    
    tabPanels.forEach(panel => {
      panel.classList.remove('active');
      panel.setAttribute('hidden', '');
    });
    
    // 選択されたタブとパネルを active にする
    const selectedButton = document.querySelector(`.tab-button[data-tab="${tabIndex}"]`);
    const selectedPanel = document.querySelector(`.tab-panel[data-tab="${tabIndex}"]`);
    
    selectedButton.classList.add('active');
    selectedButton.setAttribute('aria-selected', 'true');
    
    selectedPanel.classList.add('active');
    selectedPanel.removeAttribute('hidden');
  }
  
  // タブクリックイベント
  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const tabIndex = button.getAttribute('data-tab');
      activateTab(tabIndex);
    });
  });
  
  // キーボードナビゲーションの実装
  tabButtons.forEach((button, index) => {
    button.addEventListener('keydown', (e) => {
      let newIndex;
      
      switch(e.key) {
        case 'ArrowRight':
          newIndex = (index + 1) % tabButtons.length;
          break;
        case 'ArrowLeft':
          newIndex = (index - 1 + tabButtons.length) % tabButtons.length;
          break;
        case 'Home':
          newIndex = 0;
          break;
        case 'End':
          newIndex = tabButtons.length - 1;
          break;
        default:
          return;
      }
      
      // 新しいタブにフォーカスを移動し、アクティブ化
      tabButtons[newIndex].focus();
      activateTab(newIndex);
      e.preventDefault();
    });
  });
});
</script>