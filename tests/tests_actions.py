from train.action import Actions


class TestActions:
    def test_empty_action_set_should_be_empty(self):
        # Given
        actions = Actions()

        # Check
        assert actions.is_empty()

    def test_non_empty_action_set_shouldnt_be_empty(self):
        # Given
        actions = Actions("Hello")

        # Check
        assert not actions.is_empty()

    def test_Actions_should_supports_indexing(self):
        # Given
        actions = Actions("Hello", "World")

        # Check
        assert actions[0] == "Hello"
        assert actions[1] == "World"
