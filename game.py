from player import Player
from xo.board import Board
from xo import arbiter
import discord
from discord.ext import commands

class Game:
    board = Board.fromstring()
    row  = -1
    col = -1
    rounds = 0
    end = False

    @classmethod
    def move(cls, row:int, col:int, symbol:str, player:Player):

        if row in range(1, 4) and col in range (1,4):
            if player != None:
                for r, c, piece in cls.board:
                    if  r == row and c == col and piece == ' ':
                        cls.board[r, c] = symbol

                        arb = arbiter.outcome(cls.board, symbol)

                        if arb['status'] != 'invalid':
                            return dict(player = player, symbol = symbol, valid = True )
                        else:
                            cls.board[r, c] = ' '
            
        return dict(player = player, symbol = symbol, valid = False )

    @classmethod 
    def check_game(cls, player:Player, symbol:str):
        arb = arbiter.outcome(cls.board, symbol)
        print(arb)

        if arb['status'] == 'gameover':
            if arb['reason'] == 'winner':
                cls.end = True
                return f'Vencedor!!! {player.mention}'
            else:
                cls.end = True
                return f'#Jogo Empatado#'
        else:
            cls.rounds = cls.rounds + 1
            return f'Round {cls.rounds}: '

    @classmethod
    def reset(cls):
        for r, c, piece in cls.board:
            cls.board[r, c] = ' '

        Player.set_players(None, None)
        cls.end = False

    @classmethod
    def paint(cls):
         return cls.board



