from django.forms import ModelForm
from .models import Attacks

class AttackForm(ModelForm):
  class Meta:
    model = Attacks
    fields = ['attack', 'element']