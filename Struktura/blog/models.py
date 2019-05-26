from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(null=False, max_length=500)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)