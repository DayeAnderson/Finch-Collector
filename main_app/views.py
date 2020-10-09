from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Monster, Weakness
from .forms import AttackForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def monsters_index(request):
    monsters = Monster.objects.filter(user=request.user)
    return render(request, 'monsters/index.html', {'monsters': monsters})

@login_required
def monsters_detail(request, monster_id):
    monster = Monster.objects.get(id=monster_id)
    weaknesses_monster_doesnt_have = Weakness.objects.exclude(id__in = monster.weaknesses.all().values_list('id'))
    attack_form = AttackForm()
    return render(request, 'monsters/detail.html', {
        'monster': monster, 'attack_form': attack_form, 'weaknesses': weaknesses_monster_doesnt_have
        })
    
@login_required
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
    fields = ['name', 'size', 'element', 'wyvern_type', 'ferocity']
    success_url = '/monsters/'

    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class MonsterUpdate(LoginRequiredMixin, UpdateView):
  model = Monster
  fields = ['name', 'size', 'wyvern_type', 'ferocity']

class MonsterDelete(LoginRequiredMixin, DeleteView):
  model = Monster
  success_url = '/monsters/'

class WeaknessList(LoginRequiredMixin, ListView):
  model = Weakness

class WeaknessDetail(LoginRequiredMixin, DetailView):
  model = Weakness

class WeaknessCreate(LoginRequiredMixin, CreateView):
  model = Weakness
  fields = '__all__'

class WeaknessUpdate(LoginRequiredMixin, UpdateView):
  model = Weakness
  fields = ['name', 'color']

class WeaknessDelete(LoginRequiredMixin,  DeleteView):
  model = Weakness
  success_url = '/weaknesses/'

def assoc_weakness(request, monster_id, weakness_id):
    Monster.objects.get(id=monster_id).weaknesses.add(weakness_id)
    return redirect('detail', monster_id=monster_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)