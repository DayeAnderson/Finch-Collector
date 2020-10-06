from django.db import models

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    element = models.CharField(max_length=100)
    wyvern_type = models.CharField(max_length=100)
    ferocity = models.IntegerField()

    def __str__(self):
        return self.name