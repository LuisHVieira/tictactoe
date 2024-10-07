from player import Player
from xo.board import Board
from xo import arbiter
from paint import Paint
import matplotlib.text as text

class Game:
    board = Board.fromstring()
    rounds = 0
    end = -1
    fig = Paint.draw_board()
    last_move_player = None

    @classmethod
    def move(cls, row:int, col:int, symbol:str, player:Player):

        if row in range(1, 4) and col in range (1,4):
            if player != None and player != cls.last_move_player:
                for r, c, piece in cls.board:
                    if  r == row and c == col and piece == ' ':
                        cls.board[r, c] = symbol

                        arb = arbiter.outcome(cls.board, symbol)

                        if arb['status'] != 'invalid':
                            cls.last_move_player = player
                            cls.rounds = cls.rounds + 1
                            return dict(player = player, symbol = symbol, valid = True )
                        else:
                            cls.board[r, c] = ' '
            
        return dict(player = player, symbol = symbol, valid = False )

    @classmethod 
    def check_game(cls, player:Player, symbol:str):
        arb = arbiter.outcome(cls.board, symbol)
        print(arb)

        if arb['status'] == 'gameover':
            if arb['reason'] == 'winner':
                cls.end = 1
                return f'Vencedor!!! {player.mention}'
            else:
                cls.end = 1
                return f'#Jogo Empatado#'
        else:
            cls.end = 0
            return f'Joagda de {player.name}'

    @classmethod
    def reset(cls):
        
        cls.board = Board.fromstring()
        Player.set_players(None, None)
       
        for p in Paint.piece:
            p.set_visible(False)

        Paint.piece.clear()
        cls.rounds = 0
        cls.last_move_player = None
        cls.end = -1
        

    @classmethod
    def paint(cls):

        fig = cls.fig

        for r, c, piece in cls.board:

            color = 'purple' if piece == 'x' else 'red'

            if r == 1:
                if c == 1:
                    value = text.Text(0.1, 0.78, piece, size=40, color=color, transform=fig.transFigure, figure=fig)
                elif c == 2:
                    value = text.Text(0.43, 0.78, piece, size=40, color=color, transform=fig.transFigure, figure=fig)
                else:
                    value = text.Text(0.78, 0.78, piece, size=40, color=color, transform=fig.transFigure, figure=fig)

            elif r == 2:
                if c == 1:
                    value = text.Text(0.1, 0.43, piece, size=40, color=color, transform=fig.transFigure, figure=fig)
                elif c == 2:
                    value = text.Text(0.43, 0.43, piece, size=40, color=color, transform=fig.transFigure, figure=fig)
                else:
                    value = text.Text(0.78, 0.43, piece, size=40, color=color, transform=fig.transFigure, figure=fig)

            elif r == 3:
                if c == 1:
                    value = text.Text(0.1, 0.1, piece, size=40, color=color, transform=fig.transFigure, figure=fig)
                elif c == 2:
                    value = text.Text(0.43, 0.1, piece, size=40, color=color, transform=fig.transFigure, figure=fig)
                else:
                    value = text.Text(0.78, 0.1, piece, size=40, color=color, transform=fig.transFigure, figure=fig)

            Paint.piece.append(value)

            fig.lines.extend([p for p in Paint.piece ])
            fig.savefig('env/img/c_board.png')
            
                
                
                





