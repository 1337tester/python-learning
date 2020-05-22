import discord

token = "NzExMTcwNzk5NjU4MjA1MTk0.Xr_Ing.Rd0hzkxWMfaSk6w9aMEJ1g4GGRM"
channel = 691319709252976723
# https://discord.com/api/oauth2/authorize?client_id=711170799658205194&permissions=198720&scope=bot

client = discord.Client()  # starts the discord client.

@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    dobrichlapci = client.get_channel(channel)
    if message.author == client.user:
        return
    elif str(message.author) == "1337tester#1082" and "hello" in message.content.lower():
        await message.channel.send('Hi!')
    elif str(message.author) == "bubaakk#1973":
        await message.channel.send('Drz picu Marek!')
    elif str(message.author) == "miron6931#6648":
        await message.channel.send('Drz picu Miron!')
    elif "!kickbot" == message.content.lower():
        await client.close()
    elif "bot.statusreport" == message.content.lower():
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


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


client.run(token)  # recall my token was saved!
