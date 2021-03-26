#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import pandas as pd
from functools import lru_cache

@lru_cache(10)
def scrape_crown_menu():
    r = requests.get('https://www.cafethecrown.nl/assortiment/')

    soup = BeautifulSoup(r.text, features="lxml")

    tabs = [(tab.text, tab['href'][1:]) for tab in soup.find('ul', class_="tab-nav").findAll('a', href=True)]

    tables = []

    for tab in tabs:
        tab_title = tab[0]
        table_id = tab[1]

        df = pd.DataFrame(columns=['Title', 'Price'])

        rows = soup.find('div', id=table_id).find('table').find('tbody').findAll('tr')

        for row in rows:
            title = row.find('td', class_='column-1').text
            price = '€' + row.find('td', class_='column-2').text

            df = df.append({'Title' : title, 'Price' : price}, ignore_index=True)

        tables.append((tab_title, df))

    return tables