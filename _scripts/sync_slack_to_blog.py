import os
import requests
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 1. 環境変数の取得
SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]
THREAD_TS_RAW = os.environ["THREAD_TS"]
EVENT_NAME = os.environ.get("EVENT_NAME", "new-event").replace(" ", "-")

client = WebClient(token=SLACK_TOKEN)

def convert_ts(ts_str):
    """人間が読みやすい形式または数値をSlack API用のTSに変換する"""
    # try:
    #     # スプレッドシートの書式が "Feb 19, 2026, 1:24:13 PM" の場合
    #     dt_obj = datetime.strptime(ts_str, "%b %d, %Y, %I:%M:%S %p")
    #     return str(dt_obj.timestamp())
    # except Exception:
    #     # すでに数値形式（17400...）の場合はそのまま返す
    #     return ts_str
    return str(ts_str).strip()

def create_post():
    # タイムスタンプを変換してスレッド取得
    thread_ts = convert_ts(THREAD_TS_RAW)
    
    try:
        res = client.conversations_replies(channel=CHANNEL_ID, ts=thread_ts)
        replies = res["messages"]
    except SlackApiError as e:
        print(f"Slack APIエラー: {e.response['error']}")
        return

    # 【仕様】親:JP本文, 返信1:EN本文, 返信2以降:画像
    jp_body = replies[0]["text"]
    en_body = replies[1]["text"] if len(replies) > 1 else "English version follows soon."
    
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    rel_path = f"images/uploads/{now.strftime('%Y/%m')}"
    abs_path = os.path.join(os.getcwd(), rel_path)
    os.makedirs(abs_path, exist_ok=True)
    
    # 画像の抽出 (3通目以降)
    image_paths = []
    for msg in replies[2:]:
        if "files" in msg:
            for file in msg["files"]:
                ext = os.path.splitext(file["name"])[1]
                file_name = f"{EVENT_NAME}_{len(image_paths)+1}{ext}"
                save_path = os.path.join(abs_path, file_name)
                
                # ダウンロード
                res_img = requests.get(file["url_private_download"], 
                                      headers={"Authorization": f"Bearer {SLACK_TOKEN}"})
                with open(save_path, "wb") as f:
                    f.write(res_img.content)
                
                image_paths.append(f"/{rel_path}/{file_name}")

    if not image_paths:
        image_paths = ["/images/default.jpg"]

    # 2段組み（cols.html）用のリスト生成
    col1_list = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 == 0]
    col2_list = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 != 0]

    def generate_md(lang, content):
        # Python 3.10制約回避：f-stringの外で結合を行う
        col1_text = "\n".join(col1_list)
        col2_text = "\n".join(col2_list)
        
        title_line = jp_body.splitlines()[0] if lang == 'jp' else EVENT_NAME.replace("-", " ").capitalize()
        # タイトル行以外を本文にする（日本語版のみ）
        main_content = "\n".join(content.splitlines()[1:]) if lang == 'jp' else content
        
        template = f"""---
title: "{title_line}"
author: aislab_webstaff
lang: {lang}
image: {image_paths[0]}
tags: event
---
{main_content}

{{% capture col1 %}}
{col1_text}
{{% endcapture %}}

{{% capture col2 %}}
{col2_text}
{{% endcapture %}}

{{% include cols.html col1=col1 col2=col2 %}}
"""
        # _i18n/jp/_posts/ および _i18n/en/_posts/ への書き出し
        file_path = f"_i18n/{lang}/_posts/{date_str}-{EVENT_NAME}.md"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template)
            print(f"Created: {file_path}")

    generate_md("jp", jp_body)
    generate_md("en", en_body)

if __name__ == "__main__":
    create_post()
