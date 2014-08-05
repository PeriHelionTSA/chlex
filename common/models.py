from django.db import models


class Meaning(models.Model):
    meaning = models.CharField(max_length=5000)
    lem = models.ForeignKey("Lem")


class Lem(models.Model):
    # TODO: renaming graphs to graph
    graphs = models.CharField(max_length=5000)
    pinyin = models.CharField(max_length=5000)
    comment = models.CharField(max_length=5000, null=True, blank=True)

    def __unicode__(self):
        return self.graphs + u" " + self.pinyin
