import pandas as pd
import numpy as np
from api_calling import OddsApiCaller

class Event: 
    def __init__(self):
        self.data = pd.read_json('odds.json') # TODO: should be a paramater and the __init__ should receive the data from the main-function 

    def list_of_best_odds(self):
        all_best_odds = []
        events = self.data['bookmakers']
        for event in events:
            for count_bookmaker in range(len(event)):
                num_outcomes = len(event[count_bookmaker]['markets'][0]['outcomes'])
                best_odds = [[None, None, float('-inf')] for _ in range(num_outcomes)]
                for outcome in range(num_outcomes):
                    bookmaker_odds = round(float(event[count_bookmaker]['markets'][0]['outcomes'][outcome]['price']), 2) # price round to 2 decimals
                    current_best_odd = best_odds[outcome][2]

                    if bookmaker_odds > current_best_odd:
                        best_odds[outcome][0] = event[count_bookmaker]['title']
                        best_odds[outcome][1] = event[count_bookmaker]['markets'][0]['outcomes'][outcome]['name']
                        best_odds[outcome][2] = bookmaker_odds
            all_best_odds.append(best_odds)
        return all_best_odds

    def calculate_arbitrage_bets(self):
        pass


def main():
    x = Event()
    x.list_of_best_odds()

if __name__ == '__main__':
    main()