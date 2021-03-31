# essentials
import discord
import random
import json
import os

os.chdir("C:\Users\deepa\OneDrive\Desktop\DISCORD BOT")

from discord.ext import commands

# prefix
client = commands.Bot(command_prefix = '!')

# Bot is ready msg
@client.event
async def on_ready():
    print('Bot is online!')


# clearing msgs
@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit =  amount)
