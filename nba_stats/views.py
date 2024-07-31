# nba_stats/views.py
from django.shortcuts import render
import requests
from django.core.paginator import Paginator
import logging

API_KEY = '35424622-4972-4b89-9654-eb89992d8f97'
BASE_URL = 'https://api.balldontlie.io/v1'
TEAMS_URL = f'{BASE_URL}/teams'
GAMES_URL = f'{BASE_URL}/games'
PLAYERS_URL = f'{BASE_URL}/players'
STATS_URL = f'{BASE_URL}/stats'
SEASON_AVERAGES_URL = f'{BASE_URL}/season_averages'

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'stats/index.html')

def get_teams(request):
    try:
        response = requests.get(TEAMS_URL, headers={'Authorization': API_KEY})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        teams = data.get('data', [])
        
        logger.debug('Fetching teams from API...')
        logger.debug(f'Response Status Code: {response.status_code}')
        logger.debug(f'Response Body: {response.text}')
        logger.debug(f'Number of teams retrieved: {len(teams)}')
        
        paginator = Paginator(teams, 10)  # Show 10 teams per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'stats/teams.html', context)

    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching teams: {str(e)}')
        return render(request, 'stats/error.html', {'error': str(e)})

# nba_stats/views.py
from django.shortcuts import render
import requests
from django.core.paginator import Paginator
import logging

API_KEY = '35424622-4972-4b89-9654-eb89992d8f97'
BASE_URL = 'https://api.balldontlie.io/v1'
GAMES_URL = f'{BASE_URL}/games'

# Set up logging
logger = logging.getLogger(__name__)

def get_games(request):
    # Fetch games
    page = request.GET.get('page', 1)  # Default to page 1 if not specified
    per_page = 10  # Number of items per page
    
    api_debug_info = {
        'status_code': None,
        'response_body': None,
        'num_games': 0
    }
    
    logger.debug('Fetching games from API...')
    logger.debug(f'Request URL: {GAMES_URL}')
    logger.debug(f'Parameters: page={page}, per_page={per_page}')
    
    try:
        response = requests.get(GAMES_URL, params={'page': page, 'per_page': per_page}, headers={'Authorization': API_KEY})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        api_debug_info['status_code'] = response.status_code
        api_debug_info['response_body'] = response.text
        
        data = response.json()
        games = data.get('data', [])
        
        api_debug_info['num_games'] = len(games)
        
        logger.debug(f'Number of games retrieved: {len(games)}')
        if not games:
            logger.debug('No games found in the response.')
        
        # Pagination
        paginator = Paginator(games, per_page)
        page_obj = paginator.get_page(page)
        
        context = {
            'page_obj': page_obj,
            'api_debug_info': api_debug_info
        }
        return render(request, 'stats/games.html', context)

    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching games: {str(e)}')
        context = {
            'api_debug_info': api_debug_info,
            'error': str(e)
        }
        return render(request, 'stats/error.html', context)


def get_players(request):
    try:
        response = requests.get(PLAYERS_URL, headers={'Authorization': API_KEY})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        players = data.get('data', [])
        
        logger.debug('Fetching players from API...')
        logger.debug(f'Response Status Code: {response.status_code}')
        logger.debug(f'Response Body: {response.text}')
        logger.debug(f'Number of players retrieved: {len(players)}')
        
        paginator = Paginator(players, 10)  # Show 10 players per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {'page_obj': page_obj}
        return render(request, 'stats/players.html', context)

    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching players: {str(e)}')
        return render(request, 'stats/error.html', {'error': str(e)})

def get_stats(request):
    try:
        response = requests.get(STATS_URL, headers={'Authorization': API_KEY})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        stats = data.get('data', [])
        
        logger.debug('Fetching stats from API...')
        logger.debug(f'Response Status Code: {response.status_code}')
        logger.debug(f'Response Body: {response.text}')
        logger.debug(f'Number of stats retrieved: {len(stats)}')
        
        paginator = Paginator(stats, 10)  # Show 10 stats per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {'page_obj': page_obj}
        return render(request, 'stats/stats.html', context)

    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching stats: {str(e)}')
        return render(request, 'stats/error.html', {'error': str(e)})

def get_season_averages(request):
    try:
        response = requests.get(SEASON_AVERAGES_URL, headers={'Authorization': API_KEY})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        season_averages = data.get('data', [])
        
        logger.debug('Fetching season averages from API...')
        logger.debug(f'Response Status Code: {response.status_code}')
        logger.debug(f'Response Body: {response.text}')
        logger.debug(f'Number of season averages retrieved: {len(season_averages)}')
        
        paginator = Paginator(season_averages, 10)  # Show 10 season averages per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {'page_obj': page_obj}
        return render(request, 'stats/season_averages.html', context)

    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching season averages: {str(e)}')
        return render(request, 'stats/error.html', {'error': str(e)})
