from collections import defaultdict

import numpy as np

from lib import plotting
from lib.envs.blackjack import BlackjackEnv
from mdp.algorithms.double_q_learning import DoubleQLearning
from mdp.algorithms.mc_offline import McOfflinePolicy
from mdp.algorithms.mc_online import McOnline
from mdp.algorithms.q_learning import QLearning

if __name__ == '__main__':
    iterator = QLearning(BlackjackEnv())
    iterator.run(500000)
    print(iterator.env.states.states)
    Q = iterator.env.to_v()
    V = defaultdict(float)
    for state, actions in Q.items():
        action_value = np.max(actions)
        V[state] = action_value
    plotting.plot_value_function(V, title="Optimal Value Function")
