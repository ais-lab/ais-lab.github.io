# アドバンスド・インテリジェント・システム研究室

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
  link="ais-lab"
%}

{% include section.html %}

{% include slider.html
    data="slider_hp"%}

## ハイライト

{% capture text %}

AIS Lab.の学術論文、学会発表などの研究成果をご覧ください。

{%
  include button.html
  link="research"
  text="論文・成果を見る"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/b3_thesis.jpg"
  link="research"
  title="論文・成果"
  text=text
%}

{% capture text %}

研究テーマである「人間を空間の中心とする、潤沢で安全な生活環境を実現する」のもとで行われている研究をご覧ください。

{%
  include button.html
  link="projects"
  text="研究内容一覧を見る"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="/images/feature/team_building.jpg"
  link="projects"
  title="研究内容"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

AIS Lab.のメンバーをご紹介します。

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