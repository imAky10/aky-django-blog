from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    blog_content = models.TextField()
    pub_date = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Articles"

    def snippet(self):
        return self.blog_content[:200] + '...'