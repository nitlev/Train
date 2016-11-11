from train.state import State


class TestState:
    def test_state_should_cast_to_list(self):
        # Given
        state1 = State([1, 2, 3])
        state2 = State([])

        # Assert
        assert state1.to_list() == [1, 2, 3]
        assert state2.to_list() == []

    def test_state_method_update_should_return_new_state(self):
        # Given
        update = lambda x, n: (e + n for e in x)
        state = State([0, 1], update_function=update)

        # When
        new_state = state.update(1)

        # Assert
        assert new_state is not state
        assert new_state.to_list() == [1, 2]

    def test_states_are_iterable(self):
        # Given
        state1 = State([1, 2, 3])
        state2 = State([0, 1])
        my_list = []

        # When
        a, b, c = state1
        for element in state2:
            my_list.append(element)

        # Assert
        assert a == 1
        assert b == 2
        assert c == 3
        assert my_list == [0, 1]

    def test_update_state_return_new_state(self):
        # Given
        state = State([])

        # When
        new_state = state.update_function(None)

        # Assert
        assert isinstance(new_state, State)
        assert new_state is not state
