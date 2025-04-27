# 高度知能システム

私たちの研究室では、人間工学、心理学、電子工学、ロボティクスに至るまで、情報科学と工学を幅広く研究しています。  
この研究室では、人間と人工知能システムの相互作用のためのソリューションを設計しています。

{%
  include button.html
  type="docs"
  text="研究内容"
  link="https://greene-lab.gitbook.io/lab-website-template-docs"
%}
{%
  include button.html
  type="github"
  text="GitHubで見る"
  link="greenelab/lab-website-template"
%}

{% include section.html %}

{% include slider.html
    data="slider_hp"%}

## ハイライト

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="research"
  text="研究業績を見る"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/b3_thesis.jpg"
  link="research"
  title="研究内容"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="projects"
  text="プロジェクト一覧を見る"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/team_building.jpg"
  link="projects"
  title="プロジェクト"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="team"
  text="メンバー紹介"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/nomikai.jpg"
  link="team"
  title="チーム紹介"
  text=text
%}