from django.db import models

# Create your models here.
class Article(models.Model):
    # ����id
    article_id = models.AutoField(primary_key=True)
    # ���±���
    title = models.TextField()
    # ����ժҪ
    brief_content = models.TextField()
    # ������Ҫ����
    content = models.TextField()
    # ����
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
