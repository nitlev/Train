from train.transition import Transition


class TestTransitions:
    def test_transitions_should_compute_reward(self):
        # Given
        transition1 = Transition(0, 1, lambda x, y: 2)
        transition2 = Transition(0, 1, lambda x, y: -1)

        # Check
        assert transition1.reward == 2
        assert transition2.reward == -1
