from django.db import models
from django.urls import reverse

ELEMENTS = (
    ('NON', 'None'),
    ('FIR', 'Fire'),
    ('WAT', 'Water'),
    ('THN', 'Thunder'),
    ('DRG', 'Dragon'),
    ('BLS', 'Blast'),
    ('PAR', 'Paralysis'),
    ('PSN', 'Posion'),
    ('SLP', 'Sleep'),
)

# Create your models here.

class Weakness(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('weaknesses_detail', kwargs={'pk': self.id})

class Monster(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    element = models.CharField(max_length=100)
    wyvern_type = models.CharField(max_length=100)
    ferocity = models.IntegerField()
    weaknesses = models.ManyToManyField(Weakness)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'monster_id': self.id})

    class Meta:
        ordering = ['-ferocity']

class Attacks(models.Model):
    attack = models.CharField(max_length=50)
    element = models.CharField(
        max_length=3,
        choices=ELEMENTS,
        default=ELEMENTS[0][0]
        )
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_element_display()} on {self.attack}"
