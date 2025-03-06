---
title: titles.team
nav:
  order: 3
  tooltip: tooltips.team
---

# {% include icon.html icon="fa-solid fa-users" %} AIS Lab



{% include list.html data="members" component="portrait" filter="role == 'pi'" %}
{% include section.html %}
{% include list.html data="members" component="portrait" filter="role == 'phd'" year_asc="True" %}
---
{% include list.html data="members" component="portrait" filter="role == 'm' or role =='b'" year_asc="True" %}
{% include section.html background="images/background.jpg" dark=true %}

# Alumni

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
