from collections import defaultdict

import numpy as np

from lib import plotting
from mdp.algorithms.mc_offline import McOfflinePolicy

if __name__ == '__main__':
    iterator = McOfflinePolicy()
    iterator.run(500000)
    Q = iterator.env.to_v()
    print(Q)
    V = defaultdict(float)
    for state, actions in Q.items():
        action_value = np.max(actions)
        V[state] = action_value
    plotting.plot_value_function(V, title="Optimal Value Function")
