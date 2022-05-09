import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '/')

@bot.event
async def on_ready():
    print(">> Bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(973131573820018698)
    await channel.send(F'{member} join! ')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(9973131716766097429)
    await channel.send(F'{member} leave! ')

bot.run('OTczMTIxODEzMTUwMzAyMjM4.GWMg48.AQDYsNECs9bGjoxn0P-6JapQHSKfBt-9Odn1Og')