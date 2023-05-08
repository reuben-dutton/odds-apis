import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
print(API_KEY)

SPORT = 'upcoming'

AUS_SPORTS = 'aussierules_afl'


REGIONS = 'au'

MARKETS = 'h2h'

ODDS_FORMAT = 'decimal'

DATE_FORMAT = 'iso'



odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{AUS_SPORTS}/odds',
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
    }
)

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    odds_json = odds_response.json()
    print('Number of events:', len(odds_json))
    print(odds_json)

    # Check the usage quota
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])

    with open('data.json', 'w') as j:
        json.dump(odds_json, j)