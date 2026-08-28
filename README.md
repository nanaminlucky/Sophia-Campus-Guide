# Sophia Campus Guide　🦅

上智大学のキャンパス案内、および周辺の飲食店を紹介するアプリケーションです。
大学のPython入門授業の課題の一環として作成しました。

---

## 概要と特徴
- **全学内施設の網羅**: 上智大学のすべての建物をカバーし、写真と一緒に確認できるようにしています。
- **周辺グルメ情報の掲載**: 大学周辺にある飲食店（NO.4、町田商店、デニーズなど）の情報をまとめています。
- **シンプルな操作性**: 誰でも使いやすいよう、文字やボタンを大きめに配置し、絵文字を使って直感的に操作できるように工夫しています。

---

## 使用技術
- **言語・ライブラリ**: Python 3 / Gradio
- **データ**: 各施設の写真データ（`static/images/` フォルダ内）
- **バージョン管理**: Git / GitHub

---

## 動かし方

### 1. ローカル環境（自分のPC）で動かす場合
1. リポジトリをクローンし、仮想環境を有効化してライブラリをインストールします。
   ```bash
   git clone git@github.com:nanaminlucky/Sophia-Campus-Guide.git
   cd Sophia-Campus-Guide
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. アプリケーションを起動します。
   ```bash
   python "Sophia Campus Guide.py"
   ```
3. ブラウザで `http://127.0.0.1:7860` にアクセスすると動作します。

### 2. 他の人にURLで共有する場合
コード内で `launch(share=True)` を設定して起動すると、ターミナルに **`https://gradio.live`** という公開URLが一時的（72時間）に自動発行されます。そのURLを伝えることで、他の人のブラウザからも直接アプリを動かすことができます。
