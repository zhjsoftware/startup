from django.db import models

# Create your models here.

class knowledge(models.Model):
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=80)
    content = models.TextField()

    def __unicode__(self):
        return self.title


class brand(models.Model):
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=80)
    content = models.TextField()

    def __unicode__(self):
        return self.title
