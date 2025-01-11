import discord, os, logic as l
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='_', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name="psw")
async def contra(ctx, length = 25):
    x = l.password(length)
    await ctx.send(f"su contraseña es:{x}")

@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
@bot.command(name='eleccion')
async def elegir(ctx,*elecciones: str):
    """Is the bot cool?"""
    await ctx.send(f"{l.elegir(elecciones)}")

bot.run(token)
