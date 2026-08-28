

# Pythonアプリケーション開発
# 「Sophia Campus Guide ～四ツ谷を歩こう！〜」

import gradio as gr

# ==========================================================
# 建物データ
# ==========================================================

BUILDINGS = {

    "1号館": {
        "images": [
            "images:1_1.jpg",
            "images:1_2.jpg",
            "images:1_3.jpg"
        ],
        "description": "上智で1番古い建物。上智大学といえばこの建物！1932年に建てられた歴史ある校舎で、卒業式にはみんなここで写真を撮ります！🎓 前の『Sテラス』は学生の待ち合わせスポット！オープンキャンパスでも記念写真を撮る人が多いですよ📸"
    },

    "2号館": {
        "images": [
            "images:2_1.jpg",
            "images:2_2.jpg",
            "images:2_3.jpg",
            "images:2_4.jpg",
            "images:2_5.jpg",
            "images:2_6.jpg"
        ],
        "description": "『困ったらとりあえず2号館！』と言われるくらい学生がお世話になる建物です😊 学生センターやキャリアセンターなどの窓口が集まっています。地下には紀伊國屋書店があり、本や文房具を学生価格で購入できます！奥にはパティネスポーツもあり、上智生おなじみのソジャーや大学オリジナルグッズも販売しています"
    },

    "3号館・4号館": {
        "images": [
            "images:34_1.jpg",
            "images:34_2.jpg"
        ],
        "description": "理工学部の実験室や教室がある建物です！"
    },

    "6号館": {
        "images": [
            "images:6_1.jpg",
            "images:6_2.jpg",
            "images:6_3.jpg",
            "images:6_4.jpg",
            "images:6_5.jpg"
        ],
        "description": "とても新しくて綺麗な建物です！✨特にトイレの綺麗さにはびっくりすると思うので、ぜひ使ってみてください（笑）多くの授業がここで行われており、誰もが一度は使うことになる建物だと思います！"
    },

    "7号館": {
        "images": [
            "images:7_1.jpg",
            "images:7_2.jpg"
        ],
        "description": "神学部や文学部研究室があり、ゼミなどでよく使われます。メインストリートを跨ぐように立てられている印象的な建物です！"
    },

    "8号館": {
        "images": [
            "images:8_1.jpg",
            "images:8_2.jpg"
        ],
        "description": "理工学部の研究室があります！一階外の8号館ピロティ（通称：8ピロ）はよく、待ち合わせや昼食、外の空気にあたりながらの作業などに使う上智生が多いです！"
    },

    "9号館": {
        "images": [
            "images:9_1.jpg",
            "images:9_2.jpg",
            "images:9_3.jpg",
            "images:9_4.jpg"
        ],
        "description": "地下にある9カフェは、プロント併設でコーヒーやパスタを楽しめます！居心地が良く、ここで友人と一緒に喋ったり、課題をやったりすることもできます☺️一階には中庭もあり、お昼休みにベンチでランチを楽しむ学生もいます🌿"
    },

    "10号館": {
        "images": [
            "images:10_1.jpg",
            "images:10_2.jpg"
        ],
        "description": "講義やゼミで利用される建物です！建物の前にはザビエルがいます！1階には大きな講堂があり、大人数の授業や講演会が行われることもあります！"
    },

    "11号館": {
        "images": [
            "images:11_1.jpg",
            "images:11_2.jpg"
        ],
        "description": "1番奥にある建物で、授業やサークル活動などでよく使われています！北門や正門からは少し距離があるため、遅刻には要注意です！😅地下には、食堂や音楽室もあり、音楽系のサークルに入った人は必ず使うことになるでしょう！"
    },

    "12号館": {
        "images": [
            "images:12_1.jpg",
            "images:12_2.jpg"
        ],
        "description": "地下には学生の強い味方『セブン-イレブン』があります🍙✨ お昼時は混むので、覚悟が必要です（笑）イートインスペースもあるので、お昼ご飯や課題をする学生でいつもにぎわっています！1階にはアドミッションズオフィスがあり、入試相談もできます！"
    },

    "13号館": {
        "images": [
            "images:13_1.jpg",
            "images:13_2.jpg",
            "images:13_3.jpg",
            "images:13_4.jpg"
        ],
        "description": "あまり使ったことのない学生も多いですが、『紀尾井亭』という和風なお屋敷があります。茶道部が使用しているみたいです！🍵"
    },

    "14号館": {
        "images": [
            "images:14_1.jpg",
            "images:14_2.jpg",
            "images:14_3.jpg",
            "images:14_4.jpg"
        ],
        "description": "研究室がある建物で、ゼミで使うこともあります。なんと昔は修道院だったとか！"
    },

    "15号館": {
        "images": [
            "images:15_1.jpg",
            "images:15_2.jpg",
            "images:15_3.jpg"
        ],
        "description": "木のぬくもりを感じられる新しい建物🌳 1階にはスターバックスがあり、授業前後に立ち寄る学生もたくさん！☕️一般の方も利用できます☕"
    },

    "体育館": {
        "images": [
            "images:gym_1.jpg",
            "images:gym_2.jpg",
            "images:gym_3.jpg"
        ],
        "description": "体育の授業や部活動で利用されます！地下には25mプールもあります！"
    },

    "ホフマン・ホール": {
        "images": [
            "images:hoffmann_1.jpg",
            "images:hoffmann_2.jpg",
            "images:hoffmann_3.jpg",
            "images:hoffmann_4.jpg",
            "images:hoffmann_5.jpg"
        ],
        "description": "サークル活動の中心となる建物で、部室がたくさんあります！トレーニングルームやハラルデリという本場カレーの学食もあり、放課後は多くの学生でにぎわいます😊"
    },

    "中央図書館・総合研究棟": {
        "images": [
            "images:library_1.jpg",
            "images:library_2.jpg",
            "images:library_3.jpg",
            "images:library_4.jpg",
            "images:library_5.jpg"
        ],
        "description": "上智生の最強勉強スポット📚 約110万冊の蔵書があり、自習スペースやグループ学習室も充実！テスト前は席が埋まりやすいので、早めに行くのがおすすめです！"
    },

    "クルップ・ホール／マシン・ホール": {
        "images": [
            "images:krupp_1.jpg"
        ],
        "description": "コンピュータールームや理系の実習室がある建物💻 プログラミングの授業などで利用されます！"
    },

    "上智紀尾井坂ビル": {
        "images": [
            "images:kioizaka_1.jpg",
            "images:kioizaka_2.jpg"
        ],
        "description": "11号館の一階から奥に向かってつながっている建物で、こちらも授業やサークル活動でよく使われます！1番奥のエレベーターで地下3階に降りると、外に出ることもでき、出てすぐの場所にセブンイレブンがあります！"
    },

    "真田堀運動場": {
        "images": [
            "images:sanada_1.jpg",
            "images:sanada_2.jpg",
            "images:sanada_3.jpg",
            "images:sanada_4.jpg",
            "images:sanada_5.jpg"
        ],
        "description": "四ツ谷駅のすぐ近くとは思えない広いグラウンド⚽ 野球・サッカー・ラクロスなど、多くの体育会クラブが練習しています！真田堀の並木道はとても心地よい散歩ルートで、卒業・入学のシーズンには桜が満開に咲き誇ります🌸ずっと歩いて行くと、ホテルニューオータニに着きます！"
    }

}
# ==========================================================
# 建物を表示する関数
# ==========================================================

