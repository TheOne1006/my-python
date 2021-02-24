from django.db import models

# Create your models here.
class Article(models.Model):
    article_Id = models.AutoField(primary_key=True)

    # 标题
    title = models.TextField()

    brief = models.TextField()

    content = models.TextField()

    publish_date = models.DateTimeField(auto_now=True)