from player import Player
from xo.board import Board
import discord
from discord.ext import commands

class Game:
    board = Board.fromstring()
    row  = -1
    col = -1

    @classmethod
    def move(cls, row:int, col:int, symbol:str):

        for r, c, piece in cls.board:
            if  r == row and c == col and piece == ' ':
                cls.board[r, c] = symbol

    @classmethod
    def paint(cls):
         return cls.board



