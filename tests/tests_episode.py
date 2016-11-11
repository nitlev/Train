from mock import MagicMock
from train.action import Actions

from train.agent import Agent
from train.episode import Episode


class ActionMock(Actions):
    def __init__(self):
        self.counter = 0

    def is_empty(self):
        if self.counter == 0:
            self.counter += 1
            return False
        else:
            return True


class TestEpisode:
    def test_episode_should_update_agent_state(self):
        # Given
        actions = ActionMock()
        agent = MagicMock(Agent)
        agent.possible_actions.return_value = actions
        episode = Episode(agent, 0)

        # When
        episode.run()

        # Assert
        agent.update_state.assert_called_once()

