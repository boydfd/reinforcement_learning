from jack_car_rental.params import FEE_FOR_MOVING_A_CAR
from mdp.state import State
from mdp.action import Action
from mdp.action_state import ActionState
from .location_factory import location_factory


class CarRental(State):
    def __init__(self, num_f, num_s, factory):
        super().__init__()
        self.first = location_factory.first[num_f]
        self.second = location_factory.second[num_s]
        self.factory = factory
        self.init_action = None

    def init_policy(self):
        self.current_policy = {self.init_action: 1}

    def init_actions(self):
        # 5 4 3 ... 0 ... -4 -5
        max_move = 5 if self.first.count >= 5 else self.first.count
        min_move = -5 if -self.second.count <= -5 else -self.second.count
        available_actions = [
            self.get_action(movement) for movement in range(min_move, max_move + 1)
        ]
        self.init_action = available_actions[-min_move]
        self.config_actions(available_actions)

    def get_action(self, movement):
        reward = self.get_reward(movement)

        next_first_probabilities = self.first.calculate_next_probabilities_with_movement(movement)
        next_second_probabilities = self.second.calculate_next_probabilities_with_movement(-movement)

        next_states = {}
        for i, f in enumerate(next_first_probabilities):
            for j, s in enumerate(next_second_probabilities):
                probability = f * s
                if probability == 0:
                    continue
                next_states[self.factory.get()[i][j]] = probability

        return Action(reward, ActionState(next_states, discount_rate=0.9), name=movement)

    def get_reward(self, movement):
        first_reward = self.first.calculate_rent_expectation_with_movement(movement)
        second_reward = self.second.calculate_rent_expectation_with_movement(-movement)
        reward = first_reward + second_reward - abs(movement) * FEE_FOR_MOVING_A_CAR
        return reward

    def __str__(self):
        return '{}{}:{}->{}'.format(self.first.count, self.second.count, list(self.current_policy.keys()),
                                    self.value)


if __name__ == '__main__':
    pass
    # car_rental_factory[]
