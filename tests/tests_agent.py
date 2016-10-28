from mock import MagicMock
from train.action import Actions
from train.agent import Agent

from src.train.state import State


class TestAgent:
    def test_agent_should_return_decision(self):
        # Given
        agent = Agent()

        # When
        actions = Actions("do nothing")
        decision = agent.choose_best_action(actions)

        # Assert
        assert decision == "do nothing"

    def test_update_should_call_update_function(self):
        # Given
        mock_function = MagicMock()
        state = State([], update_function=mock_function)
        agent = Agent(state=state)

        # When
        action = "Do nothing"
        agent.update_state(action=action)

        # Assert
        mock_function.assert_called_once_with([], "Do nothing")
