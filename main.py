import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix = ";")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.command()
async def balance(ctx):
  await open_account(ctx.author)
  user = ctx.author
  users = await get_bank_data()

  account_amt = users[str(user.id)]["bank"]
  
  embed = discord.Embed(title = f"{ctx.author.name}`s balance")
  embed.add_field(name = "Account", value = account_amt)
  await ctx.send(embed = embed)

async def open_account(user):
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["bank"] = 0

  with open ("bank.json", "w") as f:
    json.dump(users,f)
  return True;

async def get_bank_data():
  with open ("bank.json", "r") as f:
    users = json.load(f)
  return users
  
client.run("OTYyOTI1NjYwNDY3MjYxNDgw.YlOoZw.0evhFloaKhWPbP5RI8iQNOPn7y0")