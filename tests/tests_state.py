from train.state import State


class TestState:
    def test_state_should_cast_to_list(self):
        # Given
        state1 = State(1, 2, 3)
        state2 = State()

        # Assert
        assert state1.to_list() == [1, 2, 3]
        assert state2.to_list() == []
