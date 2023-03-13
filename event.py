import pandas as pd
import numpy as np
from api_calling import OddsApiCaller
import math

class Event: 
    def __init__(self):
        self.data = pd.read_json('odds.json') # TODO: should be a paramater and the __init__ should receive the data from the main-function 

    def list_of_best_odds(self) -> list:
        all_best_odds = []
        events = self.data['bookmakers']
        for event in events:
            print(event)
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

    def find_arbitrage_bets(self) -> list:
        outcomes = self.list_of_best_odds()
        arbitrage_bets = []
        for outcome in outcomes:
            probability = 0.0
            for num_outcome in range(len(outcome)):
                probability = probability + (1.0 / outcome[num_outcome][2])
            if (probability < 1.0):
                arbitrage_bets.append(outcome)

        return arbitrage_bets


def main():
    x = Event()
    x.find_arbitrage_bets()

if __name__ == '__main__':
    main()