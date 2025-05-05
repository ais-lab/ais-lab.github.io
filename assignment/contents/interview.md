---
title: 在学生のインタビュー
author: webstaff
lang: jp
tags:
    - interview
    - StudentInterview
    - AIS Lab. Life
---

<style>
  .responsive-video {
    width: 100%;
    max-width: 600px;
    height: 400px;
  }
  
  @media (max-width: 600px) {
    .responsive-video {
      width: 100%;
      height: auto;
    }
  }

</style>
{% case site.lang %}
{% when 'en' %}
# Interview with Current Students
**Click the image to play the video.**
## Latest Video (<span style="color:red;">Now Updating!!!</span>)
<iframe src="http://www.aislab.org/wp-content/uploads/2022/06/インタビュー動画.mp4" class="responsive-video"></iframe>

## Past Videos
{% capture col1 %}
**2020**
<iframe src="http://www.aislab.org/wp-content/uploads/2020/07/labo_presen_final.mp4" class="responsive-video"></iframe>

**2017**
<iframe src="http://www.aislab.org/wp-content/uploads/2017/06/interview2017.mp4" class="responsive-video"></iframe>

**2015 (Graduate Students)**
<iframe src="http://www.aislab.org/interview/interview2015m.mp4" class="responsive-video"></iframe>

**2014**
<iframe src="http://www.aislab.org/interview/interview2014.mp4" class="responsive-video"></iframe> 
{% endcapture %}
{% capture col2 %}

**2018**
<iframe src="http://www.aislab.org/wp-content/uploads/2018/06/interview2018.mp4" class="responsive-video"></iframe>

**2016**
<iframe src="http://www.aislab.org/wp-content/uploads/2016/06/interview2016b.mp4" class="responsive-video"></iframe>

**2015 (Undergraduate Students)**
<iframe src="http://www.aislab.org/interview/interview2015b.mp4" class="responsive-video"></iframe>

**2013**
<iframe src="http://www.aislab.org/interview/interview2013.mp4" class="responsive-video"></iframe> 
{% endcapture %}

{% include cols.html 
    col1=col1 
    col2=col2 
%}
**2012**
{% capture col1 %}
Q. What kind of lab is AIS Lab?
<iframe src="http://www.aislab.org/interview/01.mp4" class="responsive-video"></iframe>

Q. Why did you choose this lab?
<iframe src="http://www.aislab.org/interview/03.mp4" class="responsive-video"></iframe>

Q. What kind of research are you doing?
<iframe src="http://www.aislab.org/interview/05.mp4" class="responsive-video"></iframe>

Q. What are the strengths of this lab?
<iframe src="http://www.aislab.org/interview/07.mp4" class="responsive-video"></iframe>

Bonus
<iframe src="http://www.aislab.org/interview/09.mp4" class="responsive-video"></iframe> 
{% endcapture %}

{% capture col2 %}
Q. What kind of professor is Prof. Lee?
<iframe src="http://www.aislab.org/interview/02.mp4" class="responsive-video"></iframe>

Q. What aspects of the lab were useful for job hunting?
<iframe src="http://www.aislab.org/interview/04.mp4" class="responsive-video"></iframe>

Q. What was the most challenging experience?
<iframe src="http://www.aislab.org/interview/06.mp4" class="responsive-video"></iframe>

Q. Any message for junior students?
<iframe src="http://www.aislab.org/interview/08.mp4" class="responsive-video"></iframe> 
{% endcapture %}
{% include cols.html 
    col1=col1 
    col2=col2 
%}

{% when 'jp' %}
# 在校生のインタビュー
**画像をクリックすると動画が再生されます。**
## 最新動画（<span style="color:red;">更新中！！！</span>）
<iframe src="http://www.aislab.org/wp-content/uploads/2022/06/インタビュー動画.mp4" class="responsive-video"></iframe>

## 過去の動画
{% capture col1 %}
**2020年**
<iframe src="http://www.aislab.org/wp-content/uploads/2020/07/labo_presen_final.mp4" class="responsive-video"></iframe>

**2017年**
<iframe src="http://www.aislab.org/wp-content/uploads/2017/06/interview2017.mp4" class="responsive-video"></iframe>

**2015年院生**
<iframe src="http://www.aislab.org/interview/interview2015m.mp4" class="responsive-video"></iframe>

**2014年**
<iframe src="http://www.aislab.org/interview/interview2014.mp4" class="responsive-video"></iframe>

{% endcapture %}
{% capture col2 %}
**2018年**
<iframe src="http://www.aislab.org/wp-content/uploads/2018/06/interview2018.mp4" class="responsive-video"></iframe>

**2016年**
<iframe src="http://www.aislab.org/wp-content/uploads/2016/06/interview2016b.mp4" class="responsive-video"></iframe>

**学部生**
<iframe src="http://www.aislab.org/interview/interview2015b.mp4" class="responsive-video"></iframe>

**2013年**
<iframe src="http://www.aislab.org/interview/interview2013.mp4" class="responsive-video"></iframe>
{% endcapture %}

{%
  include cols.html
  col1=col1
  col2=col2
%}
**2012年**

{% capture col1 %}
Q.AIS研究室は，どんな研究室？
<iframe src="http://www.aislab.org/interview/01.mp4" class="responsive-video"></iframe>

Q.この研究室を選んだ理由は？
<iframe src="http://www.aislab.org/interview/03.mp4" class="responsive-video"></iframe>

Q.どんな研究をしている？
<iframe src="http://www.aislab.org/interview/05.mp4" class="responsive-video"></iframe>

Q.この研究室の強みは？
<iframe src="http://www.aislab.org/interview/07.mp4" class="responsive-video"></iframe>

おまけ
<iframe src="http://www.aislab.org/interview/09.mp4" class="responsive-video"></iframe>
{% endcapture %}

{% capture col2 %}
Q.李先生は，どんな先生？
<iframe src="http://www.aislab.org/interview/02.mp4" class="responsive-video"></iframe>

Q.就職活動で役立った点は？
<iframe src="http://www.aislab.org/interview/04.mp4" class="responsive-video"></iframe>

Q.厳しかったことは？
<iframe src="http://www.aislab.org/interview/06.mp4" class="responsive-video"></iframe>

Q.3回生へのメッセージ
<iframe src="http://www.aislab.org/interview/08.mp4" class="responsive-video"></iframe>

{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% endcase %}