import discord
import requests
import sys
from discord.ext import commands


token = "NzExMTcwNzk5NjU4MjA1MTk0.XskXdw.jcJp1gvBDbxbnls9SYMKYnprxZk"
channel = 691319709252976723
# https://discord.com/api/oauth2/authorize?client_id=711170799658205194&permissions=198720&scope=bot

client = discord.Client()  # starts the discord client.

def crypto_price(crypto = "XMREUR"):
    """Getting the currency pair from kraken.com"""
    response = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={crypto}")
    json = response.json()
    print(json)
    pair = f'X{crypto[:3]}Z{crypto[3:]}'
    price = json['result'][pair]['c'][0]
    return price


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.
    """Waiting on messages"""
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    # dobrichlapci = client.get_channel(channel)

    if message.author == client.user:
        return
    elif message.content.lower() in ("bot.logout", "bot.exit"):
        await message.channel.send('Exiting')
        await client.close()
    elif "bot.report" == message.content.lower():
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
        await message.channel.send(f"\n```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")
    elif "bot.crypto." == message.content.lower()[:11]:
        pair = message.content.lower()[11:]
        print(pair)
        await message.channel.send(f'Crypto price of {pair} is {crypto_price("XMREUR")}')
    elif "bot.help" == message.content.lower():
        await message.channel.send("""
        bot.crypto.XXXYYY   - getting crypto pair XXXYYY from kraken.com
        bot.exit            - exit bot
        bot.help            - show this help
        bot.logout          - exit bot
        bot.report          - status of members
        """)
    # elif str(message.author) == "1337tester#1082":
    #     await message.channel.send('Poculi ste slovo PANA')
    elif str(message.author) == "bubaakk#1973":
        await message.channel.send('Drz picu Marek!')
    elif str(message.author) == "miron6931#6648":
        await message.channel.send('Drz picu Miron!')
    else:
        await message.channel.send("other")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(token)  # recall my token was saved!
