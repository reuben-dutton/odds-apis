import re
import json
import os
import sys

sys.path.append(os.getcwd())

import requests
from bs4 import BeautifulSoup

from apis.apiBase import OddsAPIBase

baseURL = "https://ss-aka-ori.ladbrokes.com/openbet-ssviewer/Drilldown/2.31/"

# translationLang=en&responseFormat=json

class LadBrokesOddsAPI(OddsAPIBase):

    def __init__(self, api_key=None):
        super().__init__(api_key=api_key)

    def get_matches(self, competitionId, params=None):
        '''
        Params:
            competitionId [int]
                The id corresponding to the desired competition/sport
                e.g. NBA is 136
            
        Options:
            translationLang [str] - en
                UNKNOWN - Doesn't make any apparent changes
            includeTopMarkets [bool]
                Whether markets are included in the response data
                If not given, default is false

        '''

        if not params:
            params = dict()
            params['responseFormat'] = "json"
            params['translationLang'] = "en"
        else:
            params['responseFormat'] = "json"

        headers = dict()
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"

        requestURL = baseURL + f"EventToOutcomeForType/{competitionId}"

        resp = requests.get(requestURL, params=params, headers=headers)
        print(resp.url)

        if resp.ok:
            return resp.json()
        else:
            raise Exception("Request failed with error code %s" % resp.status_code)


if __name__ == "__main__":
    api = LadBrokesOddsAPI()
    data = api.get_matches(136)