class Iterator:
    def __init__(self, environment, stats, actions):
        self.actions = actions
        self.stats = stats
        self.environment = environment

    def iterate(self):
        stats = set()
        if self.environment.not_end():
            stats.add(self.environment.next_stat())
        else:
            self.environment.get_reward()

