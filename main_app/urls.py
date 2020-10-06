from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('monsters/', views.monsters_index, name="index"),
    path('monsters/<int:monster_id>/', views.monsters_detail, name='detail')
]