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

    p1, p2 = Player.get_players()
    player_symbol = dict(player = None, symbol = '', valid = False)

    if ctx.message.author == p2:
        player_symbol = g.move(row, col, 'x', p2)  
           
    elif ctx.message.author == p1:
        player_symbol = g.move(row, col, 'o', p1)
   
    
   
    if player_symbol['player'] != None and player_symbol['symbol'] != '':
        if player_symbol['valid']:
            await ctx.send(g.check_game(player_symbol['player'], player_symbol['symbol']))
        else:
            await ctx.send(f'Jogada | Posição Inválida')

        await ctx.send(f'{g.paint()}')
    else:
        await ctx.send(f'Jogador Inválido!!!')


    if g.end == True:
        g.reset()


    
    
    


        
        

   




