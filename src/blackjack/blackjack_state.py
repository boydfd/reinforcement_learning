from blackjack.action import HitAction, StickAction
from blackjack.score_calculator import ScoreCalculator
from blackjack.utility import log
from mdp.state.mc_state import MCState
import random
import math


class BlackjackState(MCState):
    def __init__(self, player_sum, dealer_show, have_usable_a, name=None):
        super().__init__(name=name)
        self.player_sum = player_sum
        self.dealer_show = dealer_show
        self.have_usable_a = have_usable_a
        self.available_actions = [HitAction(self.epsilon), StickAction(self.epsilon)]
        self.choose_next_action()

    def choose_next_action(self):
        randint = random.randint(1, 2)
        self.next_policy = self.available_actions[0] if randint == 1 else self.available_actions[1]

    def get_reward(self) -> int:
        dealer_sum = self.get_dealer_score()
        log.debug('dealer:{} --- player:{}'.format(dealer_sum, self.player_sum))
        return self._get_reward(self.player_sum, dealer_sum)

    @staticmethod
    def _get_reward(left, right):
        difference = left - right
        return int(math.floor(abs(difference) / (difference - 1e-15)))

    def get_dealer_score(self):
        another_card = self.hit()
        dealer_cards = [another_card, self.dealer_show]

        while True:
            dealer_sum = ScoreCalculator(dealer_cards).calculate()
            if dealer_sum > 21:
                return -1
            if dealer_sum >= 17:
                return dealer_sum
            dealer_cards.append(self.hit())

    @staticmethod
    def hit():
        card = random.randint(1, 14)
        return min(card, 10)

    def choose_next_policy(self):
        self.next_policy = self._choose_next_action()
        log.debug('choose:{}'.format(self.next_policy))

    @staticmethod
    def _bigger_than(c1, c2, number):
        extra = 10 if c1 == 1 or c2 == 1 else 0
        return c1 + c2 + extra > number

    def get_cards(self):
        if self.have_usable_a:
            return [self.player_sum - 10, 1, ]
        else:
            return [self.player_sum]

    def get_result(self):
        return self._choose_next_action().get_result()


class BustBlackjackState(MCState):
    def __init__(self, ):
        super().__init__(name='bust')

    def get_next_action(self):
        return StickAction(self.epsilon)

    def get_reward(self):
        return -1

    def update_reward(self, episode_reward):
        pass

    def choose_next_policy(self):
        pass
