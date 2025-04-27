---
title: titles.contact
nav:
  order: 5
  tooltip: tooltips.contact
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

## {%t contact.lab_title %}
{% case site.lang %}
{% when 'en' %}
  <br>Ritsumeikan University<br>
  <br>College of Information Science and Engineering<br>
  <br>Department of Information Science and Engineering, [Physical Computing Course](https://www.phy.ise.ritsumei.ac.jp/)<br>
  <br>Room H525, Building H,<br>
  <br>2-150, Iwakura-cho, Ibaraki-shi, Osaka, 5678570, Japan.<br>

{% when 'jp' %}
  <br>立命館大学<br>
  <br>情報理工学部　情報理工学科　[実世界コース](https://www.phy.ise.ritsumei.ac.jp/)<br>
  <br><span style="color:red;">新住所(2024年4月より)：</span><br>
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

## {%t contact.access_title %}

{% case site.lang %}
{% when 'en' %}
<div class="map-container">
  <iframe 
     src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3275.831375021552!2d135.5610037!3d34.810183999999985!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e3280cce6417%3A0xbb3d925acbf40ab5!2z56uL5ZG96aSo5aSn5a2mIC0g5aSn6Ziq44GE44Gw44KJ44GN44Kt44Oj44Oz44OR44K5!5e0!3m2!1sen!2sjp!4v1745632808994!5m2!1sen!2sjp" 
    width="100%" 
    height="450" 
    style="border:0;" 
    allowfullscreen="" 
    loading="lazy" 
    referrerpolicy="no-referrer-when-downgrade">
  </iframe>
</div>
{% when 'jp' %}
<div class="map-container">
  <iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3275.831375021552!2d135.5610037!3d34.810183999999985!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e3280cce6417%3A0xbb3d925acbf40ab5!2z56uL5ZG96aSo5aSn5a2mIC0g5aSn6Ziq44GE44Gw44KJ44GN44Kt44Oj44Oz44OR44K5!5e0!3m2!1sja!2sjp!4v1745632808994!5m2!1sja!2sjp" 
    width="100%" 
    height="450" 
    style="border:0;" 
    allowfullscreen=""
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade">
  </iframe>
<div>
{% endcase %}


