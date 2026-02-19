import os
import requests
from datetime import datetime
from slack_sdk import WebClient

SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]
THREAD_TS = os.environ["THREAD_TS"]
EVENT_NAME = os.environ.get("EVENT_NAME", "new-event").replace(" ", "-")

client = WebClient(token=SLACK_TOKEN)

def create_post():
    # 1. スレッド情報の取得
    res = client.conversations_replies(channel=CHANNEL_ID, ts=THREAD_TS)
    replies = res["messages"]
    
    jp_body = replies[0]["text"]
    en_body = replies[1]["text"] if len(replies) > 1 else jp_body
    
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    rel_path = f"images/uploads/{now.strftime('%Y/%m')}"
    abs_path = os.path.join(os.getcwd(), rel_path)
    os.makedirs(abs_path, exist_ok=True)
    
    # 2. 画像のダウンロードとリスト化
    image_paths = []
    for msg in replies:
        if "files" in msg:
            for file in msg["files"]:
                ext = os.path.splitext(file["name"])[1]
                file_name = f"{EVENT_NAME}_{len(image_paths)+1}{ext}"
                save_path = os.path.join(abs_path, file_name)
                
                # ダウンロード
                res = requests.get(file["url_private_download"], 
                                   headers={"Authorization": f"Bearer {SLACK_TOKEN}"})
                with open(save_path, "wb") as f:
                    f.write(res.content)
                
                # Jekyllで読み込む用のパス (/images/...)
                image_paths.append(f"/{rel_path}/{file_name}")

    if not image_paths:
        image_paths = ["/images/default.jpg"] # 画像がない場合のフォールバック

    # 3. カラムの生成 (奇数はcol1, 偶数はcol2)
    col1_imgs = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 == 0]
    col2_imgs = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 != 0]

    # 4. Markdown生成関数
    def generate_md(lang, content):
        first_image = image_paths[0]
        template = f"""---
title: {jp_body.splitlines()[0] if lang == 'jp' else EVENT_NAME}
author: aislab_webstaff
lang: {lang}
image: {first_image}
tags: event
---
{content}

{{% capture col1 %}}
{"".join(col1_imgs)}
{{% endcapture %}}

{{% capture col2 %}}
{"".join(col2_imgs)}
{{% endcapture %}}

{{% include cols.html col1=col1 col2=col2 %}}
"""
        file_path = f"_i18n/{lang}/_posts/{date_str}-{EVENT_NAME}.md"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template)

    # 日本語版と英語版を出力
    generate_md("jp", jp_body)
    generate_md("en", en_body)

if __name__ == "__main__":
    create_post()