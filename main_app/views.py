from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Monster:
    def __init__(self, name, size, element, ferocity):
        self.name = name
        self.size = size
        self.element = element
        self.ferocity = ferocity

monsters = [
    Monster('Fatalis', 'large', 'fire', 'HIGH PAST THE SKY'),
    Monster('Alatreon', 'large', 'fire, water, thunder, dragon', 'high'),
    Monster('Vespoid', 'small', 'none', 'medium')
]

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def monsters_index(request):
    return render(request, 'monsters/index.html', {'monsters': monsters})
