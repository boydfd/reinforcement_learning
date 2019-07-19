from unittest import TestCase

from blackjack.blackjack_state import BlackjackState


class UtilityTest(TestCase):
    def test_bigger_than(self):
        self.assertEqual(True, BlackjackState._bigger_than(1, 7, 16))
        self.assertEqual(False, BlackjackState._bigger_than(2, 7, 16))
        self.assertEqual(True, BlackjackState._bigger_than(9, 8, 16))

    def test_get_reward(self):
        self.assertEqual(-1, BlackjackState._get_reward(17, 18))
        self.assertEqual(1, BlackjackState._get_reward(18, 17))
        self.assertEqual(0, BlackjackState._get_reward(17, 17))
