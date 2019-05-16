from mdp.builder import Builder
import matplotlib.pyplot as plt


class CarRentalBuilder(Builder):
    def __init__(self, stats, iterator=None, max_count=21):
        super().__init__(iterator)
        self.max_count = max_count
        self.row_length = self.max_count
        self.column_length = self.max_count
        self.stats = stats
        self._foreach(lambda state: state.recalculate_actions())

    def _foreach(self, func):
        for i in range(self.row_length):
            for j in range(self.column_length):
                func(self.stats[i][j])

    def _foreach_return(self, func):
        for i in range(self.row_length):
            for j in range(self.column_length):
                result = func(self.stats[i][j])
                yield result

    def print(self):
        for i in range(len(self.stats)):
            print(*self.stats[i])

    def stats_to_2d(self):
        result = self.get_values()
        plt.imshow(result, origin='lower')
        plt.show()

    def print_policy(self):
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
