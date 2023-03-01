import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://sports.tipico.de/de"

headers = {"User-Agent":"Mozilla/5.0"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.title
print(title)

app = soup.find(id = "strong")
print(app)