---
title: titles.contact
nav:
  order: 5
  tooltip: tooltips.contact
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

{% case site.lang %}
{% when 'en' %}
  ### Advanced Intelligent System Lab.(AIS Lab.)
  <br>Ritsumeikan University<br>
  <br>College of Information Science and Engineering<br>
  <br>Department of Information Science and Engineering, Physical Computing Course<br>
  <br>Room H525, Building H,<br>
  <br>2-150, Iwakura-cho, Ibaraki-shi, Osaka, 5678570, Japan.<br>
{% when 'jp' %}
  ### アドバンスド・インテリジェント・システム研究室(AIS Lab.)
  <br>立命館大学<br>
  <br>情報理工学部　情報理工学科　実世界コース<br>
  <br>新住所(2024年4月より)：<br>
  <br>〒567-8570 大阪府茨木市岩倉町2-150 H棟H525<br>
{% endcase %}

{%
  include button.html
  type="email"
  text="leejooho@is.ritsumei.ac.jp"
  link="leejooho@is.ritsumei.ac.jp"
%}
{%
  include button.html
  type="phone"
  text="072-665-2906"
  link="072-665-2906"
%}
{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://maps.app.goo.gl/YEAj9aWiAnydeHkj8"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/photo.jpg"
  caption="Lorem ipsum"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/photo.jpg"
  caption="Lorem ipsum"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% capture col2 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% capture col3 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}
