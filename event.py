import pandas as pd
import numpy as np
from api_calling import OddsApiCaller
import json

class Event: 
    def __init__(self):
        self.data = pd.read_json('odds.json') # TODO: should be a paramater and the __init__ should receive it from the main 

    def parse_df(self):
        event_outcomes = []
        events = self.data['bookmakers']
        # print(events)
        # print(events[3])
        for event in events:
            # print(f"{len(event)} \n\n\n")
            # print(event[2]['markets'][0]['outcomes']
            for count_bookmaker in range(len(event)):
                # print(count_bookmaker)
                # print(f"{event[count_bookmaker]['title']}\n")
                num_outcomes = len(event[count_bookmaker]['markets'][0]['outcomes'])
                for outcome in range(num_outcomes):
                    bookmaker_odds = round(float(event[count_bookmaker]['markets'][0]['outcomes'][outcome]['price']), 2) # prize round to 2 decimals
                    odd_name = event[count_bookmaker]['markets'][0]['outcomes'][outcome]['name'] # Name of team of the current quota
                    event_outcomes.append([event[count_bookmaker]['title'], odd_name, bookmaker_odds])
                    # print(bookmaker[1]['title'])
                    # if bookmaker_odds > current_best_odds:
                    #     best_odds[outcome][0] = bookmaker['titles']
        
        print(event_outcomes)

# TODO: find algorithm that splits the odds, find the best and returns a list like this: [bookmaker, name, price]


def main():
    x = Event()
    x.parse_df()

if __name__ == '__main__':
    main()