---
title: Workshop
author: webstaff
lang: jp
tags:
    - Workshop
---
{% case site.lang %}
{% when 'en' %}
# Workshop

{% capture col1 %}
The workshop is equipped with **six 3D printers**, allowing students to efficiently print models and create circuits using electronic circuit boards. There are workbenches where students can work on electronics projects with tools like soldering irons. Next to this area, numerous electronic components are available, enabling students to immediately begin electronics work. The workshop is also a place where third-year undergraduate students deepen their relationships during **Graduation Research 1** (a period when B3 students create projects in image processing and robotics fields individually or in teams) and spring workshops (an opportunity for B3 students aiming for graduate school to attend lectures from seniors, deepen their knowledge and relationships with upperclassmen, and build line-following cars).
{% endcapture %}

{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/workshop1.jpg"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% when 'jp' %}
# 工作室
{% capture col1 %}
工作室では、**3Dプリンタが6台**もあり、学生が効率的にモデルを印刷できたり、電子基板を使用して、回路を作ったりできます。作業台が備わっており、そこでははんだごてなど電子工作ができる環境があります。その隣には、電子部品が多数あり、部品を取ってすぐに電子工作ができます。また、**卒業研究1**（B3が個人やチームで画像処理、ロボット分野で作品を作る期間）や春の講習会（院進学志望のB3が春休みの期間に先輩の講義を聞き、知識や先輩との交流を深めたり、ライントレースカー制作をする機会）があり、B3の仲を深める場でもあります。
{% endcapture %}

{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/workshop1.jpg"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% endcase %}
