from django.db import models


class Meaning(models.Model):
    meaning = models.CharField(max_length=5000)
    lem = models.ForeignKey("Lem")

class Lem(models.Model):
    graphs = models.CharField(max_length=5000)
    pinyin = models.CharField(max_length=5000)

    def __unicode__(self):
        return self.graphs + u" " + self.pinyin
