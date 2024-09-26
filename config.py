import json 

class Tokens():

    discord = ""
    server = ""

    @classmethod
    def getTokens(cls, path):
        try:
            
            tokens_archive = open(path)
            data = json.load(tokens_archive)
            
            cls.discord = data['discord_token']
            cls.server = data['server_name']
            
        except Exception as e:
            print(e)
    

   
        
        
  

    