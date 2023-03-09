import pandas as pd
import numpy as np
from api_calling import OddsApiCaller
import json

class Event: 
    def __init__(self):
        self.data = pd.read_json('odds.json') # TODO: should be a paramater and the __init__ should receive it from the main 

    # def find_odds(self):
    #     # print(type(self.data))
    #     print(self.data['bookmakers'][0][0]['markets'][0]['outcomes'][0])
    #     # number of possible outcomes for a sporting event
    #     num_outcomes = len(self.data['bookmakers'][0][0]['markets'][0]['outcomes'])
    #     self.num_outcomes = num_outcomes
    #     # print(num_outcomes)
    #     # [Bookmaker, Name, Price]
    #     best_odds = [[None, None, float('-inf')] for _ in range(num_outcomes)]

    #     bookmakers = self.data['bookmakers']
    #     for bookmaker in bookmakers:
    #         for outcome in range(num_outcomes):
    #             bookmaker_odds = round(float(bookmaker[0]['markets'][0]['outcomes'][outcome]['price']), 2)
    #             current_best_odds = best_odds[outcome][2]
    #             print(bookmaker[0]['title'])
    #             # if bookmaker_odds > current_best_odds:
    #             #     best_odds[outcome][0] = bookmaker['titles']


# TODO: find algorithm that splits the odds, find the best and returns a list like this: [bookmaker, name, price]


def main():
    x = Event()
    x.find_odds()

if __name__ == '__main__':
    main()