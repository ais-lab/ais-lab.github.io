---
title: titles.projects
nav:
  order: 2
  tooltip: tooltips.projects
---


{% if site.lang == 'en' %}
# {% include icon.html icon="fa-solid fa-wrench" %} Research Topics
Our research focuses on the integration of robotics, deep learning, and computer vision to create intelligent systems that enhance daily life and society. We explore applications across intelligent spaces, autonomous navigation, 3D graphical computing, and related fields, aiming to develop technologies that contribute to a more sustainable and human-centered future.
{% else %}
# {% include icon.html icon="fa-solid fa-wrench" %} 研究テーマ
当研究室では、ロボティクス、ディープラーニング、コンピュータビジョンを融合させた知能システムの研究開発に取り組んでいます。インテリジェント空間、自律ナビゲーション、3Dグラフィックスコンピューティングなど幅広い分野への応用を通じて、持続可能で人間中心の未来社会の実現に貢献することを目指しています。
{% endif %}

{% include section.html %}

## ON-GOING

{% include decorate.html data="projects" filter="group == 'active'"%}

{% include section.html %}

## INACTIVE

{% include list.html component="card" data="projects" filter="!group" style="small" %}
