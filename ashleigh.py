#!/usr/bin/env python3
import random
import discord

from discord.ext import commands
from tabulate import tabulate

from assets import get_inspiring_quote, get_product_information, get_star_wars_quote, get_joke
from scraper import get_available_sections, get_crown_menu_section, scrape_crown_menu, CrownScraperCog

bot = commands.Bot(command_prefix='/')

bot.add_cog(CrownScraperCog())

@bot.command(
    help="A simpele query to test if the bot works.",
    brief="Test if Ashleigh is operating succesfully."
)
async def test(ctx):
    await ctx.message.reply("Hi, I am Ashleigh. Welcome to The Crown!", mention_author=True)


@bot.command(
    help="Prints pong as a response to the user's ping.",
    brief="Prints pong as a response to the user's ping."
)
async def ping(ctx):
    await ctx.message.reply("pong", mention_author=True)


@bot.command(
    help="In need of inspiration? Call for a quote using this command!",
    brief="Prints an inspiring quote."
)
async def inspire(ctx):
    await ctx.message.reply(get_inspiring_quote(), mention_author=True)

# @bot.command()
# async def force(ctx):
#     await ctx.channel.send(get_star_wars_quote(), mention_author=True)


@bot.command(
    help="Orders the requested drink.",
    brief="Order your favourite drink using this command!"
)
async def order(ctx, *, content):
    await ctx.message.reply("I am sorry, this function needs to be reimplemented!", mention_author=True)


@bot.command(
    help="Feeling thirsty? Ask ashleigh about the menu.",
    brief="Find your favourite drinks here!"
)
async def menu(ctx, *, category):
    menu_sections = get_available_sections()

    if not category:
        menu_headers = ", ".join([section for section in menu_sections])
        menu_headers = ' and '.join(menu_headers.rsplit(', ', 1))

        await ctx.message.reply('Hi there, what can i get for you?\n'+'We have: ' + menu_headers)
    else:
        section_name = category[0].lower()

        if section_name in menu_sections:
            section = get_crown_menu_section(section_name)

            ascii_menu = tabulate(section, headers='keys', tablefmt='psql')

            await ctx.message.reply(section_name + ':\n\n' + '```' + ascii_menu + '```', mention_author=True)

        

@bot.command(
    help="Want to cheer your day up with some jokes? Ask Ashleigh!",
    brief="Let Ashleigh tell you a joke."
)
async def joke(ctx):
    await ctx.message.reply(get_joke())

@bot.command(
    help="Need some feedback on your Tinder description? Let Ashleigh take a look!",
    brief="Let Ashleigh take a look at your Tinder description."
)
async def tinder(ctx, *, description):
    if not description:
        await ctx.message.add_reaction('🤷‍♂️')
        await ctx.message.reply(f"No description? No wonder you don't get likes...")

    if len(description) < 20:
        responses = [
            "Hmm, that's a small description. Is that the only thing small about you?",
            "Not a lot of words, eh? Or do I make you speechless?",
            "Tiny description...  don't tell me you are compensating 😏"
        ]
        await ctx.message.add_reaction('👍')
        await ctx.message.reply(random.choice(responses))
    else:
        await ctx.message.add_reaction('👍')
        await ctx.message.reply(f"Hmm, the profile description is {len(description)} characters long...")


@bot.command(
    help="Ask Ashleigh something trivial!",
    brief="Ask Ashleigh something trivial!"
)
async def query(ctx, *, content):
    await ctx.message.reply("I am sorry, this function needs to be (re)implemented!", mention_author=True)


def to_upper(argument):
    return argument.upper()


@bot.command(
    help="Display the menu of Cafe the Crown.",
    brief="Find your favourite drinks here!"
)
async def up(ctx, *, content: to_upper):
    await ctx.message.reply(content)


def get_quip():
    with open("quips.txt") as F:
        quips = F.readlines()
    return random.choice(quips)


# @bot.command(
#     help="",
#     brief=""
# )
# async def robert(ctx):
#     await ctx.message.reply(get_quip())



# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="thirsty customers"))
    print('Ashleigh is ready for action!')


@bot.event
async def on_command_error(ctx, error):
    responses = [
        f"Aww, I cannot help you with that! Maybe Google it?",
        f"That's a bit too much for my paygrade, maybe someone else can help you!",
        f"Sorry there, that's too difficult for me :(",
        f"Oh dear, I don't know really. You could ask the regulars for more information.",
        f"Wait, what?",
        f"I dunno, could you rephrase it?"
    ]
    await ctx.message.reply(random.choice(responses))


# class Greetings(commands.Cog):
#     pass


if __name__ == '__main__':
    with open("token.txt", "r", encoding='utf-8') as F:
        token = F.read()

    bot.run(token)

