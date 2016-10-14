from train.agent import Agent


class TestAgent:
    def test_agent_should_return_decision(self):
        # Given
        agent = Agent()

        # When
        actions = ["do nothing"]
        decision = agent.choose(actions)

        # Assert
        assert decision == "do nothing"
