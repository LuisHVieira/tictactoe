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
    
    if g.end == -1:

        if isinstance(players, Player):
            p1, p2 = players.get_players()
            g.end = 0
            await ctx.send(f'Jogadores -> [X] {p1.mention} VS [O] {p2.mention}')

        else:
            err = players
            await ctx.send(err)
    else:
        await ctx.send(f'Jogo em andamento!')


@bot.command(name = 'move', help = "Posição do tabuleiro EX: (1, 1)", enabled = True)
async def move(ctx, *args):    

    row = int(args[0])
    col = int(args[1])

    p1, p2 = Player.get_players()
    player_symbol = dict(player = None, symbol = '', valid = False)

    if ctx.message.author == p1:
        player_symbol = g.move(row, col, 'x', p1)  
           
    elif ctx.message.author == p2:
        player_symbol = g.move(row, col, 'o', p2)
   
   
    if player_symbol['player'] != None and player_symbol['symbol'] != '':
        if player_symbol['valid']:
            status = g.check_game(player_symbol['player'],  player_symbol['symbol'])
            await ctx.send(status)
        else:
            await ctx.send(f'Jogada | Posição Inválida')


        g.paint()
        
        file = discord.File('env/img/c_board.png', filename="c_board.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://c_board.png")
        embed.title = 'Round #' + str(g.rounds)
        
        await ctx.send(file=file, embed=embed)

    else:
        await ctx.send(f'Jogador Inválido!!!')


    if g.end == 1:
        g.reset()


    
    
    


        
        

   




