#!/usr/bin/env python3
import json

import discord
import requests
from tabulate import tabulate

from scraper import scrape_crown_menu


class AshleighClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hi'):
            await message.reply(f'Hello there, {message.author.mention}!', mention_author=True)

        if message.content.startswith('!fakka'):
            await message.reply('Rustig bro', mention_author=True)

        if message.content.startswith('!test'):
            await message.reply('Hi, I am Ashleigh. Welcome to The Crown!', mention_author=True)
            
        if message.content.startswith("!order"):
            try:
                product = message.content.split(' ', 1)[1]

                if product == "biertje" or product == "beer":
                    await message.reply('Thank you for ordering a Hertog Jan!', mention_author=True)
                elif product == "cola":
                    await message.reply('Thank you for ordering a Coca Cola!', mention_author=True)
                elif product == "nuts":
                    await message.reply('Here you go, a bowl of nuts! 🥜🥜🥜', mention_author=True)
                elif not product:
                    await message.reply(f'What would you like to order?', mention_author=True)
                else:
                    await message.reply(f'I am sorry, we do not have {product}', mention_author=True)

            except IndexError:
                await message.reply(f'What would you like to order?', mention_author=True)

        if message.content.startswith("!tinder"):
            try:
                description = message.content.split(' ', 1)[1]
                await message.reply(f"Hmm, the profile description is {len(description)} characters long...", mention_author=True)
            except IndexError:
                await message.reply(f"No description? No wonder you don't get likes...", mention_author=True)

        if message.content.startswith("!menu"):
            menu = scrape_crown_menu()
            for tabs in menu:
                ascii_menu = tabulate(tabs[0], headers='keys', tablefmt='psql')

                await message.reply(tabs[0] + ':\n\n' + '```' +  ascii_menu + '```', mention_author=True)

                # await message.reply(tabs[0] + ':\n\n' + tabs[1].to_string(), mention_author=True)
                # await message.channel.send(tabs[1].to_json(), mention_author=True)

        if message.content == "!":
            await message.reply(f'How can I help you?', mention_author=True)

        if message.content.startswith('!inspire'):
            quote = self.get_quote()
            await message.channel.send(quote)

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return quote


if __name__ == '__main__':
    with open("token.txt", "r", encoding='utf-8') as F:
        token = F.read()

    # This bot requires the members and reactions intents.
    intents = discord.Intents.default()
    intents.members = True

    client = AshleighClient(intents=intents)
    client.run(token)
