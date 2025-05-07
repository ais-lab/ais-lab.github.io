---
title: Visual Localization and Mapping
author: Itsuki Kawahara
lang: jp
tags:
  - CV
  - Visual Localization
  - Mapping
---

# Visual Localization and Mapping

{% case site.lang %}
{% when 'en' %}
## Background
Precise localization technology plays a crucial role in many applications, including augmented reality and autonomous systems. Common approaches utilize expensive hardware such as LIDAR sensors, GPS, WiFi, or Bluetooth. However, these hardware sensors become less effective in GPS-denied environments, including adverse weather conditions and indoor environments. As an alternative solution, inexpensive visual sensors can be employed. Nevertheless, robust visual localization based on a single image remains challenging.

To address this challenge, we propose a method for robust visual localization that replaces either all steps or certain components of the traditional pipeline with deep learning-based trainable models. This approach aims to overcome the limitations of current visual localization techniques by leveraging the power of deep learning to improve accuracy and robustness in challenging environments.

## Proposal Methods
### FeatLoc
{% capture col1 %}
FeatLoc is a method for indoor 3D self-localization. It was published in the ISPRS Journal of Photogrammetry and Remote Sensing in 2022. FeatLoc uses 2D camera data to perform 3D self-localization in indoor environments. It has been proven to achieve higher accuracy and performance compared to existing methods.
{% endcapture %}
{% capture col2 %}
{% include figure.html
   image="https://raw.githubusercontent.com/ais-lab/FeatLoc/1deb579099037a9a4564ad8d85c8897857761648/doc/fig4.svg"
   caption="FeatLoc Network Architecture"
   width="100%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% include figure.html
   image="https://github.com/ais-lab/FeatLoc/raw/main/doc/fig1.svg"
   caption="FeatLoc Results"
   width="60%"
%}

