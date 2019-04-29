from mdp.action import Action
from mdp.action_state import ActionState

noop_action_state = ActionState({})
noop_action = Action(0, noop_action_state)


def create_normal_action(next_state, name):
    next_state = ActionState({next_state: 1})
    return Action(-1, next_state, name)