def show_map(building):

    # 建物が選択されていない場合
    if building is None:
        return [], ""

    info = BUILDINGS[building]

    # 画像3枚
    images = info["images"]
    # 画像パスを正規化
    normalized = []
    for img in images:
        if isinstance(img, str) and img.startswith("images:"):
            normalized.append(img.replace("images:", "static/images/"))
        elif isinstance(img, str) and not (img.startswith("http") or img.startswith("static/")):
            normalized.append("static/images/" + img)
        else:
            normalized.append(img)
    images = normalized

    # 説明
    description = info["description"]

    return images, description

# ==========================================================
# 四ツ谷グルメ データベース
# ==========================================================

GOURMET = {

    # ------------------------------------------------------
    # ラーメン
    # ------------------------------------------------------

    "ラーメン": {

        "四谷商店（町田商店）": {

            "image": "yotsuya_shoten.jpg",

            "description":
            "上智生にも人気の家系ラーメン！授業終わりにガッツリ食べたい日におすすめ🍜 ライス無料サービスの日もあります！",

            "menu": "ラーメン",

            "price": "900〜1200円",

            "walk": "上智大学から徒歩4分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=町田商店店"
        },

        "立喰いらぁめん たいせい": {

            "image": "taisei.jpg",

            "description":
            "立ち食いのガッツリ家系ラーメン！体育会系におすすめ💪",

            "menu": "特選らぁめん",

            "price": "1300円",

            "walk": "上智大学から徒歩5分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=立喰いらぁめんたいせい"
        }

    },



    # ------------------------------------------------------
    # ランチ
    # ------------------------------------------------------

    "ランチ": {

        "さち福や": {

            "image": "sachifukuya.jpg",

            "description":
            "健康的な和食が食べたくなったらここ！小鉢の充実した定食はご飯おかわり自由！！🍚一人でも入りやすい人気店です☺️",

            "menu": "たっぷり野菜の和風おろしハンバーグ定食、卵焼き",

            "price": "1200〜1700円",

            "walk": "上智大学から徒歩6分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=さち福や コモレ四谷店"
        },

        "デニーズ": {

            "image": "dennys.jpg",

            "description":
            "上智生御用達のファミレス！課題やテスト勉強でも利用する学生がたくさんいます📚豪華なパフェはぜひ一度食べてほしい！",

            "menu": "デミグラスハンバーグ、パフェ",

            "price": "800〜1600円",

            "walk": "上智大学から徒歩4分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=デニーズ 二番町店"
        },

        "ムンバイ": {

            "image": "mumbai.jpg",

            "description":
            "本格インドカレーのお店！日替わりのランチセットが人気です🍛じつは、1階と2階で違う地域のインド料理を出しているみたいです！インド風アフタヌーンティーもやってるとか？",

            "menu": "バターチキンカレー🍛",

            "price": "1000〜1500円",

            "walk": "上智大学から徒歩5分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=ムンバイ 四谷"
        },

        "中国菜酒 蜀留香": {

            "image": "shuryuka.jpg",

            "description":
            "本格四川料理が楽しめます！意外と知られていませんが、店内もカラフルな提灯が綺麗で、ランチセットもとても美味しくてそんなに高くない！辛いもの好きはもちろんそうでない学生にもぜひおすすめしたいお店🌶",

            "menu": "麻婆豆腐",

            "price": "1000〜1500円",

            "walk": "上智大学から徒歩5分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=蜀留香 四谷"
        },

        "Saci Perere": {

            "image": "saci.jpg",

            "description":
            "ブラジル料理のお店🇧🇷 ボリューム満点なので、お腹いっぱい食べたい日にぴったり！",

            "menu": "シュラスコ",

            "price": "1200〜2000円",

            "walk": "上智大学から徒歩7分",

            "recommend": "★★★★☆",

            "map": "https://maps.google.com/?q=Saci Perere 四谷"
        },

        "すぱじろう": {

            "image": "supajiro.jpg",

            "description":
            "種類豊富なスパゲッティ専門店🍝 パスタ好きなら一度は行ってみてほしい人気店です！",

            "menu": "ペペロンチーノ",

            "price": "1000〜1500円",

            "walk": "上智大学から徒歩5分",

            "recommend": "★★★★☆",

            "map": "https://maps.google.com/?q=すぱじろう 四谷"
        },

        "PIZZA SALVATORE CUOMO 四谷": {

            "image": "salvatore.jpg",

            "description":
            "石窯で焼いた本格ナポリピザが人気🍕 友達とシェアしながら食べるのもおすすめ！",

            "menu": "マルゲリータ",

            "price": "1500〜2500円",

            "walk": "上智大学から徒歩6分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=PIZZA SALVATORE CUOMO 四谷"
        },

        "Trattoria Mar": {

            "image": "mar.jpg",

            "description":
            "おしゃれなイタリアンレストラン！ランチでもディナーでも人気があります✨上智生がよくアルバイトをしています！",

            "menu": "日替わりパスタ",

            "price": "1200〜1800円",

            "walk": "上智大学から徒歩7分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=Trattoria Mar 四谷"
        },

        "かつれつたけだ": {

            "image": "takeda.jpg",

            "description":
            "四ツ谷を代表する人気店！行列ができることも多いですが、その分おいしさは間違いなし✨",

            "menu": "ポークカツレツ",

            "price": "1500〜2500円",

            "walk": "上智大学から徒歩8分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=かつれつたけだ"
        }

    },



    # ------------------------------------------------------
    # カフェ・スイーツ
    # ------------------------------------------------------

    "カフェ・スイーツ": {

        "COMODO Cafe": {

            "image": "comodo.jpg",

            "description":
            "迎賓館の前にある、吹き抜けになっている地下のカフェです✨あまり知られていませんが、心地よい日差しと、迎賓館の優雅さを味わえるおすすめスポットです😉お茶をした後に、ぜひ迎賓館の庭を散歩してみてください！🏰",

            "menu": "サラダやパスタ、デザートなど各種",

            "price": "1000〜1500円",

            "walk": "上智大学から徒歩5分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=COMODO Cafe 四谷"
        },

        "Lawn": {

            "image": "lawn.jpg",

            "description":
            "四谷駅の老舗純喫茶 70年近く喫茶店を営むコーヒー・ロン。 温かみのあるレトロな喫茶店。 喫煙可能。🚬",

            "menu": "名物のたまごサンド¥850、コーヒーフロート¥850",

            "price": "1000〜1600円",

            "walk": "上智大学から徒歩2分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=Lawn 四谷"
        },

        "Paul": {

            "image": "paul.jpg",

            "description":
            "フランス発の人気ベーカリー🥐 焼きたてパンやケーキのセット、カヌレなどが楽しめます！朝ごはんにもおすすめ。中にあるレストランではちょっといいランチやデザートセットを楽しめます✨",

            "menu": "クロワッサン、カヌレなど",

            "price": "500〜1500円",

            "walk": "上智大学から徒歩3分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=PAUL 四谷"
        },

        "No.4": {

            "image": "no4.jpg",

            "description":
            "行列のできる超人気カフェ！フレンチトーストやパンが有名で、休日は特に賑わっています🥞開放感がありおしゃれで、ランチもカフェ利用も人気！ゆったり過ごしたい日におすすめです。",

            "menu": "フレンチトースト",

            "price": "1200〜2000円",

            "walk": "上智大学から徒歩12分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=No.4 千代田区"
        },

        "サンマルクカフェ": {

            "image": "saintmarc.jpg",

            "description":
            "チョコクロで有名な定番カフェ🍫 気軽に入りやすく、勉強や待ち合わせにもよく利用されています。上智生は学生証を見せると1割引になります！🙌",

            "menu": "チョコクロ",

            "price": "500〜1200円",

            "walk": "上智大学から徒歩3分",

            "recommend": "★★★★☆",

            "map": "https://maps.google.com/?q=サンマルクカフェ 四谷"
        },

        "星乃珈琲店 コモレ四谷店": {

            "image": "hoshino.jpg",

            "description":
            "落ち着いた雰囲気が魅力のチャーンの喫茶店☕ スフレパンケーキが美味しいです☺️ ",

            "menu": "スフレパンケーキ、コーヒー",

            "price": "800〜1800円",

            "walk": "上智大学から徒歩5分",

            "recommend": "★★★★☆",

            "map": "https://maps.google.com/?q=星乃珈琲店 コモレ四谷"
        },


        "TIGRATO Gelateria & Cafe Bar": {

            "image": "tigrato.jpg",

            "description":
            "ジェラートが人気のおしゃれカフェ🍨 夜はバーとしても営業しています。",

            "menu": "ジェラート",

            "price": "600〜1500円",

            "walk": "上智大学から徒歩6分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=TIGRATO 四谷"
        },

        "いーぐる": {

            "image": "eagle.jpg",

            "description":
            "全国的にも有名なジャズ喫茶🎷 落ち着いた空間でゆっくりコーヒーを楽しめます。",

            "menu": "ブレンドコーヒー",

            "price": "700〜1200円",

            "walk": "上智大学から徒歩4分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=いーぐる 四谷"
        },


        "たい焼き わかば": {

            "image": "wakaba.jpg",

            "description":
            "四ツ谷と言えばここ！🐟 行列ができることもある超人気たい焼き店です。あんこも生地も自家製にこだわり、一匹ずつ丁寧に焼いています。 薄い生地の皮の中は頭からしっぽまでつぶしあんがぎっしり!!焼きたては絶品です！",

            "menu": "たい焼き",

            "price": "210円",

            "walk": "上智大学から徒歩5分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=たい焼き わかば"
        }

    },



    # ------------------------------------------------------
    # 観光スポット
    # ------------------------------------------------------

    "観光": {

        "迎賓館赤坂離宮": {

            "image": "geihinkan.jpg",

            "description":
            "日本で唯一のネオ・バロック様式の宮殿建築✨ 建物は西洋のお城そのもので、まるで海外の貴族になったかのような気分になれます🏰👸オープンキャンパスの帰りに立ち寄るのもおすすめです！",

            "menu": "見学",

            "price": "一般公開日は見学料あり",

            "walk": "上智大学から徒歩10分",

            "recommend": "★★★★★",

            "map": "https://maps.google.com/?q=迎賓館赤坂離宮"
        }

    }

}
# ======================================================k
# 店舗情報を表示する
# ======================================================

