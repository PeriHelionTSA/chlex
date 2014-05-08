from django.db import models

# Create your models here.
class Lem(models.Model):
    graphs = models.CharField(max_length=5000)
    pinyin = models.CharField(max_length=5000)
