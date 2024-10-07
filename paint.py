import matplotlib.lines as lines
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

class Paint:
    piece = []

    @classmethod
    def draw_board(cls):
        fig = plt.figure(figsize=(3, 3), dpi=80)

        l1 = lines.Line2D([0.33, 0.33], [0, 1], color='#5165f6', transform=fig.transFigure, figure=fig)
        l2 = lines.Line2D([0.66, 0.66], [0, 1], color='#5165f6', transform=fig.transFigure, figure=fig)
        l3 = lines.Line2D([1, 0], [0.33, 0.33], color='#5165f6', transform=fig.transFigure, figure=fig)
        l4 = lines.Line2D([1, 0], [0.66, 0.66], color='#5165f6', transform=fig.transFigure, figure=fig)

        fig.lines.extend([l1, l2, l3, l4])

        return fig