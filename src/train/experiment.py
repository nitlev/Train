class Experiment:
    def __init__(self, agent):
        self.agent = agent

    def run(self, nb_run=1):
        for i in range(nb_run):
            last_result = self.run_once()
        return last_result

    def run_once(self):
        return 1
