import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '/')

@bot.event
async def on_ready():
    print(">> Bot is online")

@bot.event
async def on_member_join(member):
    print(F'{member} join!')

bot.run('OTczMTIxODEzMTUwMzAyMjM4.GWMg48.AQDYsNECs9bGjoxn0P-6JapQHSKfBt-9Odn1Og')