import discord
from discord.ext import commands
from config import Config as c
from Player import *

intents = discord.Intents.default()

prefix = "$"
bot = c.createBot(prefix, intents)

@bot.command()
async def test(ctx, *, reason: Player):
    await ctx.send(reason)
    

