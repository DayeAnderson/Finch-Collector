from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Monster, Weakness
from .forms import AttackForm

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
    weaknesses_monster_doesnt_have = Weakness.objects.exclude(id__in = monster.weaknesses.all().values_list('id'))
    attack_form = AttackForm()
    return render(request, 'monsters/detail.html', {
        'monster': monster, 'attack_form': attack_form, 'weaknesses': weaknesses_monster_doesnt_have
        })
    
def add_attacks(request, monster_id):
  # create a ModelForm instance using the data in request.POST
  form = AttackForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_attacks = form.save(commit=False)
    new_attacks.monster_id = monster_id
    new_attacks.save()
  return redirect('detail', monster_id=monster_id)

class MonsterCreate(CreateView):
    model = Monster
    fields = '__all__'
    success_url = '/monsters/'

class MonsterUpdate(UpdateView):
  model = Monster
  fields = ['name', 'size', 'wyvern_type', 'ferocity']

class MonsterDelete(DeleteView):
  model = Monster
  success_url = '/monsters/'

class WeaknessList(ListView):
  model = Weakness

class WeaknessDetail(DetailView):
  model = Weakness

class WeaknessCreate(CreateView):
  model = Weakness
  fields = '__all__'

class WeaknessUpdate(UpdateView):
  model = Weakness
  fields = ['name', 'color']

class WeaknessDelete(DeleteView):
  model = Weakness
  success_url = '/weaknesses/'

def assoc_weakness(request, monster_id, weakness_id):
    Monster.objects.get(id=monster_id).weaknesses.add(weakness_id)
    return redirect('detail', monster_id=monster_id)