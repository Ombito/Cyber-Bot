import discord
import os
from discord.ext import commands
import random
from dotenv import load_dotenv
import openai

load_dotenv()


intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

openai.api_key = os.getenv('OPENAI_API_KEY')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

    if any(word in message.content.lower() for word in ['badword1', 'badword2']):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, your message contained prohibited content and has been deleted.")




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
        "Here are some commands you can use:\n\n"
        "$hello - Greet me!\n"
        "$ping - Check if I'm alive!\n"
        "$info - Learn more about me."
    )
    await ctx.send(info_message)

@bot.command(name='ask')
async def ask(ctx, *, question: str = None):
    if question is None:
        await ctx.send("Please provide a question after the command. Usage: `$ask <your question>`")
        return
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        answer = response['choices'][0]['message']['content']
        await ctx.send(answer)
    except Exception as e:
        await ctx.send("Sorry, I couldn't process your request.")


# @bot.command(name='ask')
# async def ask(ctx, *, question: str = None):
#     if question is None:
#         await ctx.send("Please provide a question after the command. Usage: `$ask <your question>`")
#         return
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": question}]
#         )
#         answer = response['choices'][0]['message']['content']
#         await ctx.send(answer)
#     except Exception as e:
#         await ctx.send(f"Sorry, I couldn't process your request")



TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    raise ValueError("No TOKEN found in environment variables.")
    
bot.run(TOKEN)

