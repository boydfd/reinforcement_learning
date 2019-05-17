from jack_car_rental.params import MAX_CARS
from mdp.builder import Builder
import matplotlib.pyplot as plt

from mdp.foreacher.foreacher_2d import Foreacher2D


class CarRentalBuilder(Builder):
    def __init__(self, stats, policy_iterator=None, max_count=MAX_CARS + 1):
        self.row_length = max_count
        self.column_length = max_count
        super().__init__(Foreacher2D(stats, self.row_length, self.column_length), policy_iterator)
        self.stats = stats

    def final_print(self):
        for i in range(len(self.stats)):
            print(*self.stats[i])

    def stats_to_2d(self):
        result = self.get_values()
        plt.imshow(result, origin='lower')
        plt.show()

    def print_per_policy_iterate(self):
        self.stats_to_2d()

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
        for i in range(self.row_length):
            result.append([self.stats[i][j].action_names()[0] for j in range(self.column_length)])
        return result
