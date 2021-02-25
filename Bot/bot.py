import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents(messages=True, guilds=True, members=True)
client = commands.Bot(command_prefix='$', help_command=None, intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} is online!')

@client.command()
async def say(ctx, message):
    await ctx.send(f'{message}')

@client.command()
async def hibot(ctx):
    await ctx.send(f'Hello')

client.run(TOKEN)
