from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    
    @property
    def slug(self):
        return self.post.slug