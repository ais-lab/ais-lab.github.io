import os
import requests
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 環境変数の取得
SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]
THREAD_TS_RAW = os.environ["THREAD_TS"]  # "Feb 19, 2026, 1:24:13 PM" 形式
EVENT_NAME = os.environ.get("EVENT_NAME", "new-event").replace(" ", "-")

client = WebClient(token=SLACK_TOKEN)

def convert_ts(ts_str):
    """人間が読みやすい日時文字列をUNIXタイムスタンプに変換する"""
    try:
        # Slackの標準的なフォーマット "Feb 19, 2026, 1:24:13 PM" を想定
        dt_obj = datetime.strptime(ts_str, "%b %d, %Y, %I:%M:%S %p")
        return str(dt_obj.timestamp())
    except ValueError:
        print(f"警告: タイムスタンプの変換に失敗しました ({ts_str})。そのまま試行します。")
        return ts_str

def create_post():
    # 1. タイムスタンプの変換とスレッド取得
    thread_ts = convert_ts(THREAD_TS_RAW)
    
    try:
        res = client.conversations_replies(channel=CHANNEL_ID, ts=thread_ts)
        replies = res["messages"]
    except SlackApiError as e:
        print(f"Slack APIエラー: {e.response['error']}")
        return

    # 仕様に基づくメッセージの仕分け
    # replies[0]: 親メッセージ (日本語本文)
    # replies[1]: 返信1件目 (英語本文)
    # replies[2:]: 返信2件目以降 (画像)
    
    jp_body = replies[0]["text"]
    en_body = replies[1]["text"] if len(replies) > 1 else "English content not provided."
    
    # 日付情報の取得
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    rel_path = f"images/uploads/{now.strftime('%Y/%m')}"
    abs_path = os.path.join(os.getcwd(), rel_path)
    os.makedirs(abs_path, exist_ok=True)
    
    # 2. 画像のダウンロード (replies[2]以降を探索)
    image_paths = []
    for msg in replies[2:]:
        if "files" in msg:
            for file in msg["files"]:
                ext = os.path.splitext(file["name"])[1]
                file_name = f"{EVENT_NAME}_{len(image_paths)+1}{ext}"
                save_path = os.path.join(abs_path, file_name)
                
                # ダウンロード実行
                res_img = requests.get(file["url_private_download"], 
                                      headers={"Authorization": f"Bearer {SLACK_TOKEN}"})
                with open(save_path, "wb") as f:
                    f.write(res_img.content)
                
                # Jekyll用パス
                image_paths.append(f"/{rel_path}/{file_name}")

    if not image_paths:
        image_paths = ["/assets/img/default.jpg"] # サイトに存在するデフォルト画像パスを指定

    # 3. カラム生成のロジック (Jekyllのinclude用)
    col1_imgs = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 == 0]
    col2_imgs = [f'{{% include figure.html image="{img}" width="500px" %}}' for i, img in enumerate(image_paths) if i % 2 != 0]

    # 4. Markdown生成関数
    def generate_md(lang, content):
        title_line = jp_body.splitlines()[0] if lang == 'jp' else EVENT_NAME.replace("-", " ").capitalize()
        # 本文からタイトル行を除去
        main_content = "\n".join(content.splitlines()[1:]) if lang == 'jp' else content
        
        # 【修正ポイント】f-stringの外で文字列を結合しておく（Python 3.10制約回避）
        col1_text = "\n".join(col1_imgs)
        col2_text = "\n".join(col2_imgs)
        
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
        # _i18n/jp/_posts/ または _i18n/en/_posts/
        file_path = f"_i18n/{lang}/_posts/{date_str}-{EVENT_NAME}.md"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template)
            print(f"ファイルを作成しました: {file_path}")

    # 日本語版と英語版を生成
    generate_md("jp", jp_body)
    generate_md("en", en_body)

if __name__ == "__main__":
    create_post()
