import discord
import requests
import sys, os
from discord.ext import commands

fileDir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(fileDir, "token.txt")) as file:
    token = file.read()

channel = 691319709252976723
# https://discord.com/api/oauth2/authorize?client_id=711170799658205194&permissions=198720&scope=bot

bot = commands.Bot(command_prefix='bot.')

def crypto_price(crypto = "XMREUR"):
    """Getting the currency pair from kraken.com"""
    crypto = crypto
    response = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={crypto}")
    json = response.json()
    pair = f'X{crypto[:3]}Z{crypto[3:]}'
    price = json['result'][pair]['c'][0]
    return price

@bot.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'{bot.user} ready to roll')  # notification of login.
    # await dobrichlapci.send(f'{bot.user} ready to roll')

# @bot.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
# async def on_message(message):
#     if "bot." == message.content.lower()[:3]:
#         print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='text', help='Basic text write')
async def nine_nine(ctx, text='default text'):
    await ctx.send(text)

@bot.command(name='exit', help='Closes the bot')
async def nine_nine(ctx):
    await ctx.send('Exiting')
    await bot.close()

@bot.command(name='report', help='Getting channel members report')
async def crypto(ctx, pair: str):
    dobrichlapci = bot.get_channel(channel)
    online = 0
    idle = 0
    offline = 0
    for m in dobrichlapci.members:
        if str(m.status) == "online":
            online += 1
        if str(m.status) == "offline":
            offline += 1
        else:
            idle += 1
    await ctx.channel.send(f"\n```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")

@bot.command(name='crypto', help='Getting crypto pairs from kraken.com and printing them in channel')
async def crypto(ctx, pair: str):
    pair = pair.upper()
    await ctx.channel.send(f'Crypto price of {pair} is {crypto_price(pair)}')

bot.run(token)
