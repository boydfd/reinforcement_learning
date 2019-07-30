from lib.envs.blackjack import BlackjackEnv
from mdp.algorithms.double_q_learning import DoubleQLearning
from mdp.algorithms.mc_offline import McOfflinePolicy
from mdp.algorithms.mc_online import McOnline
from mdp.algorithms.n_step_sarsa import NStepSarsa
from mdp.algorithms.q_learning import QLearning
from mdp.algorithms.sarsa import Sarsa
from mdp.result_getter.blackjack_getter import BlackjackGetter
from test_base import TestBase


class BlackjackTest(TestBase):
    def test_blackjack(self):
        expect_usable_a = [
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        ]
        iterator = Sarsa(BlackjackEnv())
        iterator.run(30000000, learning_rate=1)
        print(iterator.env.states.states)

        # blackjack_environment = BlackjackEnvironment()
        # blackjack_environment.monte_carlo_es()
        self.assertEqual(expect_usable_a, BlackjackGetter(iterator.env).get())
