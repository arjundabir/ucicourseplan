import requests
import json
from bs4 import BeautifulSoup

url = "https://catalogue.uci.edu/thepaulmerageschoolofbusiness/accounting_minor/" + \
    "#requirementstext"

json_data = []

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


def find_table():
    table = soup.find_all('table', class_='sc_courselist')
    for index, table in enumerate(soup.find_all("table")):
        if (index == 0):
            print("prereq")
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) == 2:
                course_id = tds[0].text.strip()
                course_title = tds[1].text.strip()
                course_link = "https://catalogue.uci.edu/" + \
                    tds[0].find('a')['href']

                print(
                    f"Course ID: {course_id}, Course Title: {course_title}, Course Link: {course_link}")

    #


print(find_table())
