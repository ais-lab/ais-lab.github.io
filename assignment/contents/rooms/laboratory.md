---
title: Laboratory
author: webstaff
lang: jp
tags:
    - laboratory
    - Robotics
---
{% case site.lang %}
{% when 'en' %}
# Laboratory

{% capture col1 %}
The laboratory has a spacious area secured for the development and experimentation of various types of robots. Here, students researching robotics exchange ideas while developing robots and improving their performance. Additionally, since there are records of past robot research, students can develop robots with reference to previous research or quickly understand the mechanisms of past robots.
{% endcapture %}
{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/laboratory1.jpg"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% when  'jp' %}
# 実験室

{% capture col1 %}
実験室では、広いスペースが確保されており、様々なタイプのロボットの開発と実験を行っています。ここでは、ロボットを研究している学生同士で意見交換をしながら、ロボットの開発や性能向上をしています。また、過去のロボットの研究があるため、過去の研究を参考にしながらロボットを開発したり、過去のロボットの仕組みをすぐに理解したりすることができます。
{% endcapture %}
{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/laboratory1.jpg"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% endcase %}