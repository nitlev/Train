from train.environment.experiment import Experiment
from train.environment.recorder import Recorder

from train.learning.state import State
from train.learning.agent import Agent
from train.learning.action import Actions
from train.learning.q_function import RandomQFunction


def update_state(state, action):
    position, speed = state
    new_speed = max(speed - action, 0)
    new_position = position + speed
    return State((new_position, new_speed))


def state_to_actions(state):
    _, speed = state
    if speed > 0:
        return Actions(*[0.1 * i for i in range(11)])
    else:
        return Actions()


class TestFullRunExperiment:
    def test_run_full_train_experiment(self):
        # Given
        state = State([0, 20]).update_function(update_state)
        agent = Agent(state, RandomQFunction(), state_to_actions)
        experiment = Experiment(agent)

        # When
        experiment.run()

        # Assert
        assert experiment.agent.state[1] == 0

    def test_run_full_train_experiment_with_record(self):
        # Given
        state = State([0, 20]).update_function(update_state)
        agent = Agent(state, RandomQFunction(), state_to_actions)
        recorder = Recorder()
        experiment = Experiment(agent)

        # When
        experiment.run(recorder=recorder)

        # Assert
        assert len(list(recorder.all_transitions)) > 0

