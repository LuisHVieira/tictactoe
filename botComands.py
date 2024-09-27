import discord
from discord.ext import commands
from config import Config as c

intents = discord.Intents.default()

prefix = "$"
bot = c.createBot(prefix, intents)
c.setBot(bot)

@bot.command()
async def test(ctx, *args):
    await ctx.send(f'{len(args)} arguments: {args}')
    

