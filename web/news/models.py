from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField()
    content = models.TextField()
    published = models.BooleanField(default=False)
        
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.title)

class Link(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField()
    content = models.TextField()
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.title)
