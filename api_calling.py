import pandas as pd
import requests
import os
from dotenv import load_dotenv
import json

class OddsApiCaller:
    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.url = "https://api.the-odds-api.com/v4/sports"
        self.sport = 'upcoming'
        self.region = 'eu'
        self.market = 'h2h' 
        self.odds_format = 'decimal' 
        self.date_format = 'iso' 
    
    def get_odds_df(self) -> pd.DataFrame:
        result = pd.DataFrame()
        response = requests.get(f'{self.url}/{self.sport}/odds', 
            params={
                'api_key': self.api_key,
                'regions': self.region,
                'markets': self.market,
                'oddsFormat': self.odds_format,
                'dateFormat': self.date_format
            }
        )
        
        if response.status_code == 200:
            fo = open("odds.json", "w")
            json.dump(response.json, fo)
            fo.close()
            result = pd.read_json("odds.json")
        else: 
            result['error-code'] = response.status_code
            result['error-text'] = response.text

        return result
    
    def __parse_dataframe(self) -> pd.DataFrame:
        pass

    def remaining_api_usage(self) -> dict:
        result = {}
        response = requests.get(f'{self.url}',
            params={
                'api_key': self.api_key
            })
        if response.status_code == 200:
            result['remaining'] = response.headers['x-requests-remaining']
            result['used'] = response.headers['x-requests-used']
        else: 
            result['error-code'] = response.status_code
            result['error-text'] = response.text