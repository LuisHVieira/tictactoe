from discord.ext import commands

bot = commands.Bot(command_prefix="$")

@bot.command(name='play', help='Para jogar faça menção aos dois jogadores.', brief='Inicia o jogo')
async def play(ctx, *args):
	if len(args) == 2:
		players = []

		for arg in args:
			players.append(arg)


		response_players = "Player X: " + players[0] + "Player O: " +  players[1]
		await ctx.channel.send(response_players)

		#playing  get players function 

	else:
		await ctx.channel.send("Invalid Command") 


def run(token):
	return bot.run(token)




