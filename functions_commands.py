from discord.ext import commands

bot = commands.Bot(command_prefix="$")
players = []

@bot.command(name='play', help='Para jogar faça menção aos dois jogadores.', brief='Inicia o jogo')
async def play(ctx, *args):

	global status
	status = 0

	if len(args) == 2:

		for arg in args:
			players.append(arg)

		if players[0] != players[1]:			

			response_players = "Player X: " + players[0] + "Player O: " +  players[1]
			await ctx.channel.send(response_players)
			status = get_status(1)

		else:
			await ctx.channel.send('Invalid Players')

		#playing  get players function 	

	else:
		await ctx.channel.send("Invalid Command") 


@bot.listen('on_message')
async def gameplay(message):

	rounds = 0

	if message.content == "Player X: " + players[0] + "Player O: " +  players[1]:
		await message.channel.send(players[0] + ' faça sua jogada: ')

	msg_mention = mention(message.author.mention)

	if status == 1:
		if rounds % 2 == 0:
			if msg_mention == players[0]:
				print('te')

		else:
			if message.author.mention == players[1]:
				pass
	

def mention(msg_mention):
	split_msg_metion = msg_mention.split('@')
	add_mention = ''
	for pos, splits in zip(range(len(split_msg_metion)), split_msg_metion):
		if pos == 1:
			add_mention += '@!'

		add_mention += splits

	return add_mention

def get_status(status):
	return status;


def run(token):
	return bot.run(token)



