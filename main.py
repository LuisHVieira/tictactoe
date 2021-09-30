from discord.ext import commands
import json 
import functions_commands as fc

#archive with tokens
archive = open('tokens.json', )
data = json.load(archive)

#disc tokens
tokenDisc = data['discord_token']
serverName = data['server_name']


"""@bot.command(name='ping')
async def teste(ctx):
	await ctx.channel.send(ctx.author.mention)"""
	
fc.run(tokenDisc)