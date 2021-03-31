# essentials
import discord
import random
import math
import json
import os



from discord.ext import commands

# prefix
client = commands.Bot(command_prefix = '!')

# On ready msg
@client.event
async def on_ready():
    print('Bot is online!')




# clearing msgs
@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit =  amount)



# Economy system

@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]


    em = discord.Embed(title = f'{ctx.author.name} balance', color = discord.Color.red())
    em.add_field(name = "Wallet Balance", value = wallet_amt)
    em.add_field(name = "Bank Balance", value = bank_amt)
    await ctx.send(embed = em)


@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    
    users = await get_bank_data()

    user = ctx.author
    
    earnings = random.randrange(501)

    await ctx.send(f'Someone gave you {earnings} coins!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)


async def open_account(user):

    users = await get_bank_data()


    if str(user.id) in users:
        return False
    else:

        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users

    

# bot token
client.run('your token here')
