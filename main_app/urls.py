from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('monsters/', views.monsters_index, name="index"),
    path('monsters/<int:monster_id>/', views.monsters_detail, name='detail'),
    path('monsters/create/', views.MonsterCreate.as_view(), name='monsters_create'),
    path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monsters_update'),
    path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monsters_delete'),
    path('monsters/<int:monster_id>/add_attacks/', views.add_attacks, name='add_attacks'),
    path('weaknesses/', views.WeaknessList.as_view(), name='weaknesses_index'),
    path('weaknesses/<int:pk>/', views.WeaknessDetail.as_view(), name='weaknesses_detail'),
    path('weaknesses/create/', views.WeaknessCreate.as_view(), name='weaknesses_create'),
    path('weaknesses/<int:pk>/update/', views.WeaknessUpdate.as_view(), name='weaknesses_update'),
    path('weaknesses/<int:pk>/delete/', views.WeaknessDelete.as_view(), name='weaknesses_delete'),
    path('monsters/<int:monster_id>/assoc_weakness/<int:weakness_id>/', views.assoc_weakness, name='assoc_weakness'),


]