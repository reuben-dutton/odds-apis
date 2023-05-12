
import re
import json
import os
import sys
import urllib.parse

sys.path.append(os.getcwd())

import requests
from bs4 import BeautifulSoup

from apis.apiBase import OddsAPIBase


baseSportsURL = "https://api.beta.tab.com.au/v1/tab-info-service/sports"


class TabOddsAPI(OddsAPIBase):

    def __init__(self, api_key=None):
        super().__init__(api_key=api_key)

    def get_sports(self, jurisdiction):
        '''
        Params:
            jurisdiction [str] NSW VIC ACT QLD SA NT TAS
                A string code corresponding to an Australian state.
                The returned sports will be those available for betting in
                that state (I assume)
            
        Options:

        '''

        if jurisdiction not in ["NSW", "VIC", "ACT", "QLD", "SA", "NT", "TAS"]:
            raise ArgumentException("Jurisdiction must be NSW, VIC, ACT, QLD, SA, NT or TAS")

        params = dict()
        params['jurisdiction'] = jurisdiction

        requestURL = baseSportsURL

        resp = requests.get(requestURL, params=params)

        if resp.ok:
            return resp.json()
        else:
            raise Exception("Request failed with error code %s" % resp.status_code)

    def get_matches(self, sportsName, competitionName, jurisdiction):
        '''
        Params:
            sportsName [str] 
                The name of the sport (e.g. Basketball)
            competitionName
                The name of the competition (e.g. NBA)
            jurisdiction [str] NSW VIC ACT QLD SA NT TAS
                A string code corresponding to an Australian state.
                The returned sports will be those available for betting in
                that state (I assume)
            
        Options:

        '''

        if jurisdiction not in ["NSW", "VIC", "ACT", "QLD", "SA", "NT", "TAS"]:
            raise ArgumentException("Jurisdiction must be NSW, VIC, ACT, QLD, SA, NT or TAS")

        sportsName = urllib.parse.quote(sportsName)
        competitionName = urllib.parse.quote(competitionName)

        requestURL = baseSportsURL + f"/{sportsName}/competitions/{competitionName}/matches"

        params = dict()
        params['jurisdiction'] = jurisdiction

        resp = requests.get(requestURL, params=params)

        if resp.ok:
            return resp.json()
        else:
            raise Exception("Request failed with error code %s" % resp.status_code)

    def get_markets(self, sportsName, competitionName, matchName, jurisdiction):
        '''
        Params:
            sportsName [str] 
                The name of the sport (e.g. Basketball)
            competitionName [str]
                The name of the competition (e.g. NBA)
            matchName [str]
                The name of the match (e.g. Boston v Philadelphia)
            jurisdiction [str] NSW VIC ACT QLD SA NT TAS
                A string code corresponding to an Australian state.
                The returned sports will be those available for betting in
                that state (I assume)
            
        Options:

        '''

        if jurisdiction not in ["NSW", "VIC", "ACT", "QLD", "SA", "NT", "TAS"]:
            raise ArgumentException("Jurisdiction must be NSW, VIC, ACT, QLD, SA, NT or TAS")

        sportsName = urllib.parse.quote(sportsName)
        competitionName = urllib.parse.quote(competitionName)
        matchName = urllib.parse.quote(matchName)

        requestURL = baseSportsURL + f"/{sportsName}/competitions/{competitionName}/matches/{matchName}/markets"

        params = dict()
        params['jurisdiction'] = jurisdiction

        resp = requests.get(requestURL, params=params)

        if resp.ok:
            return resp.json()
        else:
            raise Exception("Request failed with error code %s" % resp.status_code)

    # Processing data

    def process_matches(self, data):
        for market in data['markets']:
            print(market['betOption'])


if __name__ == "__main__":
    oddsAPI = TabOddsAPI()
    data = oddsAPI.get_markets('Basketball', 'NBA', "Boston v Philadelphia", "QLD")
    oddsAPI.process_matches(data)