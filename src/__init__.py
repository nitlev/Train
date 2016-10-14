class TestExperiment:
    def test_experiment_should_run_correctly(self):
        experiment = Experiment()
        assert experiment.run()