## D2s
{% capture col1 %}
Previous state-of-the-art self-localization methods may involve significant costs during inference and storage due to their complex procedures. In response, D2S offers a method that generates 3D scene coordinates from sparse descriptors extracted from a single RGB image using a simple network. This approach demonstrates superior performance compared to state-of-the-art CNN-based methods.
{% endcapture %}
{% capture col2 %}
{% include figure.html
   image="https://thpjp.github.io/d2s/images/pipeline.svg"
   caption="D2S Pipeline"
   width="100%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}

## PL2Map
{% capture col1 %}
In recent years, integrating point and line features in images has been expected to achieve better accuracy as a method for visual localization and mapping. However, extending localization frameworks can increase the memory and computational resources required for matching tasks. PL2Map is a technique where lightweight neural networks learn to represent both 3D point and line features, achieving excellent pose accuracy by leveraging multiple learned mappings.
{% endcapture %}
{% capture col2 %}
{% include figure.html
   image="https://thpjp.github.io/pl2map/images/pipeline.svg"
   caption="PL2Map Pipeline"
   width="100%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% include responsive-file.html type="video" url="https://thpjp.github.io/pl2map/images/video1.mp4" caption="Demo Video of PL2Map" width="70%" %}

## D2S+NeRF
{% capture col1 %}
Neural Radiance Fields (NeRF) is a technology published in 2020 that uses neural networks to create 3D scenes from multiple photographs. Due to deep learning models' dependence on large amounts of data, performance decreases when data samples are limited. To address this challenge, D2S+NeRF introduces a pipeline for keypoint descriptor synthesis using NeRF, effectively solving this issue.
{% endcapture %}
{% capture col2 %}
{% include responsive-file.html type="video" url="https://private-user-images.githubusercontent.com/46952800/374812253-98071e95-8ace-417e-a44c-58f5c62f6af8.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY1OTEyNzMsIm5iZiI6MTc0NjU5MDk3MywicGF0aCI6Ii80Njk1MjgwMC8zNzQ4MTIyNTMtOTgwNzFlOTUtOGFjZS00MTdlLWE0NGMtNThmNWM2MmY2YWY4Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA3VDA0MDkzM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTA0MDcxNjU1YjE4M2UxYWE5Y2RhODg2ZTU3NTQzYjJhZDZiNTY1MWJmNjUzZTdkYWE2ZmMwNmVlOTNkOTZlYjEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.DMYJu5nUgJ4yWi11mrgFoMFVJg4qR97Xj_JKxioWHzk" caption="D2S+NeRFデモビデオ" width="100%" %}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}

{% when 'jp' %}
## 背景
精密な位置推定技術は、AR、自律システムなど、多くのアプリケーションにおいて重要な役割を果たしています。一般的なアプローチとして、LIDARセンサ、GPS、WiFiまたはBluetoothなどの高価なハードウェアを用いたものがあります。しかしながら、このようなハードウェアセンサは、悪天候、屋内環境などのGPS信号が届かない環境では、効果が減少します。そこで、もう一つの一般的な解決策として、安価な視覚センサを用いる方法があげられます。しかし、単一画像に基づく堅牢な視覚的位置推定は、依然として課題があります。

そこで、深層学習を用いて、学習ベースの全てのステップまたは一部のステップを学習可能なモデルに置き換え、堅牢な視覚的位置推定の手法を提案します。

## 提案手法
### FeatLoc
{% capture col1 %}
FeatLocは、室内用3次元自己位置推定のための手法です。2022年にISPRS Journal of Photogrammetry and Remote Sensingに記載されました。2Dカメラデータを用いて室内環境の3次元自己位置推定を行います。FeatLocは、既存の手法より高い精度と性能であることが証明されています。
{% endcapture %}
{% capture col2 %}
{% include figure.html
   image="https://raw.githubusercontent.com/ais-lab/FeatLoc/1deb579099037a9a4564ad8d85c8897857761648/doc/fig4.svg"
   caption="FeatLocネットワークアーキテクチャ"
   width="100%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% include figure.html
   image="https://github.com/ais-lab/FeatLoc/raw/main/doc/fig1.svg"
   caption="FeatLocの結果"
   width="60%"
%}

## D2S
{% capture col1 %}
これまでの最先端の自己位置推定手法は、複雑な手順を用いて推定しているため、推論、保存の際に、多大なコストを伴う可能性があります。そこで、D2Sは、シンプルなネットワークを用いて、単一のRGB画像から抽出したスパース記述子から3Dシーン座標を生成する手法であり、最先端のCNNベースの手法と比較して、より高い性能です。
{% endcapture %}
{% capture col2 %}
{% include figure.html
   image="https://thpjp.github.io/d2s/images/pipeline.svg"
   caption="D2Sパイプライン"
   width="100%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}

## PL2Map
{% capture col1 %}
近年、視覚的な位置推定と地図作成の手法として、画像内の点と線の特徴の統合をすることで、よりよい精度が期待されるが、位置推定フレームワークを拡張することで、マッチングタスクに必要なメモリと計算リソースが増加することがあります。PL2Mapは、軽量なニューラルネットワークが3Dの点と線の両方の特徴を表現することを学習し、複数の学習済みマッピングを活用することで、優れた姿勢精度を発揮する手法です。
{% endcapture %}
{% capture col2 %}
{% include figure.html
   image="https://thpjp.github.io/pl2map/images/pipeline.svg"
   caption="PL2Mapパイプライン"
   width="100%"
%}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% include responsive-file.html type="video" url="https://thpjp.github.io/pl2map/images/video1.mp4" caption="PL2Mapデモビデオ" width="70%" %}

## D2S+NeRF
{% capture col1 %}
Neural Radiance Fields（NeRF）は、2020年に発表された技術で、ニューラルネットワークを使用して、複数の写真から3Dシーンを作成します。深層学習モデルが大量のデータに依存するため、データサンプルが限られている場合は、性能が下がる問題がある。そこで、D2S+NeRFは、NeRFを使用したキーポイント記述子合成のためのパイプラインを導入することで、この課題に対する解決します。
{% endcapture %}
{% capture col2 %}
{% include responsive-file.html type="video" url="https://private-user-images.githubusercontent.com/46952800/374812253-98071e95-8ace-417e-a44c-58f5c62f6af8.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY1OTEyNzMsIm5iZiI6MTc0NjU5MDk3MywicGF0aCI6Ii80Njk1MjgwMC8zNzQ4MTIyNTMtOTgwNzFlOTUtOGFjZS00MTdlLWE0NGMtNThmNWM2MmY2YWY4Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA3VDA0MDkzM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTA0MDcxNjU1YjE4M2UxYWE5Y2RhODg2ZTU3NTQzYjJhZDZiNTY1MWJmNjUzZTdkYWE2ZmMwNmVlOTNkOTZlYjEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.DMYJu5nUgJ4yWi11mrgFoMFVJg4qR97Xj_JKxioWHzk" caption="D2S+NeRFデモビデオ" width="100%" %}
{% endcapture %}
{%
  include cols.html
  col1=col1
  col2=col2
%}
{% endcase %}
