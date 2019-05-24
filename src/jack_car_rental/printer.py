from mdp.printer.per_line_printer import PerLinePrinter
import matplotlib.pyplot as plt


class Printer(PerLinePrinter):
    def print_per_policy_iterate(self):
        self.stats_to_2d()

    def stats_to_2d(self):
        result = self.get_values()
        plt.imshow(result, origin='lower')
        plt.show()

    @classmethod
    def show(cls, my_img, ax=None, **kwargs):
        if ax is None:
            ax = plt.gca()

        def format_coord(x, y):
            x = int(x + 0.5)
            y = int(y + 0.5)
            try:
                return "%s @ [%4i, %4i]" % (my_img[y, x], x, y)
            except IndexError:
                return ""

        ax.imshow(my_img, **kwargs)
        ax.format_coord = format_coord
        plt.draw()

    def get_values(self):
        result = []
        for i in range(len(self.stats)):
            result.append([self.stats[i][j].action_names()[0] for j in range(len(self.stats[i]))])
        return result
