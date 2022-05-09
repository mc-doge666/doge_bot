import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '/')

@bot.event
async def on_ready():
    print(">> Bot is online")

bot.run('OTczMTIxODEzMTUwMzAyMjM4.GWMg48.AQDYsNECs9bGjoxn0P-6JapQHSKfBt-9Odn1Og')