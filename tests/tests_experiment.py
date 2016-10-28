from train.agent import Agent
from train.experiment import Experiment


class TestExperiment:
    def test_experiment_run_should_return_one_when_running_once(self):
        # Given
        agent = Agent()
        experiment = Experiment(agent)

        # When
        result = experiment.run()

        assert result == 1

    def test_experiment_run_should_return_1_when_running_multiple_times(self):
        # Given
        agent = Agent()
        experiment = Experiment(agent)

        # When
        result = experiment.run(10)

        assert result == 1
