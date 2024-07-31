# nba_project/urls.py
from django.contrib import admin
from django.urls import path
from nba_stats import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('teams/', views.get_teams, name='teams'),
    path('games/', views.get_games, name='games'),
    path('players/', views.get_players, name='players'),
    path('stats/', views.get_stats, name='stats'),
    path('season_averages/', views.get_season_averages, name='season_averages'),
]







