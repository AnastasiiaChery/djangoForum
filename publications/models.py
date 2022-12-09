from django.contrib.auth.models import User
from django.db import models


class Topics(models.Model):
    name = models.CharField(max_length=30)


class Publication(models.Model):
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    topics = models.ManyToManyField(Topics)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



class PostLike(models.Model):
    author = models.ManyToManyField(User)
    like_post = models.OneToOneField(Publication, on_delete=models.CASCADE)

class CommentLike(models.Model):
    author = models.ManyToManyField(User)
    like_comment = models.OneToOneField(Comment, on_delete=models.CASCADE)

