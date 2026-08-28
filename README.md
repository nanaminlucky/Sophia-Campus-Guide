# Sophia Campus Guide

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

## ローカル環境での動かし方

### 1. リポジトリのクローン
```bash
git clone git@github.com:nanaminlucky/Sophia-Campus-Guide.git
cd Sophia-Campus-Guide
```

### 2. 仮想環境の作成と有効化
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 4. アプリケーションの起動
```bash
python "Sophia Campus Guide.py"
```
起動後、ブラウザで `http://127.0.0.1:7860` などの指定されたアドレスにアクセスすると動作します。

