from mdp.action.first_mc_action import FirstMCAction
from mdp.state.gym_state import GymState


class States:
    def __init__(self, epsilon):
        self.states = {}
        self.epsilon = epsilon

    def add_state(self, state, actions):
        if state not in self.states:
            self.states[state] = GymState(state, actions, epsilon=self.epsilon)

    def get(self, state):
        return self.states[state]

    def to_v(self):
        return {state.state: state.to_v() for state in self.states.values()}


class Env:
    def __init__(self, env, discount_factor, epsilon):
        self.env = env
        self.states = States(epsilon)
        self.discount_factor = discount_factor

    def to_v(self):
        return self.states.to_v()

    def reset(self):
        state = self.env.reset()
        self.add_state(state)
        return self.states.get(state)

    def step(self, action):
        state, reward, done, info = self.env.step(action)
        if not done:
            self.add_state(state)
            return self.states.get(state), reward, done, info
        return state, reward, done, info

    def add_state(self, state):
        self.states.add_state(state, [FirstMCAction(self.discount_factor, name=action) for action in
                                      range(self.env.action_space.n)])
