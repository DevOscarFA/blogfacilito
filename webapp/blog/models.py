from django.db import models
from tinymce import models as tinymce_models

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = tinymce_models.HTMLField()
    slug = models.SlugField(default='null')
    thumb = models.ImageField(default='null.png', blank=True)
    time = models.DateTimeField()