def show_gourmet(category, shop):

    if category is None or shop is None:
        return None, ""

    info = GOURMET[category][shop]

    text = f"""

# 🍽 {shop}

## ⭐ おすすめ度

### {info["recommend"]}

---

## 🍜 おすすめメニュー

**{info["menu"]}**

---

## 💰 予算

**{info["price"]}**

---

## 🚶 上智大学から

**{info["walk"]}**

---

## 💬 上智生コメント

> {info["description"]}

---

## 📍 Google Map

<a href="{info["map"]}" target="_blank">

🌍 Google Mapで見る

</a>

"""

    image = info["image"]
    if isinstance(image, str) and not (image.startswith("http") or image.startswith("static/")):
        image = "static/images/" + image
    return image, text

# ======================================================
# ジャンル変更時に店舗一覧を更新
# ======================================================

def update_shop(category):

    if category is None:
        return gr.update(
            choices=[],
            value=None
        )

    return gr.update(
        choices=list(GOURMET[category].keys()),
        value=None
    )

# ==========================================================
# GUI作成
# ==========================================================

# Blocks()
# アプリ全体を作る
with gr.Blocks() as demo:

    # タイトル
    gr.Markdown("# 🦅 Sophia Campus Guide 🎓")
    gr.Markdown("### オープンキャンパスへようこそ！")


    # ======================================================v
    # タブ① キャンパスマップ
    # ======================================================

    with gr.Tab("🏫 キャンパスマップ"):

        gr.Markdown("## 上智大学キャンパスマップ")

        # キャンパス全体の地図を表示
        campus_map = gr.Image(
            value="static/images/campus_map.jpg",
            label="キャンパスマップ",
            interactive=False   # ユーザーは画像を変更できない
        )

        # 建物をラジオボタンで選択
        building = gr.Radio(
              choices=list(BUILDINGS.keys()),
              label="建物を選択してください"
        )

        # 表示ボタン
        map_button = gr.Button("表示")

        # 建物の写真を3枚表示するギャラリー
        map_image = gr.Gallery(
            label="建物写真",
            columns=3,
            rows=1,
            height=250
        )

        # 建物説明
        map_text = gr.Textbox(
            label="建物説明"
        )

        # ボタンを押したらshow_map()を実行
        map_button.click(
            fn=show_map,
            inputs=building,
            outputs=[map_image, map_text]
        )
    # ======================================================
    # タブ② 四ツ谷グルメ
    # ======================================================

    with gr.Tab("🍴 四ツ谷グルメ"):

        gr.Markdown("""
        # 🍴 四ツ谷グルメ

        ### 上智大学周辺のおすすめグルメをご紹介！

        授業終わりやランチに人気のお店を、
        現役上智生目線でまとめました😊

        気になるお店を選んでみてください！
        """)

        # -----------------------
        # ジャンル
        # -----------------------

        category = gr.Radio(

            choices=[
                "カフェ・スイーツ",
                "ランチ",
                "ラーメン",
                "観光"
            ],

            label="ジャンル"
        )

        # -----------------------
        # 横並びレイアウト
        # -----------------------

        with gr.Row():

            # ==========================k
            # 左側（店舗一覧）
            # ==========================

            with gr.Column(scale=1):

                gr.Markdown("## 🏪 店舗一覧")

                shop = gr.Radio(
                    choices=[],
                    label="お店を選択してください"
                )

            # ==========================カラー
            # 右側（店舗詳細）
            # ==========================

            with gr.Column(scale=3):

                gourmet_image = gr.Image(
                    height=500,
                    label="📷 店舗写真"
                )

                gourmet_text = gr.Markdown()

    # -----------------------
    # ジャンル変更
    # -----------------------

    category.change(

        fn=update_shop,

        inputs=category,

        outputs=shop

    )

    # -----------------------
    # 店舗変更
    # -----------------------

    shop.change(

        fn=show_gourmet,

        inputs=[category, shop],

        outputs=[gourmet_image, gourmet_text]

    )

# アプリを起動
demo.launch(share=True)