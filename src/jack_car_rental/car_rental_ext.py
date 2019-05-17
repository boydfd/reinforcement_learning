from jack_car_rental.car_rental import CarRental
from jack_car_rental.params import FEE_FOR_MOVING_A_CAR
from mdp.action import Action
from mdp.action_state import ActionState


class CarRentalExt(CarRental):

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
                next_state = self.factory.get()[i][j]
                reward -= next_state.first.get_extra_fee() * probability
                reward -= next_state.second.get_extra_fee() * probability
                next_states[next_state] = probability

        return Action(reward, ActionState(next_states, discount_rate=0.9), name=movement)

    def get_reward(self, movement):
        first_reward = self.first.calculate_rent_expectation_with_movement(movement)
        second_reward = self.second.calculate_rent_expectation_with_movement(-movement)
        reward = first_reward + second_reward - self.get_moving_cost(movement)
        return reward

    @classmethod
    def get_moving_cost(cls, movement):
        move_from_first_to_second = movement > 0
        if move_from_first_to_second:
            return cls.calc_moving_cost_for(movement - 1)
        return cls.calc_moving_cost_for(movement)

    @staticmethod
    def calc_moving_cost_for(movement):
        return abs(movement) * FEE_FOR_MOVING_A_CAR

    def __str__(self):
        return '{}{}:{}->{}'.format(self.first.count, self.second.count, list(self.current_policy.keys()),
                                    self.value)
