from bs4 import BeautifulSoup
import requests


google = requests.get("https://trends.google.com/trends/?geo=IT", headers={'User-Agent': 'Mozilla/5.0'})
soup2 = BeautifulSoup(google.content, "html.parser")
print(soup2.select(“div#result-stats”))
##
##result_number = soup2.find(id="result-stats")
##print(result_number)
