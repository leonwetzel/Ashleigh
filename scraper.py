#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import pandas as pd
from functools import lru_cache
import os

MENU_DIRECTORY = 'menu'

def section_to_path(section):
    global MENU_DIRECTORY

    path = os.path.join(MENU_DIRECTORY, section.lower().replace(' ', '_')) + '.csv'

    return path

def get_available_sections():
    global MENU_DIRECTORY

    files = os.listdir(MENU_DIRECTORY)
    sections = [section.replace('.csv', '').replace('_', ' ') for section in list(filter(lambda f: f.endswith('.csv'), files))]

    return sections

def scrape_crown_menu():
    global MENU_DIRECTORY

    if not os.path.exists(MENU_DIRECTORY):
        os.mkdir(MENU_DIRECTORY)

    r = requests.get('https://www.cafethecrown.nl/assortiment/')

    soup = BeautifulSoup(r.text, features="lxml")

    tabs = [(tab.text, tab['href'][1:]) for tab in soup.find('ul', class_="tab-nav").findAll('a', href=True)]

    for tab in tabs:
        tab_title = tab[0]
        table_id = tab[1]

        df = pd.DataFrame(columns=['Title', 'Price'])

        rows = soup.find('div', id=table_id).find('table').find('tbody').findAll('tr')

        for row in rows:
            title = row.find('td', class_='column-1').text
            price = '€' + row.find('td', class_='column-2').text

            df = df.append({'Title' : title, 'Price' : price}, ignore_index=True)

        df.to_csv(section_to_path(tab_title), index=False)

def get_crown_menu_section(section):
    path = section_to_path(section)

    try:
        df = pd.read_csv(path)

        return df
    except IOError as e:
        print(e)
        return None