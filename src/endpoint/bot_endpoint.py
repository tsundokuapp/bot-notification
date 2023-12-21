import logging
import os
from dotenv import load_dotenv

import discord
from discord import option

#Carregando as variaveis de ambiente
load_dotenv()
token = os.getenv('API_KEY')

bot = discord.Bot()

@bot.command(description="Envia a Latência") 
async def ping(ctx):
    await ctx.respond(f"Calma garai, tô vivo. Latência: {round(bot.latency, 3)} ms")

bot.run(token)