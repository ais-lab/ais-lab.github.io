---
layout: default
title: Home
lang: en
---

{% if site.lang == "jp" %}
# 高度知能システム

私たちの研究室では、人間工学、心理学、電子工学、ロボティクスに至るまで、情報科学と工学を幅広く研究しています。  
この研究室では、人間と人工知能システムの相互作用のためのソリューションを設計しています。

{%
  include button.html
  type="docs"
  text="研究内容"
  link="https://greene-lab.gitbook.io/lab-website-template-docs"
%}
{%
  include button.html
  type="github"
  text="GitHubで見る"
  link="greenelab/lab-website-template"
%}

{% elsif site.lang == "en" %}
# Advanced Intelligent System

Our research focuses on information science and engineering varied from human engineering, psychology, electronics to robotics. In this lab we design solutions for Interaction between humans and artificial intelligent systems.

{%
  include button.html
  type="docs"
  text="Our Research"
  link="https://greene-lab.gitbook.io/lab-website-template-docs"
%}
{%
  include button.html
  type="github"
  text="On GitHub"
  link="greenelab/lab-website-template"
%}
{% endif %}



{% include section.html %}

{% include slider.html
    data="slider_hp"%}

{% if site.lang == "jp" %}

## ハイライト

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="research"
  text="研究業績を見る"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/b3_thesis.jpg"
  link="research"
  title="研究内容"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="projects"
  text="プロジェクト一覧を見る"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/team_building.jpg"
  link="projects"
  title="プロジェクト"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="team"
  text="メンバー紹介"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/nomikai.jpg"
  link="team"
  title="チーム紹介"
  text=text
%}

{% elsif site.lang == "en" %}
## Highlights

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/feature/b3_thesis.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/feature/team_building.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/feature/nomikai.jpg"
  link="team"
  title="Our Team"
  text=text
%}

{% endif %}