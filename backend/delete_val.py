import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','model_project.settings')

from django import setup
setup()

from model_app.models import Article

Article.objects.all().delete() # 全件削除