#!/usr/bin/env python3
import json

import requests


def get_inspiring_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = f""""{json_data[0]['q']}" - {json_data[0]['a']}"""  # json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


def get_star_wars_quote():
    response = requests.get("https://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote")
    json_data = json.loads(response.text)
    quote = json_data[0]['content']
    return quote


def get_product_information():
    pass