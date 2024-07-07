import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from serializer.models import Video, Maker, Tag, Label, Series


import pykakasi

def convert_to_romaji(text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")        # Hiragana to ascii
    kakasi.setMode("K", "a")        # Katakana to ascii
    kakasi.setMode("J", "a")        # Japanese to ascii
    kakasi.setMode("r", "Hepburn")  # use Hepburn Roman table
    kakasi.setMode("s", True)       # add space
    kakasi.setMode("C", False)      # no capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)
    return result



#4 各種リスト
import requests
from bs4 import BeautifulSoup





productnumber_info = "midv00394"
url = f"https://www.dmm.co.jp/digital/videoa/-/detail/=/cid={productnumber_info}/"
# url = f"https://www.dmm.co.jp/digital/videoa/-/actress/recommend/"
# url="https://www.dmm.co.jp/digital/videoa/-/maker/"
# url="https://www.dmm.co.jp/digital/videoa/-/series/=/sort=ranking/"



# url = "https://www.dmm.co.jp/digital/videoa/-/maker/"

session = requests.Session()
session.cookies.set("age_check_done", "1")

response = session.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")




import json


# GET_VIDEOS１

import re
import datetime

def get_duration_info(text):
    duration_info = int(re.search(r'\d+', text).group())
    hours = str(duration_info // 60)
    remaining_minutes = str(duration_info % 60)
    duration_info = f"{hours}:{remaining_minutes}:00"
    return duration_info


# ■■■■■■■■■１■■■■■■■■
id_info = None
performers_info = soup.find(attrs={"data-i3pst": "info_actress"}).get_text()
maker_info = soup.find(attrs={"data-i3pst": "info_maker"}).get_text()
label_info = soup.find(attrs={"data-i3pst": "info_label"}).get_text()
series_info = None
# tags_info = soup.find(attrs={"data-i3pst": "info_genre"}).get_text() 　※複数あり、処理が必要
tags_info = None
duration_info = get_duration_info(soup.find(text='収録時間：').find_parent('td').find_next_sibling().get_text().strip())
producturl_info = f"https://www.dmm.co.jp/digital/videoa/-/detail/=/cid={productnumber_info}/"
productimage_info = None
images_ifno = "a,b,c,d"
title_info = soup.title.get_text().strip().split(" - []")[0]
productnumber_info = productnumber_info
description_info = "記事"
views_info = "0"
kyounuki_post_day_info = datetime.datetime.today().date().strftime("%Y-%m-%d")
active_ifno ="true"
thumbnails = []
issue_info = soup.find(text='商品発売日：').find_parent('td').find_next_sibling().get_text().strip().replace(r'/', '-')


# ■■■■■■■■■２■■■■■■■■■
# type属性が"application/ld+json"の<script>タグを見つける
script_tag = soup.find('script', attrs={'type': 'application/ld+json'})

# <script>タグの中のJSONデータを抽出する
json_str = script_tag.string.strip()
json_data = json.loads(json_str)

# 取得したいキーを指定して値を取得
product_name = json_data["name"]
product_image = json_data["image"]
product_sumple = json_data["subjectOf"]["contentUrl"]
product_thumbnail = json_data["subjectOf"]["thumbnailUrl"]
product_description = json_data["description"]
product_sku = json_data["sku"]
product_brand_name = json_data["brand"]["name"]
product_actor_name = json_data["subjectOf"]["actor"]["name"]
product_actor_name_eng = json_data["subjectOf"]["actor"]["alternateName"]
product_actor_name_eng = convert_to_romaji(product_actor_name_eng)
product_actor_genre = json_data["subjectOf"]["genre"]


maker_instance = None
label_instance = None
series_instance = None
if maker_info != None:
    maker_instance = Maker.objects.get(name=maker_info).pk
if label_info != None:
    print("label_info", label_info)
    label_instance = Label.objects.get(name=label_info).pk
if series_info != None:
    print("series_info", series_info)
    series_instance = Series.objects.get(name=series_info).pk




import json
json_str = json.dumps({
#     "id": 1,
    "performers": performers_info,
    "maker": maker_instance,
    "label": label_instance,
    "series": series_instance,
    "tags": None,
    "duration": duration_info,
    "producturl": producturl_info,
    "productimage": product_image,
    "productsumple": product_sumple,
    "productthumbnail": product_thumbnail,
    "images": "['https://picsum.photos/200/300', 'https://picsum.photos/200/300', 'https://picsum.photos/200/300', 'https://picsum.photos/200/300']",
    "title": product_name,
    "productnumber": productnumber_info,
    "description": description_info,
    "views": views_info,
    "kyounuki_post_day": kyounuki_post_day_info,
    "active": True,
    "thumbnails": [],
    "issue": issue_info
}, indent=4, ensure_ascii=False)

# JSON形式の文字列に変換
# json_str = json.dumps(data, indent=4, ensure_ascii=False)

# データを表示
print(json_str)

# JSON文字列を辞書に変換
data_dict = json.loads(json_str)

# 新しいオブジェクトを作成して保存する
new_object = Video.objects.create(**data_dict)
print(new_object)
time.sleep(10)
