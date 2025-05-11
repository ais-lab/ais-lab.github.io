---
title: Main Laboratory
author: webstaff
lang: jp
tags:
    - Main Laboratory
    - CV
---
{% case site.lang %}
{% when 'en' %}
# Main Laboratory

{% capture col1 %}
In the AIS Lab's main laboratory, desks and computers are provided for each student to work comfortably, functioning as a daily research space and student workspace. In the shared space, students enjoy snacks from various countries while engaging in active interaction **regardless of seniority**. Due to the close relationships between students, it's easy to approach senior students to share new knowledge and ideas that enhance research. Near the entrance, there are paintings and Yogibo bean bags where students can relax. There is also a **PlayStation 5** with a large monitor, allowing everyone to enjoy games on a big screen.
{% endcapture %}
{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/main-lab1.jpg"
    width="80%"
%}
{% include figure.html
    image="/images/assignment/rooms/main-lab3.jpg"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% when 'jp' %}
# メインラボ

{% capture col1 %}
AIS Lab. のメインラボでは、各学生が快適に作業できるように机とコンピュータが用意されており、日々の研究活動や学生のワークスペースとして機能しています。また共有スペースでは、各国のお菓子を食べながら、**先輩後輩関係なく学生間の交流**が活発です。学生間の距離が近いため、先輩にも話をしやすく新たな知識や考え方を共有し、研究に活かしています。入口付近には、絵画が飾られていたり、yogiboがあったりします。ここでは、リラックスをすることができます。また**PlayStation 5**と大きなモニターがあるため、大画面でゲームを楽しむことができます。
{% endcapture %}

{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/main-lab1.jpg"
    width="80%"
%}
{% include figure.html
    image="/images/assignment/rooms/main-lab3.jpg"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% endcase %}