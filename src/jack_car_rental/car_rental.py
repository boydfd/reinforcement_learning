from mdp.state import State
from mdp.action import Action
from mdp.action_state import ActionState
from .location_factory import location_factory
from . import car_rental_factory


class CarRental(State):
    def __init__(self, num_f, num_s):
        super().__init__()
        self.first = location_factory.first[num_f]
        self.second = location_factory.second[num_s]

    def recalculate_actions(self):
        # 5 4 3 ... 0 ... -4 -5
        max_move = 5 if self.first.count >= 5 else self.first.count
        min_move = -5 if -self.second.count <= -5 else -self.second.count
        self.available_actions = {
            self.get_action(movement): 1 for movement in range(min_move, max_move + 1)
        }
        self.balance_actions()
        self.current_policy = {self.get_action(0): 1}

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
                next_states[car_rental_factory.car_rental_factory.car_rentals[i][j]] = probability

        return Action(reward, ActionState(next_states), name=movement, discount_rate=0.9)

    def get_reward(self, movement):
        fee_for_moving_a_car = 2
        first_reward = self.first.calculate_expectation_with_movement(movement)
        second_reward = self.second.calculate_expectation_with_movement(-movement)
        reward = first_reward + second_reward - abs(movement) * fee_for_moving_a_car
        return reward

    def __str__(self):
        return '{}{}:{}->{}'.format(self.first.count, self.second.count, list(self.current_policy.keys()),
                                    self.value)


if __name__ == '__main__':
    pass
    # car_rental_factory[]
