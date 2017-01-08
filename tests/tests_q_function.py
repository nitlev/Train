from train.learning.state import State

from train.learning.action import Actions
from train.learning.q_function import ZeroQFunction, RandomQFunction


class Test:
    def test_zero_q_function_should_return_vector(self):
        # Given
        q_function = ZeroQFunction()
        state = State([])
        two_actions = Actions("Do Nothing", "Do Something")
        three_actions = Actions("Do Nothing", "Do Something",
                                "Do Something else")

        # When
        two_q_values = q_function.evaluate(state, two_actions)
        three_q_values = q_function.evaluate(state, three_actions)

        # Check
        assert len(two_q_values) == 2
        assert len(three_q_values) == 3

    def test_random_q_function_should_return_vector(self):
        # Given
        q_function = RandomQFunction()
        state = State([])
        two_actions = Actions("Do Nothing", "Do Something")
        three_actions = Actions("Do Nothing", "Do Something",
                                "Do Something else")

        # When
        two_q_values = q_function.evaluate(state, two_actions)
        three_q_values = q_function.evaluate(state, three_actions)

        # Check
        assert len(two_q_values) == 2
        assert len(three_q_values) == 3
