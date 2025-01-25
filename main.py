import discord, os, logic as l, Ambiente as Am
from dotenv import load_dotenv
from discord.ext import commands
import commandapi as c
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

@bot.command(name='meme')
async def img_meme(ctx):
    x = l.meme()
    await ctx.send(file = x)

@bot.command(name='memes')
async def img_memes(ctx):
    x = l.memes()
    await ctx.send(file = x)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = c.get_duck_image_url()
    await ctx.send(image_url)
@bot.command('eco')
async def ecology(ctx,opcion:int):
    if opcion== 1:
        await ctx.send(embed=Am.etiqueta_reciclar())
    elif opcion== 2:
        await ctx.send(embed=Am.etiqueta_reducir())
    elif opcion== 3:
        await ctx.send(embed=Am.etiqueta_reutilizar())
    else: 
        await ctx.send("opcion invalid")


bot.run(token)