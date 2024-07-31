# nba_stats/urls.py
from django.urls import path
from .views import get_teams, get_games, get_players, get_stats, get_season_averages, index

urlpatterns = [
    path('', index, name='index'),
    path('teams/', get_teams, name='teams'),
    path('games/', get_games, name='games'),
    path('players/', get_players, name='players'),
    path('stats/', get_stats, name='stats'),
    path('season_averages/', get_season_averages, name='season_averages'),
]

