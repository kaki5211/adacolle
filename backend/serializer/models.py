# Create your models here.
from django.db import models

class Performer(models.Model):
    name = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class Maker(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

# class Thumbnail(models.Model):
#     url = models.URLField()
#     width = models.IntegerField()
#     height = models.IntegerField()

# class Kyounuki(models.Model):
#     post_day = models.DateField()
#     productnumbers = models.ManyToManyField('Video')
#     article = models.TextField()
#     def __str__(self):
#         return str(self.post_day)


class Video(models.Model):
    video_title = models.CharField(max_length=255, blank=True, null=True)
    video_postday = models.DateField(blank=True, null=True)
    video_performers = models.ManyToManyField(Performer, blank=True, null=True)
    video_productnumber = models.CharField(max_length=255, blank=True, null=True, unique=True)
    video_maker = models.ForeignKey(Maker, on_delete=models.CASCADE, blank=True, null=True)
    video_label = models.ForeignKey(Label, on_delete=models.CASCADE, blank=True, null=True)
    video_series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True)
    video_description = models.TextField(blank=True, null=True)
    video_duration = models.CharField(max_length=255, blank=True, null=True)
    video_views = models.IntegerField(blank=True, null=True)
    # thumbnails = models.ManyToManyField(Thumbnail, blank=True, null=True)
    # kyounuki_post_day = models.DateField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    video_image = models.CharField(max_length=1023, blank=True, null=True)
    video_images = models.CharField(max_length=1023, blank=True, null=True)
    video_sumple_video = models.URLField(blank=True, null=True)
    # productthumbnail = models.URLField(blank=True, null=True)
    video_tags = models.ManyToManyField(Tag, blank=True, null=True, related_name="video_tags")
    # video_active = models.BooleanField(default=True)
    # images = models.CharField(max_length=1023, blank=True, null=True)
    video_issue = models.DateField(blank=True, null=True)
    video_affiliateurl = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.video_productnumber
    


class Article_child(models.Model):
    article_title_id = models.CharField(max_length=255, blank=True, null=True)
    article_name = models.CharField(max_length=255, blank=True, null=True)
    article_name_eng = models.CharField(max_length=255, blank=True, null=True)

    article_child_options = models.JSONField()
    article_affiliate_urls = models.JSONField()



class Article_tag(models.Model):
    article_tag_name = models.CharField(max_length=255, blank=True, null=True)
    article_tag_name_eng = models.CharField(max_length=255, blank=True, null=True)



class Article(models.Model):
    article_num = models.IntegerField(blank=True, null=True)
    article_title_id = models.CharField(max_length=255, blank=True, null=True)
    article_title = models.CharField(max_length=255, blank=True, null=True)
    article_title_eng = models.CharField(max_length=255, blank=True, null=True)
    article_post_day = models.DateField(blank=True, null=True)
    # article_image = models.ForeignKey(Article_child, on_delete=models.CASCADE, blank=True, null=True)
    # article_images = models.ManyToManyField(Article_child, blank=True, null=True, related_name="article_child_article_images")
    article_tags = models.ManyToManyField(Article_tag, blank=True, null=True)
    # title = models.CharField(max_length=255, blank=True, null=True)
    # title_eng = models.CharField(max_length=255, blank=True, null=True)

    # title_number = models.IntegerField(blank=True, null=True)
    # name = models.CharField(max_length=1023, blank=True, null=True)
    # classmajor = models.CharField(max_length=255, blank=True, null=True)
    # classmedium = models.CharField(max_length=255, blank=True, null=True)
    # classminor = models.CharField(max_length=255, blank=True, null=True)
    # number = models.IntegerField(blank=True, null=True)
    # price = models.CharField(max_length=255, blank=True, null=True)
    article_explain = models.CharField(max_length=1023, blank=True, null=True)
    article_options_explain = models.CharField(max_length=1023, blank=True, null=True)
    # content = models.TextField(max_length=255, blank=True, null=True)
    # top_image = models.CharField(max_length=1023, blank=True, null=True)
    # article_images = models.CharField(max_length=1023, blank=True, null=True)
    # affiliateurl = models.CharField(max_length=1023,blank=True, null=True)
    # article_post_day = models.DateField()
    article_childlen = models.ManyToManyField(Article_child, blank=True, null=True, related_name="article_child_article_childlen")
    article_views = models.IntegerField(blank=True, null=True)
    article_options = models.JSONField(blank=True, null=True)
    article_options_order = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return str(self.article_title)






# class ContentsTag(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     name_eng = models.CharField(max_length=255, unique=True, blank=True, null=True)
#     def __str__(self):
#         return self.name


# class Contents(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     contents = models.TextField(blank=True, null=True)
#     views = models.IntegerField(blank=True, null=True)
#     tags = models.ManyToManyField(ContentsTag, blank=True, null=True)

#     def __str__(self):
#         return self.title
    
    # contents = 
    #     <title>あいうえお
    #     <subtitle>かきくけこ
    #     <text>text
    #     <blockquote>blockquote<bookpage>2
    #     <title>2



class Test(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, blank=True, null=True)
    teststr = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.maker


