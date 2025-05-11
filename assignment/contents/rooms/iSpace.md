---
title: SP LAB 8
author: webstaff
lang: jp
tags:
    - SP LAB
    - iSpace
---
{% case site.lang %}
{% when 'en' %}
# SP LAB 8

{% capture col1 %}
SP LAB 8 is a dedicated room for intelligent space (iSpace) research. This is where iSpace research experiments are conducted and **actively presented to external audiences**. It is an **essential room for iSpace research**, which is the main research focus of AIS Lab. During campus open days, iSpace demonstrations are held here for people of all ages to enjoy. Additionally, since iSpace demonstrations are planned during laboratory open periods, those interested in AIS Lab are encouraged to visit.
{% endcapture %}

{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/iSpace2.JPG"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% when 'jp' %}
# SP LAB 8

{% capture col1 %}
SP LAB 8では、知能化空間（iSpace）の研究を行う専用の部屋です。iSpaceの研究の実験を行ったり、**外部に積極的に公開**したりしています。AIS Lab.の主要な研究である**iSpaceには、欠かせない部屋**です。キャンパス公開のときは、ここでiSpaceのデモをして老若男女に楽しんでもらっています。また、研究室公開期間では、iSpaceのデモを予定しているため、AIS Lab.に興味がある人はぜひ訪れてみてください。
{% endcapture %}

{% capture col2 %}
{% include figure.html
    image="/images/assignment/rooms/iSpace2.JPG"
    width="80%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% endcase %}