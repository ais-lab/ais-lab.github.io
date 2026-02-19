import os
import re
import requests
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 1. 環境変数の取得
SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]
MESSAGE_URL = os.environ.get("MESSAGE_URL", "")
EVENT_NAME = os.environ.get("EVENT_NAME", "new-event").replace(" ", "-")

client = WebClient(token=SLACK_TOKEN)

def extract_ts_from_url(url):
    """Slack URL末尾の p1771512751000123 から 1771512751.000123 を抽出"""
    match = re.search(r'p(\d{10})(\d{6})', url)
    if match:
        return f"{match.group(1)}.{match.group(2)}"
    return url

def split_title_and_body(content, default_title):
    """
    '==='（半角）または '＝＝＝'（全角）が3つ以上並んでいる箇所で分割する。
    境界線がない場合は、1行目をタイトルにする。
    """
    # 正規表現: 半角'='または全角'＝'が3回以上続く
    pattern = r'[=＝]{3,}'
    parts = re.split(pattern, content, maxsplit=1)
    
    if len(parts) > 1:
        title = parts[0].strip()
        body = parts[1].strip()
    else:
        # 境界線がない場合のフォールバック（以前の仕様を維持）
        lines = content.splitlines()
        title = lines[0].strip() if lines else default_title
        body = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
    
    return title, body

def create_post():
    thread_ts = extract_ts_from_url(MESSAGE_URL)
    
    try:
        res = client.conversations_replies(channel=CHANNEL_ID, ts=thread_ts)
        replies = res["messages"]
    except SlackApiError as e:
        print(f"Slack APIエラー: {e.response['error']}")
        return

    # 内容の取得
    jp_raw = replies[0]["text"]
    en_raw = replies[1]["text"] if len(replies) > 1 else "English version follows soon."
    
    # 日本語版のタイトル・本文分割
    jp_title, jp_body = split_title_and_body(jp_raw, EVENT_NAME)
    
    # 英語版のタイトル・本文分割（英語スレッドに区切りがない場合はEVENT_NAMEを使用）
    en_default_title = EVENT_NAME.replace("-", " ").capitalize()
    en_title, en_body = split_title_and_body(en_raw, en_default_title)
    # 英語スレッドに区切りがなかった場合、タイトルをEVENT_NAME形式に上書き
    if "===" not in en_raw and "＝＝＝" not in en_raw:
        en_title = en_default_title
        en_body = en_raw

    # 画像の抽出
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    rel_path = f"images/uploads/{now.strftime('%Y/%m')}"
    abs_path = os.path.join(os.getcwd(), rel_path)
    os.makedirs(abs_path, exist_ok=True)
    
    image_paths = []
    for msg in replies[2:]:
        if "files" in msg:
            for file in msg["files"]:
                ext = os.path.splitext(file["name"])[1]
                file_name = f"{EVENT_NAME}_{len(image_paths)+1}{ext}"
                save_path = os.path.join(abs_path, file_name)
                
                res_img = requests.get(file["url_private_download"], 
                                      headers={"Authorization": f"Bearer {SLACK_TOKEN}"})
                with open(save_path, "wb") as f:
                    f.write(res_img.content)
                
                image_paths.append(f"/{rel_path}/{file_name}")

    if not image_paths:
        image_paths = ["/images/default.jpg"]

    # 2段組みHTML生成
    col1_list = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 == 0]
    col2_list = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 != 0]

    def generate_md(lang, title, body):
        col1_text = "\n".join(col1_list)
        col2_text = "\n".join(col2_list)
        
        template = f"""---
title: "{title}"
author: aislab_webstaff
lang: {lang}
image: {image_paths[0]}
tags: event
---
{body}

{{% capture col1 %}}
{col1_text}
{{% endcapture %}}

{{% capture col2 %}}
{col2_text}
{{% endcapture %}}

{{% include cols.html col1=col1 col2=col2 %}}
"""
        file_path = f"_i18n/{lang}/_posts/{date_str}-{EVENT_NAME}.md"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template)
            print(f"Created: {file_path}")

    generate_md("jp", jp_title, jp_body)
    generate_md("en", en_title, en_body)

if __name__ == "__main__":
    create_post()
