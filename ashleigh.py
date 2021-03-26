#!/usr/bin/env python3
import discord
from discord.ext import commands
from tabulate import tabulate

from assets import get_quote, get_product_information
from scraper import scrape_crown_menu

bot = commands.Bot(command_prefix='!')


@bot.command()
async def test(ctx):
    await ctx.channel.send("Hi, I am Ashleigh. Welcome to The Crown!", mention_author=True)


@bot.command(
    help="Prints pong as a response to the user's ping.",
    brief="Prints pong as a response to the user's ping."
)
async def ping(ctx):
    await ctx.channel.send("pong", mention_author=True)


@bot.command(
    help="In need of inspiration? Call for a quote using this command!",
    brief="Prints an inspiring quote."
)
async def inspire(ctx):
    await ctx.channel.send(get_quote(), mention_author=True)


@bot.command(
    help="Orders the requested drink.",
    brief="Order your favourite drink using this command!"
)
async def order(ctx):
    await ctx.channel.send("I am sorry, this function needs to be reimplemented!", mention_author=True)


@bot.command(
    help="Display the menu of Cafe the Crown.",
    brief="Find your favourite drinks here!"
)
async def menu(ctx):
    menu = scrape_crown_menu()

    for tabs in menu:
        ascii_menu = tabulate(tabs[1], headers='keys', tablefmt='psql')
        await ctx.channel.send(tabs[0] + ':\n\n' + '```' + ascii_menu + '```', mention_author=True)


@bot.command(
    help="Need some feedback on your Tinder description? Let Ashleigh take a look!",
    brief="Let Ashleigh take a look at your Tinder description."
)
async def tinder(ctx, description):
    try:
        await ctx.channel.send(f"Hmm, the profile description is {len(description)} characters long...",
                               mention_author=True)
    except IndexError:
        await ctx.channel.send(f"No description? No wonder you don't get likes...", mention_author=True)


if __name__ == '__main__':
    with open("token.txt", "r", encoding='utf-8') as F:
        token = F.read()

    bot.run(token)
