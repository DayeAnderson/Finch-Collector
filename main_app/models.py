from django.db import models
from django.urls import reverse

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    element = models.CharField(max_length=100)
    wyvern_type = models.CharField(max_length=100)
    ferocity = models.IntegerField()

    def __str__(self):
        return self.name
    
def get_absolute_url(self):
    return reverse('detail', kwargs={'monster_id': self.id})