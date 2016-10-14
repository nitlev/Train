from src.experiment import Experiment


class TestExperiment:
    def test_experiment_method_run_should_return_one(self):
        # Given
        experiment = Experiment()

        # When
        result = experiment.run()

        assert result == 1
