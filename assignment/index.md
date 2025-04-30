---
title: titles.assignment
nav:
  order: 6
  tooltip: tooltips.assignment
---

# {% include icon.html icon="fa-solid fa-robot" %} {%t assignment.assignment_title %}
{% case site.lang %}
{% when 'jp' %}
アドバンスド・インテリジェント・システム研究室に興味をいていただき、真にありがとうござ います。このページは実世界情報コースの新卒研生（3回生）のために作られたものです。

{% when 'en' %}
Thank you very much for your interest in the Advanced Intelligent Systems Laboratory. This page was created for new graduate students (3rd year students) in the Real World Information Course.
{% endcase %}
## {% include icon.html icon="fa-solid fa-circle-info" %} {%t assignment.openlab_title %}
{% case site.lang %}
{% when 'jp' %}
研究室公開期間中（<span style="color:red;">H525 6月2（月）〜6月11日（水）</span>）は研究室の教員と先輩たちが皆さんの要望に応じて研究室に関することなら何でも紹介します。気軽にアクセスしてみてください。
{% when 'en' %}
During the laboratory open period (<span style="color:red;">June 2 (Monday) to June 11 (Wednesday), 2025</span>), the faculty and senior students of the laboratory will introduce anything related to the laboratory according to your requests. Please feel free to visit.
{% endcase %}

{% include section.html %}
## {% include icon.html icon="fa-solid fa-tags" %}{%t assignment.assignment_contents %}
{% include list.html component="card" data="recruit" filter="group == 'contents'" style="small" %}

{% include section.html %}
## {% include icon.html icon="fa-solid fa-circle-check" %}{%t assignment.about_assignment %}
{% include list.html component="card" data="recruit" filter="!group" style="small" %}
