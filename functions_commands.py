from xo.game import Game
from config import Config as c

prefix = "$"
bot = c.createBot(prefix)


players = []
rounds = []

@bot.command(name='play', help='Para jogar faça menção aos dois jogadores.', brief='Inicia o jogo')
async def play(ctx, *args):

	global status
	global game
	status = 0
	game = Game()

	if len(args) == 2:

		for arg in args:
			players.append(arg)

		if players[0] != players[1]:			

			response_players = "Player X: " + players[0] + " Player O: " +  players[1]
			await ctx.channel.send(response_players)
			status = get_status(1)
			game = Game()
			game.start('x')

		else:
			await ctx.channel.send('Invalid Players')

	else:
		await ctx.channel.send("Invalid Command") 


@bot.listen('on_message')
async def gameplay(message):

	msg_mention = mention(message.author.mention)
	msg_content = message.content

	if msg_content == "Player X: " + players[0] + " Player O: " +  players[1]:
		await message.channel.send(players[0] + ' faça sua jogada: ')

	if status == 1:
		if len(rounds) % 2 == 0:	
			if msg_mention == players[0]:
				datas = validate_played(msg_content)
				move = game.moveto(datas[0], datas[1])
				await message.channel.send(game.board.toascii())
				if move['name'] == 'next-turn':
					await message.channel.send(players[1] + ' faça sua jogada: ')
					rounds.append('x')

				elif move['name'] == 'invalid-move':
					await message.channel.send(players[0] + ' jogue novamente: ')

				elif move['name'] == 'gameover':
					if move['reason'] == 'winner':
						await message.channel.send(players[0] + ' você venceu!')

					else:
						await message.channel.send('Deu Velha!')

					#clear array rounds, because start next play with other play of the called
					del rounds[:]
					
			elif msg_mention == players[1]:
				await message.channel.send("Não é a sua vez")


		else:
			if msg_mention == players[1]:
				datas = validate_played(message.content)
				move = game.moveto(datas[0], datas[1])
				await message.channel.send(game.board.toascii())
				if move['name'] == 'next-turn':
					rounds.append('o')
					await message.channel.send(players[0] + ' faça sua jogada: ')

				elif move['name'] == 'invalid-move':
					await message.channel.send(players[1] + ' jogue novamente: ')

				elif move['name'] == 'gameover':
					if move['reason'] == 'winner':
						await message.channel.send(players[1] + ' você venceu!')

					else:
						await message.channel.send('Deu Velha!')

					#clear array rounds, because start next play with other play of the called
					del rounds[:]

			elif msg_mention == players[0]:
				await message.channel.send("Não é a sua vez")


def mention(msg_mention):
	split_msg_metion = msg_mention.split('@')
	add_mention = ''
	for pos, splits in zip(range(len(split_msg_metion)), split_msg_metion):
		if pos == 1:
			add_mention += '@!'

		add_mention += splits

	return add_mention

def get_status(status):
	return status

def validate_played(message):

	pos_played = []

	for pos_play in list(message):
		try:
			if pos_play == '0':
				pos_play = 4
			else:
				pos_play = int(pos_play)
		except Exception as e:
			pos_play = -1

		if pos_play > 0:
			pos_played.append(pos_play)
			if len(pos_played) == 2:
				break

	return pos_played


def run(token):
	return bot.run(token)



