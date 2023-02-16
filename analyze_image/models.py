from django.db import models
class ImageAnalyze(models.Model):
    image = models.ImageField(upload_to='images/')
