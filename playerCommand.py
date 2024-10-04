import discord
from discord.ext import commands
from player import Player

class PlayerCommand (commands.Converter):
    async def convert(self, ctx, *args):

        #Jogadores 1 e 2 
        self.p1 = ctx.message.author    
        self.p2 = ctx.message.mentions[0]

        try:
            if ctx.command.enabled:

                if not ( self.p2.bot ):

                    if len(args) == 1 and self.p1 != self.p2:

                        player = Player()
                        player.set_players(self.p1, self.p2)
                  
                        return player

                    else:

                        raise Exception(' Jogador Inválido! ( Limite 1 ) ')

                else:
                        
                    raise Exception(' BOT não são jogáveis ')
                    

        except Exception as e:
            return 'ERRO! ' +  e.args[0]

