from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster

# Create your views here.
from django.http import HttpResponse


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def monsters_index(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/index.html', {'monsters': monsters})

def monsters_detail(request, monster_id):
    monster = Monster.objects.get(id=monster_id)
    return render(request, 'monsters/detail.html', {'monster': monster})

class MonsterCreate(CreateView):
    model = Monster
    fields = '__all__'
    success_url = '/monsters/'

class CatUpdate(UpdateView):
  model = Monster
  fields = '__all__'

class CatDelete(DeleteView):
  model = Monster
  success_url = '/monsters/'