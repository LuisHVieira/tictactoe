import discord
from discord.ext import commands

class Player (commands.Converter):
    async def convert(self, ctx, *args):

        #Jogadores 1 e 2 
        self.p1 = ctx.message.author    
        self.p2 = ctx.message.mentions[0]
        self.status_game = 0

        if self.p2.bot:
            return "BOT"

        elif len(args) == 1 and self.p1 != self.p2:

            self.status_game = 1

            return f'Jogadores -> [1] {self.p1.mention} VS [2] {self.p2.mention}'

        else:

            return "Inválido"