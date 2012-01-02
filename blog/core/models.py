from django.db import models

class Tag(models.Model):
    
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)

class Post(models.Model):

    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag)
