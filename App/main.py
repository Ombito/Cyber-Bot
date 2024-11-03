import discord
import os
from discord.ext import commands
import random
from dotenv import load_dotenv


load_dotenv()


intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command(name='info')
async def info(ctx):
    info_message = (
        "I'm a simple Discord bot created to assist you!\n"
        "Here are some commands you can use:\n"
        "$hello - Greet me!\n"
        "$ping - Check if I'm alive!\n"
        "$info - Learn more about me."
    )
    await ctx.send(info_message)


TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    raise ValueError("No TOKEN found in environment variables.")
    
bot.run(TOKEN)

