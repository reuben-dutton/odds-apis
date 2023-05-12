import re
import json
import os
import sys

sys.path.append(os.getcwd())

import requests
from bs4 import BeautifulSoup

from apis.apiBase import OddsAPIBase

baseSportsURL = "https://www.sportsbet.com.au/apigw/sportsbook-sports/Sportsbook/Sports"


class SportsBetOddsAPI(OddsAPIBase):

    def __init__(self, api_key=None):
        super().__init__(api_key=api_key)

    def get_events(self, competitionId, params = None):
        '''
        Params:
            competitionId [int]
                The id corresponding to the desired competition/sport
                e.g. NBA is 6927
            
        Options:
            displayType [str] - default
                UNKNOWN
            includeTopMarkets [bool]
                Whether markets are included in the response data
                If not given, default is false
            eventFilter [str] - matches, outrights
                Filters for matches or futures (outrights)
                If not given, both are included
            numMarkets [int]
                Specify many markets are included in the response data
                If not given, then return all markets possible

        '''

        requestURL = baseSportsURL + f'/Competitions/{competitionId}'
        if not params:
            params = dict()
            params['displayType'] = 'default'
            params['includeTopMarkets'] = "false"
            # params['eventFilter'] = 'matches'
        else:
            # convert includeTopMarkets to a string in lowercase
            params['includeTopMarkets'] = str(params.get(includeTopMarkets, "false")).lower()

        resp = requests.get(requestURL, params=params)

        if resp.ok:
            return resp.json()
        else:
            raise Exception("Request failed with error code %s" % resp.status_code)

    def get_match(self, matchId, params = None):
        '''
        Params:
            matchId [int]
                The id corresponding to the desired match/event
                e.g. New York Knicks vs Miami Heat 9th May is 7333708
            
        Options:
            
        '''

        requestURL = baseSportsURL + f'/Events/{matchID}/SportCard'
        if not params:
            params = dict()

        resp = requests.get(requestURL, params=params)

        if resp.ok:
            return resp.json()
        else:
            raise Exception("Request failed with error code %s" % resp.status_code)

    def get_match_market(self, matchId, marketId, params=None):
        '''
        Params:
            matchId [int]
                The id corresponding to the desired match/event
                e.g. New York Knicks vs Miami Heat 9th May is 7333708
            marketId [int]
                The id corresponding to the desired market
                e.g. Match Betting for NBA matches is 286
            
        Options:
            
        '''

        requestURL = baseSportsURL + f'/Events/{matchID}/MarketGroupings/{marketId}/Markets'
        if not params:
            params = dict()

        resp = requests.get(requestURL, params=params)

        if resp.ok:
            return resp.json()
        else:
            raise Exception("Request failed with error code %s" % resp.status_code)