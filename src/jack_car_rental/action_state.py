from mdp.action_state import ActionState as AS


class ActionState(AS):
    # pass
    def evaluate(self):
        return sum([self.calc_for_one_state(possibility, state) for state, possibility in self.next_states.items()])

    def calc_for_one_state(self, possibility, state):
        return (self.discount_rate * state.value - state.first.get_extra_fee() - state.second.get_extra_fee()) * possibility
