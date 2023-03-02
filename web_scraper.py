import pandas as pd
import requests
# python -m pipreqs.pipreqs . --force in current file for filling requirements.txt

# URL location -> Developer Tools -> Network -> try and error until response is correct 
url = "https://sports.tipico.de/json/program/hourEvents/2?oneSectionResult=true&language=de&isLoggedIn=0&licenseRegion=DE&maxMarkets=5"

# response object of upcoming events. important things: events, matchoddgroups
# events object contains list of id's. each id is a footbal match with the name of both teams, etc...
# matchoddgroups object contains a list of id's (identical of what are in events). each id is the footbal match with all betting options 

headers = {"User-Agent":"Mozilla/5.0"}
upcoming_events = requests.get(url, headers=headers) # full object of upcoming events, headers simulate a real browser not a programm without headers status_code=403
print(upcoming_events.json()) 
