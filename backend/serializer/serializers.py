from rest_framework import serializers
from .models import Video, Performer, Maker, Label, Series, Tag, Article, Article_tag, Article_child
# from .models import Thumbnail, Kyounuki, Test, Contents, ContentsTag
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps
import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db.models import Q
import pandas as pd

import ast

import re
import json
import requests
from bs4 import BeautifulSoup

import pykakasi


from asgiref.sync import sync_to_async
from django.forms.models import model_to_dict


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

def get_duration_info(text):
    duration_info = int(re.search(r'\d+', text).group())
    hours = str(duration_info // 60)
    remaining_minutes = str(duration_info % 60)
    duration_info = f"{hours}:{remaining_minutes}:00"
    return duration_info

def calculate_age(birth_date):
    today = datetime.datetime.now()
    birth_year = birth_date.year
    birth_month = birth_date.month
    birth_day = birth_date.day

    age = today.year - birth_year

    if (today.month < birth_month) or (today.month == birth_month and today.day < birth_day):
        age -= 1

    return age


# ■■■■■■■■■■■■■■■■■■
# ■■■　Performer　■■■
# ■■■■■■■■■■■■■■■■■■
class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'
class GetPerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ["id", "name", "name_eng", "birth", "age"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
class CreatePerformerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, read_only=True)
    birth = serializers.CharField(required=False, read_only=True)
    age = serializers.CharField(required=False, read_only=True)
    name_eng = serializers.CharField(required=False, read_only=True)
    def create(self, validated_data):
        birth_info = validated_data.get('birth')
        age = calculate_age(birth_info)
        validated_data["age"] = age
        performer = Performer.objects.create(**validated_data)
        return performer
    class Meta:
        model = Performer
        fields = '__all__'



# ■■■■■■■■■■■■■■■■■■
# ■■■　Tag　■■■
# ■■■■■■■■■■■■■■■■■■
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class GetTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    
# ■■■■■■■■■■■■■■■■■■
# ■■■　Maker　■■■
# ■■■■■■■■■■■■■■■■■■
class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = '__all__'
    def create(self, validated_data):
        name_data = validated_data.pop('name', None)
        name_eng_data = validated_data.pop('name_eng', None)
        if name_eng_data != "": 
            validated_data["name_eng"] = name_eng_data
        else:
            name_eng_data = convert_to_romaji(name_data).lower()
            validated_data["name_eng"] = name_eng_data
            validated_data["name"] = name_data
        create_obj = Maker.objects.create(**validated_data)
        return create_obj
class GetMakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")

# ■■■■■■■■■■■■■■■■■■
# ■■■　Label　■■■
# ■■■■■■■■■■■■■■■■■■
class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
    def create(self, validated_data):
        name_data = validated_data.pop('name', None)
        name_eng_data = validated_data.pop('name_eng', None)
        if name_eng_data != "": 
            validated_data["name_eng"] = name_eng_data
        else:
            name_eng_data = convert_to_romaji(name_data).lower()
            validated_data["name_eng"] = name_eng_data
            validated_data["name"] = name_data
        create_obj = Maker.objects.create(**validated_data)
        return create_obj
class GetLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")

# ■■■■■■■■■■■■■■■■■■
# ■■■　Series　■■■
# ■■■■■■■■■■■■■■■■■■
class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'
    def create(self, validated_data):
        name_data = validated_data.pop('name', None)
        name_eng_data = validated_data.pop('name_eng', None)
        if name_eng_data != "": 
            validated_data["name_eng"] = name_eng_data
        else:
            name_eng_data = convert_to_romaji(name_data).lower()
            validated_data["name_eng"] = name_eng_data
            validated_data["name"] = name_data
        create_obj = Maker.objects.create(**validated_data)
        return create_obj
class GetSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")

# ■■■■■■■■■■■■■■■■■■
# ■■■　Thumnails　■■■
# ■■■■■■■■■■■■■■■■■■
# class ThumbnailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Thumbnail
#         fields = '__all__'
# class GetThumbnailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Thumbnail
#         fields = '__all__'
#     def create(self, validated_data):
#         # レコード作成を禁止するため、何も処理せずに例外を発生させます
#         raise serializers.ValidationError("Creating records is not allowed.")


# class TestSerializer(serializers.ModelSerializer):
#     # maker = MakerSerializer()
#     maker = serializers.CharField(max_length=255)
#     def create(self, validated_data):
#         print("validated_data", validated_data)


#         maker_data = validated_data.pop('maker', None)
#         if maker_data:
#             try:
#                 maker = Maker.objects.get(name=maker_data)
#             except Maker.DoesNotExist:
#                 raise serializers.ValidationError('Maker does not exist.')
#             validated_data['maker'] = maker
        

#         return Test.objects.create(**validated_data)
 
#     class Meta:
#         model = Test
#         fields = '__all__'




# ■■■■■■■■■■■■■■■■■■
# ■■■　URL　■■■
# ■■■■■■■■■■■■■■■■■■
class UrlPerformerSerializer(serializers.ModelSerializer):
    class Meta: model = Performer; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlTagSerializer(serializers.ModelSerializer):
    class Meta: model = Tag; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlMakerSerializer(serializers.ModelSerializer):
    class Meta: model = Maker; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlLabelSerializer(serializers.ModelSerializer):
    class Meta: model = Label; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlSeriesSerializer(serializers.ModelSerializer):
    class Meta: model = Series; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
# class UrlKyounukiSerializer(serializers.ModelSerializer):
#     class Meta: model = Kyounuki; fields = ['post_day']
    # def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlVideoSerializer(serializers.ModelSerializer):
    class Meta: model = Video; fields = ['video_productnumber']
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
# class GetUrlSerializer(serializers.Serializer):
#     video = UrlVideoSerializer(many=True)
#     performer = UrlPerformerSerializer(many=True)
#     tag = UrlTagSerializer(many=True)
#     maker = UrlMakerSerializer(many=True)
#     label = UrlLabelSerializer(many=True)
#     series = UrlSeriesSerializer(many=True)
#     kyounuki = UrlKyounukiSerializer(many=True)
#     class Meta:
#         fields = '__all__'
#     def create(self, validated_data):
#         # レコード作成を禁止するため、何も処理せずに例外を発生させます
#         raise serializers.ValidationError("Creating records is not allowed.")



# ■■■■■■■■■■■■■■■■■■
# ■■■　Video　■■■
# ■■■■■■■■■■■■■■■■■■
class VideoSerializer(serializers.ModelSerializer):
    performers = serializers.CharField(max_length=255)
    # performers = PerformerSerializer()
    # thumbnails = ThumbnailSerializer()
    maker = serializers.CharField(max_length=255, allow_null=True)
    label = serializers.CharField(max_length=255, allow_null=True)
    series = serializers.CharField(max_length=255, allow_null=True)
    tags = serializers.CharField(max_length=255, allow_null=True)
    duration = serializers.TimeField(format='%H:%M:%S', input_formats=['%H:%M:%S', '%H:%M'], default=datetime.time(0, 0, 0), allow_null=True)
    producturl = serializers.URLField(max_length=200, allow_null=True)
    images = serializers.CharField(max_length=1023)


    def create(self, validated_data):
        # ネストされたフィールドの作成手順を指定
        # performers_data = validated_data.pop('performers', [])

        thumbnails_data = validated_data.pop('thumbnails', [])
        # tags_data = validated_data.pop('tags', [])
        # maker_data = validated_data.pop('maker', None)
        # label_data = validated_data.pop('label', None)
        # series_data = validated_data.pop('series', None)

        # maker_name = maker_data.get('name') if maker_data else None
        # maker = Maker.objects.filter(name=maker_name).first()

        maker_data = validated_data.pop('maker', None)
        obj = self.duplicate_check("maker", maker_data)
        validated_data["maker"] = obj

        label_data = validated_data.pop('label', None)
        obj = self.duplicate_check("label", label_data)
        validated_data["label"] = obj

        series_data = validated_data.pop('series', None)
        obj = self.duplicate_check("series", series_data)
        validated_data["series"] = obj

        tags_data = validated_data.pop('tags', [])
        objs_tags = self.duplicate_check_loop("tag", tags_data)
        # validated_data["tags"] = objs

        performers_data = validated_data.pop('performers', [])
        objs_performers = self.duplicate_check_loop("performer", performers_data)
        # validated_data["performers"] = objs


        images_data = validated_data.pop('images', None)
        print(images_data)
        urls = images_data.split(",")
        objs_images = []
        for url in urls:
            objs_images.append(url)
        validated_data["images"] = objs_images

    

        video = Video.objects.create(**validated_data)

        video.video_tags.set(objs_tags)
        video.video_performers.set(objs_performers)


            

        return video


    # # Check for duplicate data 
    def duplicate_check(self, item, data):
        obj = None
        if data:
            ModelClass = apps.get_model(app_label="serializer", model_name=item)

            if ModelClass.objects.filter(name=data).exists():
                obj = ModelClass.objects.get(name=data)

                print(f"{item}: OK")
            else:
                raise serializers.ValidationError(f"{item.capitalize()} does not exist.")
                print("err")
        return obj
    
    def duplicate_check_loop(self, item, data):
        if ".None" in data:
            raise serializers.ValidationError(f"That {data} value does not exist in the {item.capitalize()} model.")
        objs = []
        obj = None
        err_flag = 0
        err_items = []
        ModelClass = apps.get_model(app_label="serializer", model_name=item)

        for data_item in data.split(","):
            data_item = data_item.strip()
            if data_item:
                ModelClass = apps.get_model(app_label="serializer", model_name=item)
                if ModelClass.objects.filter(name=data_item).exists():
                    obj = ModelClass.objects.get(name=data_item).id
                    print(f"{data_item}: OK")
                    objs.append(obj)
                else:
                    err_items.append(data_item)
                    err_flag=1
        if err_flag == 1:
            raise serializers.ValidationError(f"That {err_items} value does not exist in the {item.capitalize()} model.")
        return objs
    
    # # VALIDATE
    def validate_def(self, attrs, item):
        print("item_data", item, attrs)
        ModelClass = apps.get_model(app_label="serializer", model_name=item)

        # item_name = attrs.get("name", None)
        # print("attrs", item, attrs)
        # print("item_data", item, item_name)
        if attrs:
            # item_name = item_data.get('name')
            if ModelClass.objects.filter(name=attrs).exists():
                print(f"{item}: OK")
            else:
                raise serializers.ValidationError(f"That {attrs} value does not exist in the {item.capitalize()} model.")
        return attrs
    
    def validate_def_loop(self, attrs, item):
        if ".None" in attrs:
            return attrs

        print("item_data", item, attrs)
        ModelClass = apps.get_model(app_label="serializer", model_name=item)
        err_flag=0
        err_items = []
        for attrs_item in attrs.split(","):
            attrs_item = attrs_item.strip()
            if attrs_item:
                # item_name = item_data.get('name')
                print("■", attrs_item)
                if ModelClass.objects.filter(name=attrs_item).exists():
                    print(f"{attrs_item}: OK")
                else:
                    err_items.append(attrs_item)
                    err_flag=1
        if err_flag == 1:
            raise serializers.ValidationError(f"That {err_items} value does not exist in the {item.capitalize()} model.")
        return attrs

    def validate_maker(self, attrs):
        return self.validate_def(attrs, "maker")
    
    def validate_label(self, attrs):
        return self.validate_def(attrs, "label")
    
    def validate_series(self, attrs):
        return self.validate_def(attrs, "series")
    
    def validate_tags(self, attrs):
        return self.validate_def_loop(attrs, "tag")
    
    def validate_performers(self, attrs):
        return self.validate_def_loop(attrs, "performer")
    
    def validate_images(self, attrs):
        urls = attrs.split(",")
        url_validator = URLValidator()
        for url in urls:
            try:
                url_validator(url.strip())
            except ValidationError:
                # URLの形式が正しくない場合の処理
                print("■URL", url)
                raise serializers.ValidationError("Invalid URL format")
            
        return attrs
    
    def update(self, instance, validated_data):
        # バリデーション済みデータでインスタンスを更新します
        maker_data = validated_data.pop('maker', None)
        obj = self.duplicate_check("maker", maker_data)
        validated_data["maker"] = obj

        label_data = validated_data.pop('label', None)
        obj = self.duplicate_check("label", label_data)
        validated_data["label"] = obj

        series_data = validated_data.pop('series', None)
        obj = self.duplicate_check("series", series_data)
        validated_data["series"] = obj

        # tags_data = validated_data.pop('tags', [])
        # objs_tags = self.duplicate_check_loop("tag", tags_data)
        # validated_data["tags"] = objs

        # performers_data = validated_data.pop('performers', [])
        # objs_performers = self.duplicate_check_loop("performer", performers_data)
        # validated_data["performers"] = objs

        # print("instance.performers", instance.performers)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        # instance.performers = validated_data.get('performers', instance.performers)
        instance.maker = validated_data.get('maker', instance.maker)
        instance.label = validated_data.get('label', instance.label)
        instance.series = validated_data.get('series', instance.series)
        # instance.tags = validated_data.get('tags', instance.tags)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.producturl = validated_data.get('producturl', instance.producturl)

        images_data = validated_data.pop('images', [])
        urls = images_data.split(",")
        
        objs_images = []
        for url in urls:
            objs_images.append(url)
            print("objs_images", objs_images)
        # validated_data["images"] = objs_images
        # instance.images = validated_data.get('images', instance.images)
        instance.images = objs_images

        tags_data = validated_data.pop('tags', [])
        tags_data_result = self.duplicate_check_loop("tag", tags_data)
        # validated_data["tags"] = objs

        performers_data = validated_data.pop('performers', [])
        performers_data_result = self.duplicate_check_loop("performer", performers_data)

        instance.tags.set(tags_data_result)
        instance.performers.set(performers_data_result)


        print("instance.tags", instance.tags)
        print("instance.performers", instance.performers)
        # productnumber = validated_data.pop('productnumber', None)
        # videos = Video.objects.filter(productnumber=productnumber)
        # print("aaaaaaaaaaaaaaaaa")
        # if (videos):
        #     get_video, _ = Video.objects.get_or_create(productnumber=productnumber)
        #     if (validated_data["title"] != None) or (validated_data["title"] != []) or (validated_data["title"] != ""):get_video.title = validated_data["title"]
        #     if (validated_data["performers"] != None) or (validated_data["performers"] != []) or (validated_data["performers"] != "") :get_video.performers = validated_data["performers"] 
        #     if (validated_data["productnumber"] != None) or (validated_data["productnumber"] != []) or (validated_data["productnumber"] != "") :get_video.productnumber = validated_data["productnumber"] 
        #     # if (validated_data["maker"] != None) or (validated_data["maker"] != []) or (validated_data["maker"] != "") :get_video.maker = validated_data["maker"] 
        #     if (validated_data["label"] != None) or (validated_data["label"] != []) or (validated_data["label"] != "") :get_video.label = validated_data["label"] 
        #     if (validated_data["series"] != None) or (validated_data["series"] != []) or (validated_data["series"] != "") :get_video.series = validated_data["series"] 
        #     if (validated_data["description"] != None) or (validated_data["description"] != []) or (validated_data["description"] != "") :get_video.description = validated_data["description"] 
        #     if (validated_data["duration"] != None) or (validated_data["duration"] != []) or (validated_data["duration"] != "") :get_video.duration = validated_data["duration"] 
        #     if (validated_data["views"] != None) or (validated_data["views"] != []) or (validated_data["views"] != "") :get_video.views = validated_data["views"] 
        #     if (validated_data["thumbnails"] != None) or (validated_data["thumbnails"] != []) or (validated_data["thumbnails"] != "") :get_video.thumbnails = validated_data["thumbnails"] 
        #     if (validated_data["kyounuki_post_day"] != None) or (validated_data["kyounuki_post_day"] != []) or (validated_data["kyounuki_post_day"] != "") :get_video.kyounuki_post_day = validated_data["kyounuki_post_day"] 
        #     if (validated_data["producturl"] != None) or (validated_data["producturl"] != []) or (validated_data["producturl"] != "") :get_video.producturl = validated_data["producturl"] 
        #     if (validated_data["tags"] != None) or (validated_data["tags"] != []) or (validated_data["tags"] != "") :get_video.tags = validated_data["tags"] 
        #     if (validated_data["active"] != None) or (validated_data["active"] != []) or (validated_data["active"] != "") :get_video.active = validated_data["active"] 
        #     if (validated_data["images"] != None) or (validated_data["images"] != []) or (validated_data["images"] != "") :get_video.images = validated_data["images"] 
        #     get_video.save()
        #     return



        # video.tags.set(objs_tags)
        # video.performers.set(objs_performers)

        # ネストされた関係を更新します
        # self.update_thumbnails(instance, validated_data)

        # 更新したインスタンスを保存します
        instance.save()

        return instance

    class Meta:
        model = Video
        fields = '__all__'






# class UpdateVideoSerializer(serializers.ModelSerializer):
#     # performers = serializers.CharField(max_length=255)
#     performers = GetPerformerSerializer(many=True)
#     # thumbnails = ThumbnailSerializer()
#     maker = GetMakerSerializer()
#     label = GetLabelSerializer()
#     series = GetSeriesSerializer()
#     tags = GetTagSerializer(many=True)
#     duration = serializers.TimeField(format='%H:%M:%S', input_formats=['%H:%M:%S', '%H:%M'], default=datetime.time(0, 0, 0))
#     producturl = serializers.URLField(max_length=200, allow_blank=True)

#     class Meta:
#         model = Video
#         fields = '__all__'
#     def create(self, validated_data):
#         # レコード作成を禁止するため、何も処理せずに例外を発生させます
#         raise serializers.ValidationError("Creating records is not allowed.")

class GetVideoSerializer(serializers.ModelSerializer):
    # performers = serializers.CharField(max_length=255)
    video_performers = GetPerformerSerializer(many=True)
    # thumbnails = ThumbnailSerializer()
    video_maker = GetMakerSerializer()
    video_label = GetLabelSerializer()
    video_series = GetSeriesSerializer()
    video_tags = GetTagSerializer(many=True)
    video_duration = serializers.TimeField(format='%H:%M:%S', input_formats=['%H:%M:%S', '%H:%M'], default=datetime.time(0, 0, 0))
    video_url = serializers.URLField(max_length=200, allow_blank=True)

    class Meta:
        model = Video
        fields = '__all__'
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    




# ■■■■■■■■■■■■■■■■■■
# ■■■　KNK　■■■
# ■■■■■■■■■■■■■■■■■■
# class KyounukiSerializer(serializers.ModelSerializer):
#     post_day = serializers.DateField(format='%Y-%m-%d')
#     class Meta:
#         model = Kyounuki
#         fields = '__all__'

#     def create(self, validated_data):
#         # kyounuki_post_days = validated_data.get('post_day', [])
#         # if not isinstance(kyounuki_post_days, list):
#         #     kyounuki_post_days = [kyounuki_post_days]
#         article = validated_data.get('article')
#         # productnumbers = validated_data.get('productnumbers', [])

#         # videos = Video.objects.filter(kyounuki_post_day=kyounuki_post_day)


#         # kyounukis = []

#         # kyounuki_post_days = Video.objects.values_list('kyounuki_post_day', flat=True).distinct()
#         # for kyounuki_post_day in kyounuki_post_days:
#         #     print("■■■■■■１")

#         #     # Videoモデルをフィルターしてデータを取得
#         #     videos = Video.objects.filter(kyounuki_post_day=kyounuki_post_day)

#         #     # フィルター結果からproductnumberを取得してリストに格納
#         #     if len(videos) > 5:
#         #         raise serializers.ValidationError(f"Creating videos records is not length ({len(videos)}).")

#         #     productnumbers = [video.pk for video in videos]
#         #     # date_str = date_obj.strftime("%Y-%m-%d")


#         #     # Kyounukiモデルを作成してリストに追加
#         #     kyounuki, _ = Kyounuki.objects.get_or_create(
#         #         post_day=kyounuki_post_day, 
#         #         defaults={'article': article})
#         #     kyounuki.article = article
#         #     kyounuki.productnumbers.set(productnumbers)
#         #     kyounuki.save()

#         #     # kyounuki = Kyounuki.objects.create(
#         #     #     post_day=kyounuki_post_day,
#         #     #     article=article
#         #     # )

#         #     kyounukis.append(kyounuki)

#         article = validated_data.get('article')
#         post_day = validated_data.get('post_day')

#         # Videoモデルをフィルターしてデータを取得
#         videos = Video.objects.filter(kyounuki_post_day=post_day)

#         # フィルター結果からproductnumberを取得してリストに格納
#         if len(videos) > 5:
#             raise serializers.ValidationError(f"Creating videos records is not length ({len(videos)}).")

#         productnumbers = [video.pk for video in videos]
#         # date_str = date_obj.strftime("%Y-%m-%d")

#         # Kyounukiモデルを作成してリストに追加
#         kyounuki, _ = Kyounuki.objects.get_or_create(
#             post_day=post_day, 
#             defaults={'article': article})
#         kyounuki.article = article
#         kyounuki.productnumbers.set(productnumbers)
#         kyounuki.save()

#         return kyounuki



# class GetKyounukiSerializer(serializers.ModelSerializer):
#     productnumbers = GetVideoSerializer(many=True, read_only=True)
#     class Meta:
#         model = Kyounuki
#         fields = '__all__'
#     def create(self, validated_data):
#         # レコード作成を禁止するため、何も処理せずに例外を発生させます
#         raise serializers.ValidationError("Creating records is not allowed.")


class UpdateVideoSerializer(serializers.ModelSerializer):
    # video_performers = GetPerformerSerializer(many=True)
    # video_tags = GetTagSerializer(many=True)
    # article_tags = GetArticletagSerializer(many=True)
    # # article_explain = models.CharField(max_length=1023, blank=True, null=True)
    # article_childlen = GetArticlechildSerializer(many=True)


    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    class Meta:
        model = Video
        fields = '__all__'

class CreateVideoSerializer(serializers.ModelSerializer):
    video_title = serializers.CharField(required=False, read_only=True)
    video_performers = serializers.CharField(required=False)
    video_productnumber = serializers.CharField()
    video_maker = serializers.CharField(required=False, read_only=True)
    video_label = serializers.CharField(required=False, read_only=True)
    video_series = serializers.CharField(required=False, read_only=True)
    video_description = serializers.CharField(required=False, read_only=True)
    video_duration = serializers.CharField(required=False, read_only=True)
    video_views = serializers.CharField(required=False, read_only=True)
    # thumbnails = serializers.CharField(required=False, read_only=True)
    # kyounuki_post_day = serializers.CharField(required=False, read_only=True)
    video_url = serializers.CharField(required=False, read_only=True)
    video_image = serializers.CharField(required=False, read_only=True)
    video_images = serializers.CharField(required=False, read_only=True)    
    video_sumple_video = serializers.CharField(required=False, read_only=True)
    # productthumbnail = serializers.CharField(required=False, read_only=True)
    video_tags = serializers.CharField(required=False, read_only=True)
    # active = serializers.CharField(required=False, read_only=True)
    # images = serializers.CharField(required=False, read_only=True)
    video_issue = serializers.CharField(required=False, read_only=True)
    video_affiliateurl = serializers.URLField(required=False, read_only=True)
    def create(self, validated_data):
        productnumber_info = validated_data.get('video_productnumber')
        # Video obj に重複あるか確認。重複していればエラー処理    
        try:
            # データベースから指定のproductnumberでVideoを取得
            existing_video = Video.objects.get(video_productnumber=productnumber_info)
            raise serializers.ValidationError(f"Duplicate data for productnumber='{productnumber_info}'.")
        except Video.DoesNotExist:
            pass

        # performers_info = validated_data.get('video_performers').split(', ')
        # try:
        #     for item in performers_info:
        #         existing_video = Performer.objects.get(name=item)
        #         if existing_video == None:
        #             raise serializers.ValidationError(f"None data for performer='{item}'.")
        # except:pass
                
        video_performers_info = validated_data.get('video_performers').split(',')

        if video_performers_info:
            for item in video_performers_info:
                judge_existence_obj(item, Performer)
        else:
            raise serializers.ValidationError(f"None data for performer='{video_performers_info}'.")
            
        



        



        # soup 取得
        url = f"https://www.dmm.co.jp/digital/videoa/-/detail/=/cid={productnumber_info}/" #一般ビデオ
        url = f"https://www.dmm.co.jp/digital/videoc/-/detail/=/cid={productnumber_info}/" #素人ビデオ        
        session = requests.Session()
        session.cookies.set("age_check_done", "1") 
        response = session.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        # type属性が"application/ld+json"の<script>タグを見つける
        script_tag = soup.find('script', attrs={'type': 'application/ld+json'})
        # <script>タグの中のJSONデータを抽出する
        json_str = script_tag.string.strip()
        json_data = json.loads(json_str)

        # soupから情報をゲット
        id_info = None
        video_title = soup.title.get_text().strip().split(" - []")[0]
        video_performers = None #手動で入れる
        video_productnumber = productnumber_info
        video_maker = None
        video_label = json_data["brand"]["name"]
        video_series = None
        video_description = json_data["description"]
        video_duration = get_duration_info(soup.find(text='収録時間：').find_parent('td').find_next_sibling().get_text().strip())
        video_views = 0
        # # thumbnails = json_data["subjectOf"]["thumbnailUrl"]
        # # kyounuki_post_day = models.DateField(blank=True, null=True)
        video_url = f"https://www.dmm.co.jp/digital/videoc/-/detail/=/cid={productnumber_info}/"
        video_image = json_data["image"]
        video_images = [x.get("src") for x in soup.find(attrs={"id": "sample-image-block"}).find_all("img")]
        video_sumple_video = json_data["subjectOf"]["contentUrl"]
        # # productthumbnail = models.URLField(blank=True, null=True)
        video_tags = json_data["subjectOf"]["genre"]
        # # video_active = models.BooleanField(default=True)
        # # images = models.CharField(max_length=1023, blank=True, null=True)
        video_issue = json_data["subjectOf"]["uploadDate"]
        video_affiliateurl = None

        # 取得したいキーを指定して値を取得
        # product_name = json_data["name"]
        # product_sku = json_data["sku"]
        # product_actor_name = json_data["subjectOf"]["actor"]["name"]
        # product_actor_name_eng = json_data["subjectOf"]["actor"]["alternateName"]
        # product_actor_name_eng = convert_to_romaji(product_actor_name_eng)
        # issue_info = soup.find(text='商品発売日：').find_parent('td').find_next_sibling().get_text().strip().replace(r'/', '-')


        from asgiref.sync import sync_to_async
        from django.forms.models import model_to_dict

        # 不足したLableとTagを作成
        judge_existence_obj(video_label, Label)
        for item in video_tags:
            judge_existence_obj(item, Tag)

        # Json作成
        json_str = json.dumps({
            "id" : None, 
            "video_title" : soup.title.get_text().strip().split(" - []")[0], 
            # "video_performers" : [],  #手動で入れる
            "video_productnumber" : productnumber_info, 
            "video_maker" : None, 
            "video_label" : json_data["brand"]["name"], 
            "video_series" : None, 
            "video_description" : json_data["description"], 
            "video_duration" : get_duration_info(soup.find(text='収録時間：').find_parent('td').find_next_sibling().get_text().strip()), 
            "video_views" : 0, 
            # # "thumbnails" : json_data["subjectOf"]["thumbnailUrl"], 
            # # "kyounuki_post_day" : models.DateField(blank=True, null=True), 
            "video_url" : f"https://www.dmm.co.jp/digital/videoc/-/detail/=/cid={productnumber_info}/", 
            "video_image" : json_data["image"], 
            "video_images" : video_images, 
            "video_sumple_video" : json_data["subjectOf"]["contentUrl"], 
            # # "productthumbnail" : models.URLField(blank=True, null=True), 
            # "video_tags" : json_data["subjectOf"]["genre"], 
            # # "video_active" : models.BooleanField(default=True), 
            # # "images" : models.CharField(max_length=1023, blank=True, null=True), 
            "video_issue" : json_data["subjectOf"]["uploadDate"], 
            "video_affiliateurl" : None, 
        }, indent=4, ensure_ascii=False)

        # JSON文字列を辞書に変換
        data_dict = json.loads(json_str)

        # LableとTagの設定、及びVideoCreate
        data_dict["video_label"] = Label.objects.get(name=video_label)

        video = Video.objects.create(**data_dict)

        performers_ids = [Performer.objects.get(name=x).id for x in video_performers_info]
        tag_ids = [Tag.objects.get(name=x).id for x in json_data["subjectOf"]["genre"]]

        video.video_tags.set(tag_ids)
        video.video_performers.set(performers_ids)

        return video

    class Meta:
        model = Video
        fields = '__all__'

def create_record(name, obj):
    try:
        name_eng = convert_to_romaji(name)
        name_eng = name_eng.replace(" ", "-")
        data_dict = {
            "name": name,
            "name_eng": name_eng
        }
        obj.objects.create(**data_dict)
        return "obj created successfully"
    except:pass

def create_record_article(name, obj):
    try:
        name_eng = convert_to_romaji(name)
        name_eng = name_eng.replace(" ", "-")
        data_dict = {
            "article_tag_name": name,
            "article_tag_name_eng": name_eng
        }
        obj.objects.create(**data_dict)
        return "obj created successfully"
    except Exception as e:
        # エラーが発生した場合、エラーメッセージを表示する
        print(f"Error occurred: {e}")
        return "Error occurred while creating obj"
    
def judge_existence_obj(name, obj):
    try:
        existing_videos = obj.objects.get(name=name)
        print(f"Duplicate data for name='{name}'.")
    except:
        # タグが存在しない場合の処理
        print("obj matching query does not exist. and create()")
        create_record(name, obj)
        pass
    return

def judge_existence_obj_article(name, obj):
    try:
        existing_videos = obj.objects.get(article_tag_name=name)
        print(f"Duplicate data for name='{name}'.")
    except:
        # タグが存在しない場合の処理
        print("obj matching query does not exist. and create()")
        create_record_article(name, obj)
        pass
    return





# class ContentsSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         contents_info = validated_data.get('contents')
#         contents_info = """
#         <title>あいうえお
#         <subtitle>かきくけこ
#         <text>text
#         <blockquote>blockquote<bookpage>2
#         <title>2
#         """

#         lines = contents_info.split("\n")
#         contents_ = []
#         contents = []
#         current_page = None
#         count = 1
#         count_title = 0
#         count_subtitle = 0
#         count_page = 0

#         for line in lines:
#             line = line.strip()
#             if not line:
#                 continue
#             if line == "":
#                 continue

#             tag, *content = line.split(">")
#             tag = tag[1:].lower()
#             content = ">".join(content).strip()

#             if tag == "title":
#                 count_title += 1
#             elif tag == "subtitle":
#                 count_subtitle += 1
#             elif tag == "page":
#                 if count_page != 0:
#                     count_page = int(content) - 1
#                     contents_.append(
#                         {"page": count_page, "contents": contents})
#                     contents = []
#                 continue


#             if "<bookpage>" in content:
#                 content, page = content.split("<bookpage>")
#                 page = int(page)
#                 obj = {
#                     "tag": tag,
#                     "text": content,
#                     "count": count,
#                     "title": count_title,
#                     "subtitle": count_subtitle,
#                     "blockquotepage": page
#                 }
#             else:
#                 obj = {
#                     "tag": tag,
#                     "text": content,
#                     "count": count,
#                     "title": count_title,
#                     "subtitle": count_subtitle
#                 }
#             contents.append(obj)
#             count += 1
        
#         # ManyToManyField の関連オブジェクトを新しいセットに置き換えます

#         contents_tags_info = validated_data.pop('tags', [])
#         validated_data["contents"] = contents
#         contents = Contents.objects.create(**validated_data)

#         contents.tags.set([x.id for x in contents_tags_info])

  
#         return contents
    
#     class Meta:
#         model = Contents
#         fields = '__all__'



# class GetContentsSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         # レコード作成を禁止するため、何も処理せずに例外を発生させます
#         raise serializers.ValidationError("Creating records is not allowed.")
#     class Meta:
#         model = Contents
#         fields = '__all__'





# class ContentsTagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContentsTag
#         fields = '__all__'
# class GetContentsTagSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         # レコード作成を禁止するため、何も処理せずに例外を発生させます
#         raise serializers.ValidationError("Creating records is not allowed.")
#     class Meta:
#         model = ContentsTag
#         fields = '__all__'


# ■■■■■■■■■■■■■■■■■■
# ■■■　Article　■■■
# ■■■■■■■■■■■■■■■■■■
def read_ods(filename, sheet_name=None, header=0):
    import pandas as pd 
    import ezodf

    doc = ezodf.opendoc(filename=filename)
    if sheet_name is not None:
        tab = doc.sheets[sheet_name]
    else:
        tab = doc.sheets[0]
    return pd.DataFrame({col[header].value: [x.value for x in col[header+1:]] for col in tab.columns()}) 


class GetArticletagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_tag
        fields = ["article_tag_name", "article_tag_name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    
class GetArticlechildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_child
        fields = ["article_name", "article_name_eng", "article_child_options", "article_affiliate_urls"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")

class CreateArticlechildSerializer(serializers.ModelSerializer):
    virtual_article_title_id = serializers.CharField(required=False)
    # virtual_article_title = serializers.CharField(required=False)
    article_title_id = serializers.CharField(required=False, read_only=True)
    article_name = serializers.CharField(required=False, read_only=True)
    article_name_eng = serializers.CharField(required=False, read_only=True)
    article_child_options = serializers.CharField(required=False, read_only=True)

    def create(self, validated_data):
        virtual_article_title_id = validated_data.get('virtual_article_title_id')
        # article_name_info = validated_data.get('article_name')
        # article_name_eng_info = convert_to_romaji(article_name_info)

        article_master = Article.objects.get(article_title_id=virtual_article_title_id)

        df = read_ods(filename='../../CreateArticlechildSerializer.ods', sheet_name=virtual_article_title_id)
        print("■■df■■\n", df.shape[0])
        Article_child_macth_ids = Article_child.objects.filter(article_title_id=virtual_article_title_id)
        if Article_child_macth_ids.exists():
            for article_child in Article_child_macth_ids:
                article_child.delete()
            print("関連するArticle_childオブジェクトが全て削除されました")
        else:
            print("関連するArticle_childオブジェクトは存在しません")

        my_dict = {}
        article_child_ids = []
        for i in range(1, int(df.shape[0])):
            article_name_info = df.iloc[i]["name"]
            article_name_eng_info = convert_to_romaji(article_name_info)
            print(f"df.iloc[i] ■■{i} \n", df.iloc[i])

            for key, value in df.iloc[i].items():
                my_dict[key.strip()] = value.strip() 
            # article_options_info = json.dumps(my_dict, ensure_ascii=False, separators=(",", ":"))

            json_str = json.dumps({
                "article_title_id" : virtual_article_title_id,
                "article_name" : article_name_info,
                "article_name_eng" : article_name_eng_info,
                "article_child_options" : my_dict,
                "article_affiliate_urls" : ''
            }, indent=4)

            # JSON文字列を辞書に変換
            data_dict = json.loads(json_str)    
            # data_dict["article_options_info"] = article_options_info

            article_child = Article_child.objects.create(**data_dict)
            article_child_id = article_child.pk
            article_child_ids.append(article_child_id)

        article_master.article_childlen.set(article_child_ids)

        return
            # Json作成
 

        # # "{\"name\":\"まとめ\",\"price\":\"価格\"}",

        #     # JSON文字列を辞書に変換
        #     data_dict = json.loads(json_str)
        #     article = Article.objects.get(**data_dict)

        #     # article_tags_ids = [Article_tag.objects.get(article_tag_name=x).id for x in article_tags_info]


        # # JSON文字列を辞書に変換
        # data_dict = json.loads(json_str)

        # article = Article.objects.create(**data_dict)

        # for name in article_tags_info:
        #     print(article_tags_info)
        #     # judge_existence_obj_article(name, Article_tag)

        # article_tags_ids = [Article_tag.objects.get(article_tag_name=x).id for x in article_tags_info]
        # # tag_ids = [Tag.objects.get(name=x).id for x in json_data["subjectOf"]["genre"]]

        # article.article_tags.set(article_tags_ids)            
            
            






        return
    

    class Meta:
        model = Article_child
        fields = '__all__'



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
def create(self, validated_data):
    # 'id' フィールドが 'validated_data' に存在するか確認
    id_info = validated_data.get('id', None)
    
    # 'id' フィールドが存在する場合
    if id_info is not None:
        try:
            # データベースから指定の 'id' の Article を取得
            existing_article = Article.objects.get(pk=id_info)
            
            # 'id' フィールドを除いた 'validated_data' を使って Article インスタンスを更新
            for field, value in validated_data.items():
                if field != 'id':
                    setattr(existing_article, field, value)
            existing_article.save()
            
            return existing_article
        except Article.DoesNotExist:
            # Article が存在しない場合、新しい Article を作成
            create_obj = Article.objects.create(**validated_data)
            return create_obj
    else:
        # 'id' フィールドが存在しない場合、新しい Article を作成
        create_obj = Article.objects.create(**validated_data)
        return create_obj

# class GetArticleParamsSerializer(serializers.Serializer):
#     classmajor = serializers.ListField()
#     classmedium = serializers.ListField()
#     classminor = serializers.ListField()

class GetArticleDupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CreateArticleSerializer(serializers.ModelSerializer):
    article_num = serializers.CharField(required=False, read_only=True)
    article_title_id = serializers.CharField(required=False)
    article_title = serializers.CharField(required=False)
    article_title_eng = serializers.CharField(required=False, read_only=True)
    article_post_day = serializers.DateField(required=False, format='%Y-%m-%d')
    article_tags = serializers.CharField(required=False)
    article_explain = serializers.CharField(required=False)
    article_childlen = serializers.CharField(required=False, read_only=True)
    article_views = serializers.CharField(required=False, read_only=True)
    article_options = serializers.CharField(required=False, read_only=True)
    article_options_explain = serializers.JSONField(required=False)
    article_options_order = serializers.CharField(required=False)
    

    def create(self, validated_data):
        article_title_info = validated_data.get('article_title')
        # Video obj に重複あるか確認。重複していればエラー処理

        # Article_tag.objects.all().delete()
        # Article.objects.all().delete()

        try:
            # データベースから指定のproductnumberでVideoを取得
            existing_article = Article.objects.get(article_title=article_title_info)
            raise serializers.ValidationError(f"Duplicate data for productnumber='{article_title_info}'.")
        except Article.DoesNotExist:
            pass

        article_tags_info = validated_data.get('article_tags').split(',')
        article_tags_info = list(article_tags_info)
        print(article_tags_info)
        if article_tags_info:
            for item in article_tags_info:
                print(item)
                judge_existence_obj_article(item, Article_tag)
        else:
            raise serializers.ValidationError(f"None data for performer='{article_tags_info}'.")

        article_post_day_info = validated_data.get('article_post_day')    
        if not article_post_day_info:
            article_post_day_info = datetime.date.today().strftime('%Y-%m-%d')
        else:
            # 日付情報を指定された形式に変換
            article_post_day_info = article_post_day_info.strftime('%Y-%m-%d')            

        from asgiref.sync import sync_to_async
        from django.forms.models import model_to_dict

        article_num_info = validated_data.pop('article_num', None)
        if article_num_info == "":
            article_num_info = 1
        else:
            article_num_info = len(Article.objects.all()) + 1



        article_title_info = validated_data.pop('article_title', None)

        article_title_eng_info = convert_to_romaji(article_title_info)
        article_title_eng_info = article_title_eng_info.replace(" ", "-")

        # article_options_info = validated_data.get('article_options')
        # my_dict = {}
        # for pair in article_options_info.split(","):
        #     key, value = pair.split(":")
        #     my_dict[key.strip()] = value.strip() 
        # article_options_info = json.dumps(my_dict, ensure_ascii=False, separators=(",", ":"))
        article_title_id_info = validated_data.pop('article_title_id', None)
        
        df = read_ods(filename='../../CreateArticlechildSerializer.ods', sheet_name=article_title_id_info)
        print("■■df■■\n", df.shape[0])
        Article_child_macth_ids = Article_child.objects.filter(article_title_id=article_title_id_info)
        my_dict = {}
        for key, value in df.iloc[0].items():
            my_dict[key.strip()] = value.strip() 






        article_options_order_info = validated_data.get('article_options_order')
        article_options_order_info = article_options_order_info.replace("[", "['").replace(",", "','").replace("]", "']")
        article_options_order_info = eval(article_options_order_info)
        


        # Json作成
        json_str = json.dumps({
            "article_num" : article_num_info,
            "article_title_id": article_title_id_info,
            "article_title" : article_title_info,
            "article_title_eng" : article_title_eng_info,
            "article_post_day" : article_post_day_info,
            # "article_tags" : validated_data.get('article_tags'),
            "article_explain" : validated_data.get('article_explain'),
            "article_options_explain" : validated_data.get('article_options_explain'),
            # "article_childlen" : validated_data.get('article_childlen'),
            "article_views" : validated_data.get('article_views'),
            "article_options" : my_dict,
            "article_options_order" : article_options_order_info
        }, indent=4, ensure_ascii=False)




        # JSON文字列を辞書に変換
        data_dict = json.loads(json_str)

        article = Article.objects.create(**data_dict)

        for name in article_tags_info:
            print(article_tags_info)
            # judge_existence_obj_article(name, Article_tag)

        article_tags_ids = [Article_tag.objects.get(article_tag_name=x).id for x in article_tags_info]
        # tag_ids = [Tag.objects.get(name=x).id for x in json_data["subjectOf"]["genre"]]

        article.article_tags.set(article_tags_ids)
        # article.video_performers.set(performers_ids)

        return article

    class Meta:
        model = Article
        fields = '__all__'


class UpdateArticleSerializer(serializers.ModelSerializer):
    # article_options = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

class GetArticleSerializer(serializers.ModelSerializer):
    # article_num = models.IntegerField(blank=True, null=True)
    # article_title = models.CharField(max_length=255, blank=True, null=True)
    # article_title_eng = models.CharField(max_length=255, blank=True, null=True)
    # article_post_day = models.DateField(blank=True, null=True)
    article_tags = GetArticletagSerializer(many=True)
    # article_explain = models.CharField(max_length=1023, blank=True, null=True)
    article_childlen = GetArticlechildSerializer(many=True)
    # article_views = models.IntegerField(blank=True, null=True)
    # article_options = models.JSONField()
    # article_options_order = models.CharField(max_length=255,blank=True, null=True)
    class Meta:
        model = Article
        fields = '__all__'
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")


class ArticltagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_tag
        fields = '__all__'
