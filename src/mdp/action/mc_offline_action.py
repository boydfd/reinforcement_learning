class McOfflineAction:
    def __init__(self, discount_factor, name=None):
        self.name = name
        self.c = 0
        self.q = 0

    def update_c(self, w):
        self.c = self.c + w

    def update_q(self, g, w):
        self.q = self.q + w / self.c * (g - self.q)

