---
title: titles.blog
nav:
  order: 4
  tooltip: tooltips.blog
---

{% if site.lang == "en" %}

# {% include icon.html icon="fa-solid fa-newspaper" %} News

Welcome to our lab's news page. Here we share the latest updates on our research activities, including:

- {% include icon.html icon="fa-solid fa-bullhorn" %} Conference presentations and invited talks  
- {% include icon.html icon="fa-solid fa-trophy" %} Awards and recognitions  
- {% include icon.html icon="fa-solid fa-handshake" %} Collaborative projects and outreach events  
  
{% endif %}

{% if site.lang == "jp" %}

# {% include icon.html icon="fa-solid fa-newspaper" %} ニュース

私たちの研究室のニュースページへようこそ。  
このページでは、研究活動に関する最新情報をお届けしています。主な内容は以下のとおりです：

- {% include icon.html icon="fa-solid fa-bullhorn" %} 学会発表や招待講演  
- {% include icon.html icon="fa-solid fa-trophy" %} 受賞歴・表彰  
- {% include icon.html icon="fa-solid fa-handshake" %} 共同研究やアウトリーチ活動  
  
{% endif %}

{% include section.html %}

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}
