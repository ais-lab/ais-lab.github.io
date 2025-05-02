---
title: MosaicArtSystem
author: Park Junwoo
lang: jp
tags:
  - Robotics Art
---

{% case site.lang %}
{% when 'en' %}
# Realization of Participatory Art Using a Robotic Mosaic Art System

## Background
Robotic technology has traditionally been developed primarily to improve efficiency in industrial fields.
In recent years, however, its applications have expanded into a variety of areas, including entertainment and the arts.
In particular, the artistic domain has seen an increasing number of initiatives in which humans and robots collaborate to create works, or in which robots engage in creative activities on their own, opening up new possibilities for artistic expression.

Among various artistic techniques, mosaic art involves assembling small individual parts to form a complete image.
This characteristic aligns well with the step-by-step production process of robots.
Furthermore, since the placement and sequence of the pieces can greatly alter the impression of the work, collaboration between humans and robots enables the creation of unique forms of expression.
By leveraging these characteristics, this study explores new possibilities for artistic expression through the use of robotic technology.

## Robotics Mosaic Art System
{% capture col1 %}
The Robotics Mosaic Art System is a system that generates mosaic art by dividing an image into multiple small parts and using a robotic arm to place these parts in appropriate positions.

This study aims to realize a participatory art form through human-robot collaboration by incorporating interactive elements that allow users to take part in the mosaic creation process.

{% endcapture %}
{% capture col2 %}
{%
  include figure.html
  image="/images/mosaicart/mosaicart.png"
  caption="Robotics Mosaic Art System"
  width="400px"
%}
{% endcapture %}

{%
  include cols.html
  col1=col1
  col2=col2
%}

{%
  include figure.html
  image="/images/mosaicart/flow.png"
  caption="Overview of Participatory Robotics Mosaic Art System"
  width="90%"
%}
The system proposes an optimal placement position based on the similarity between each part and the target image.
The user refers to this suggestion and specifies the placement position, after which the robotic arm physically places the part in the real environment.
By repeating this process, the system gradually constructs the complete mosaic artwork.

{% capture col1 %}
{%
  include figure.html
  image="/images/mosaicart/dexarm.jpg"
  caption="DexArm"
  width="400px"
%}
{% endcapture %}
{% capture col2 %}
## Hardware
- Robot Arm: DexArm
- Modules Used:
    - Air Pump Box
    - Air Picker
    - Rotary Module
    - Sliding Rails

{% endcapture %}

{%
  include cols.html
  col1=col1
  col2=col2
%}

{% when 'jp' %}
# ロボティクスモザイクアートシステムを用いた参加型アートの実現

## 背景
ロボット技術は従来、主に産業分野における効率化のために発展してきました。
しかし近年では、その応用範囲が広がり、娯楽や芸術といった様々な分野にも進出しています。
特に芸術分野では、人間とロボットが共同で作品を作ったり、ロボットが自ら創作活動を行ったりする取り組みが増えており、芸術表現の在り方に新たな可能性をもたらしています。

様々な芸術技法の中で、モザイクアートは、小さなパーツを組み合わせることで、一枚の模様を作り出すという特性を持ち、ロボットの段階的な制作プロセスに親和性が高いです。
また、パーツの配置位置や順序によって作品の印象が大きく変化するため、人間とロボットの協働によって独自な表現を生み出すことができます。
このような特徴を活かし、ロボット技術を活用した新たな芸術表現の可能性を探ります。

## ロボティクスモザイクアートシステム
{% capture col1 %}
ロボティクスモザイクアートシステムは、ある画像を複数のパーツに細分化し、ロボットアームがそれらのパーツを適切に配置することでモザイクアートを生成するシステムです。

本研究では、ユーザがモザイクアートの生成過程に参加できるインタラクティブな要素を導入し、人間とロボットの協働による参加型アートの実現を目的とします。
{% endcapture %}
{% capture col2 %}
{%
  include figure.html
  image="/images/mosaicart/mosaicart.png"
  caption="ロボティクスモザイクアートシステム"
  width="400px"
%}
{% endcapture %}

{%
  include cols.html
  col1=col1
  col2=col2
%}

{%
  include figure.html
  image="/images/mosaicart/flow.png"
  caption="参加型ロボティクスモザイクアートシステムの概要"
  width="90%"
%}
システムは、パーツと目標画像の類似度に基づいて適した配置位置を提案します。ユーザは、その提案を参考に配置位置を指定すると、ロボットアームが実環境でパーツを配置を行います。このプロセスを繰り返すことで、モザイクアートを生成していきます。

{% capture col1 %}
{%
  include figure.html
  image="/images/mosaicart/dexarm.jpg"
  caption="DexArm"
  width="400px"
%}
{% endcapture %}
{% capture col2 %}
## ハードウェア
- ロボットアーム：DexArm
- 使用モジュール
    - エアポンプ
    - エアピッカー
    - 回転モジュール
    - スライディングレール

{% endcapture %}

{%
  include cols.html
  col1=col1
  col2=col2
%}

{% endcase %}