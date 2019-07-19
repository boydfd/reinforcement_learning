import itertools
import random

from tqdm import tqdm

from blackjack.blackjack_state import BlackjackState, BustBlackjackState
from blackjack.score_calculator import ScoreCalculator
from blackjack.utility import log

BUST = 'b'
USABLE_A = 'a'
NO_USABLE_A = 'na'


class BlackjackEnvironment:
    def __init__(self, ):
        self.stats = {
            USABLE_A: list(self.create_state_list(True)),
            NO_USABLE_A: list(self.create_state_list(False)),
            BUST: BustBlackjackState()
        }
        self.current_stat = None
        self.state_gone_through = None
        self.start_state_new_episode()

    @staticmethod
    def create_state_list(have_usable_a):
        for i in range(1, 11):
            yield [BlackjackState(j, i, have_usable_a, name='dealer: {} --- player: {} ---- usable_a: {}'.format(i, j, have_usable_a)) for j in
                   range(11, 22)]

    def monte_carlo_es(self):
        for _ in tqdm(range(500000)):
            reward = self.execute_one_episode()
            self.settle_reward(reward)
            self.start_state_new_episode()

    def execute_one_episode(self):
        log.debug('start')
        while True:
            log.debug(self.current_stat)
            is_end, reward = self.play()
            log.debug('reward={}'.format(reward))
            if is_end:
                log.debug('end')
                return reward
                # self.update_reward(reward)
                # break

    def play(self):
        action = self.current_stat.get_next_action()
        if action.is_stick():
            return True, self.current_stat.get_reward()
        else:
            self.update_next_state()
            return False, 0

    def update_next_state(self):
        self.current_stat = self._get_next_state(self.current_stat)
        self.go_through_state(self.current_stat)

    def go_through_state(self, state):
        self.state_gone_through.append(state)

    def _get_next_state(self, stat: BlackjackState):
        player_cards = stat.get_cards()
        player_cards.append(stat.hit())
        calculator = ScoreCalculator(player_cards)
        player_sum = calculator.calculate()
        return self._get_state(calculator.have_usable_a(), stat.dealer_show, player_sum)

    def _get_state(self, have_usable_a, dealer_show, player_sum):
        if player_sum > 21:
            return self.stats[BUST]
        if have_usable_a:
            return self.stats[USABLE_A][dealer_show - 1][player_sum - 11]
        return self.stats[NO_USABLE_A][dealer_show - 1][player_sum - 11]

    def update_reward(self, reward):
        log.debug('start update')
        for state in self.state_gone_through:
            state.update_reward(reward)
            log.debug(state)
        log.debug('end update')

    def start_state_new_episode(self):
        self.current_stat = self.new_random_state()
        self.state_gone_through = [self.current_stat]

    def new_random_state(self):
        stats = list(itertools.chain.from_iterable(self.stats[USABLE_A] + self.stats[NO_USABLE_A]))
        state = stats[random.randint(0, len(stats) - 1)]
        state.choose_random_policy()
        return state

    def settle_reward(self, reward):
        self.update_reward(reward)
        for state in self.state_gone_through:
            state.choose_next_policy()

    def print(self):
        self._print(self.stats[USABLE_A])
        self._print(self.stats[NO_USABLE_A])

    def _print(self, states):
        stats = list(itertools.chain.from_iterable(states))
        for state in stats:
            log.log(state)

    def get_result(self, flag):
        for dealer_show in self.stats[flag]:
            yield [player_sum.get_result() for player_sum in dealer_show]


