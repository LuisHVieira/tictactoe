from discord.ext import commands

bot = commands.Bot(command_prefix="$")
players = []

@bot.command(name='play', help='Para jogar faça menção aos dois jogadores.', brief='Inicia o jogo')
async def play(ctx, *args):
	if len(args) == 2:

		for arg in args:
			players.append(arg)


		if players[0] != players[1]:			

			response_players = "Player X: " + players[0] + "Player O: " +  players[1]
			await ctx.channel.send(response_players)

		else:
			await ctx.channel.send('Invalid Players')

		#playing  get players function 	

	else:
		await ctx.channel.send("Invalid Command") 


@bot.listen('on_message')
async def gameplay(message):
	if message.content == "Player X: " + players[0] + "Player O: " +  players[1]:
		await message.channel.send(players[0] + ' faça sua jogada: ')

	


def run(token):
	return bot.run(token)



