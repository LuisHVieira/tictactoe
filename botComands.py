import discord
from discord.ext import commands
from config import Config as c
from playerCommand import *
from player import Player
from game import Game as g

intents = discord.Intents.default()

prefix = "$"
bot = c.createBot(prefix, intents)

@bot.command(name = 'play', help = "Desafia o jogador mencionado ( apenas 1 )", enabled = True)
async def play(ctx, *, players: PlayerCommand):    
    
    if isinstance(players, Player):
        p1, p2 = players.get_players()
        await ctx.send(f'Jogadores -> [1] {p1.mention} VS [2] {p2.mention}')
        ctx.command.enabled = False

    else:
        err = players
        await ctx.send(err)


@bot.command(name = 'pos', help = "Desafia o jogador mencionado ( apenas 1 )", enabled = True)
async def pos(ctx, *args):    

    row = int(args[0])
    col = int(args[1])

    g.move(row, col, 'x')

    await ctx.send(f'{g.paint()}')
    


        
        

   




