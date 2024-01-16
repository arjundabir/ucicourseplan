import requests
from bs4 import BeautifulSoup
import json
import json

json_data = []

with open('links.json') as file:
    data = json.load(file)

for item in data:
    response = requests.get(item["uri"])
    soup = BeautifulSoup(response.content, 'html.parser')
    page_title = soup.find('h1', class_='page-title').text.strip()
    json_data.append({
        "title": page_title,
        "uri": item["uri"]
    })
    print(json_data[-1])

with open("links-with-title.json", "w") as f:
    json.dump(json_data, f, indent=4)
