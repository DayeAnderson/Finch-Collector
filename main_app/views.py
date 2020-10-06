from django.shortcuts import render
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
