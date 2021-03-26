#!/usr/bin/env python3
import discord
from discord.ext import commands

from assets import get_quote, get_product_information

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
    help="In need of inspiration? Call for a quote using this command!",
    brief="Prints an inspiring quote."
)
async def order(ctx, product):
    pass


if __name__ == '__main__':
    with open("token.txt", "r", encoding='utf-8') as F:
        token = F.read()

    bot.run(token)
