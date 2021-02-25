import os
import discord
from discord.ext import commands

TOKEN = os.env.get("BOT_TOKEN")

intents = discord.Intents(messages=True, guilds=True, members=True)
client = commands.Bot(command_prefix='$', help_command=None, intents = intents)

@client.event
async def on_ready():
    print(f'{self.client.user} is online!')

@client.command()
async def say(ctx, message):
    await ctx.send(f'{message}')

@client.command()
async def hibot(ctx):
    await ctx.send(f'Hello')


client.start(TOKEN)