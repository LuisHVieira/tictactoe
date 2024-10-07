import json 
from discord.ext import commands

class Config:

    discord = ""
    server = ""
    bot = None

    @classmethod
    def getTokens(cls, path):
        try:
            
            tokens_archive = open(path)
            data = json.load(tokens_archive)
            
            cls.discord = data['discord_token']
            cls.server = data['server_name']
            
        except Exception as e:
            print(e)
    

    @classmethod
    def createBot(cls, prefix:str, intents):
        cls.bot = commands.Bot(command_prefix=prefix, intents=intents) 
        return cls.bot

    @classmethod
    def runBot(cls):
        print('Running...')
        return cls.bot.run(cls.discord)

    


    


    

   
        
        
  

    