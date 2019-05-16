from gambler.capital import Capital, FinalCapital
from mdp.action_state import ActionState
from mdp.action import Action


def action_state(result, capital, i):
    tail = result[capital.count - i]
    head = result[capital.count + i]
    return ActionState({
        tail: 0.6,
        head: 0.4,
    })


def recalculate_actions():
    result = [Capital(i) for i in range(100)] + [FinalCapital()]
    for capital in result:
        capital.available_actions = {
            Action(0, action_state(result, capital, i), name=i): 1 for i in
            range(min(capital.count, 100 - capital.count) + 1)
        }
        capital.balance_actions()
        capital.init_policy()
    return result


capitals = recalculate_actions()
