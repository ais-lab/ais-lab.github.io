---
title: titles.team
nav:
  order: 3
  tooltip: tooltips.team
---

# {% include icon.html icon="fa-solid fa-users" %} AIS Lab

{% include section.html %}
# Administration
<div class="be-prof">
  {% include list.html data="members" component="portrait" filter="role == 'pi' or role == 'ap' or role == 'vr'" %}
</div>

{% include section.html %}
# Staff・Postdoctoral・Exchange Student
{% include list.html data="members" component="portrait" filter="role == 's' or role == 'pd' or role == 'is'" %}

{% include section.html %}
# Graduate Student
{% include list.html data="members" component="portrait" filter="role == 'phd'" year_asc="True" %}
---
{% include list.html data="members" component="portrait" filter="role == 'm'" year_asc="True" %}


{% include section.html %}
# Undergraduate Student
{% include list.html data="members" component="portrait" filter="role == 'b'" year_asc="True" %}

{% include section.html background="images/background.jpg" dark=true %}

# Alumni

{% include section.html %}

{% capture content %}

{% include figure.html image="/images/yearbook/wc_party25.jpg" %}

{% endcapture %}

{% include grid.html content=content %}
