from typing import Tuple

from mdp.action.first_mc_action import FirstMCAction
from mdp.state.gym_state import GymState


class States:
    def __init__(self, epsilon):
        self.states = {}
        self.epsilon = epsilon

    def add_state(self, state, actions):
        if state not in self.states:
            self.states[state] = GymState(state, actions, epsilon=self.epsilon)
        return self.states[state]

    def get(self, state):
        return self.states[state]

    def to_v(self):
        return {state.state: state.to_v() for state in self.states.values()}


class Env:
    def __init__(self, env, discount_factor, epsilon, learning_rate=0.5, action_type=FirstMCAction):
        self.env = env
        self.states = States(epsilon)
        self.discount_factor = discount_factor
        self.action_type = action_type
        self.learning_rate = learning_rate

    def to_v(self):
        return self.states.to_v()

    def reset(self) -> GymState:
        state = self.env.reset()
        self.add_state(state)
        return self.states.get(state)

    def render(self, *args):
        self.env.render(*args)

    def step(self, action) -> Tuple[GymState, float, bool, dict]:
        state, reward, done, info = self.env.step(action)
        state = self.add_state(state)
        return state, reward, done, info

    def add_state(self, state):
        return self.states.add_state(state, [
            self.action_type(self.discount_factor, action, learning_rate=self.learning_rate) for action in
            range(self.env.action_space.n)])
