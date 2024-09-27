from Player import *


class Game:
    
    p1 = None
    p2 = None

    def __init__(self, bot):
        self.bot = bot


    @classmethod
    def setPlayers(cls, context):
        
        cls.p1 = Player(1, "nome1")
        cls.p2 = Player(2, "nome2")


