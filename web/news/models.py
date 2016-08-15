from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
        content = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        published = models.BooleanField(default=False)
        slug = models.SlugField(max_length=255, unique=True)
        title = models.CharField(max_length=255)

        class Meta:
                ordering = ['-created']

class Link(models.Model):
        content = models.CharField(max_length=255)
        created = models.DateTimeField(auto_now_add=True)
        published = models.BooleanField(default=False)
        slug = models.SlugField(max_length=255, unique=True)
        title = models.CharField(max_length=255)
