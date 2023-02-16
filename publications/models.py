from django.contrib.auth.models import User
from django.db import models



class Topics(models.Model):
    name = models.CharField(max_length=30)


class Publication(models.Model):
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True)
    topics = models.ManyToManyField(Topics, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)


class Comment(models.Model):
    post = models.ForeignKey(Publication, on_delete=models.CASCADE, default=Publication)
    comment = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)


class PostLike(models.Model):
    author = models.ManyToManyField(User)
    like_post = models.ManyToManyField(Publication)
