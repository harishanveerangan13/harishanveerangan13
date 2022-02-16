from bs4 import BeautifulSoup
import requests

url = "https://html.com/"

kws = requests.get(url)

doc = BeautifulSoup(kws.text, "lxml")

resultz = doc.find("h")
print(resultz)
