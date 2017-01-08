from train.environment.episode import Episode


class Experiment:
    def __init__(self, agent):
        self.agent = agent
        self.initial_state = self.agent.state

    def run(self, nb_run=1, recorder=None):
        last_result = None
        for i in range(nb_run):
            self.agent = self.agent.set_state(self.initial_state)
            episode = Episode(self.agent, i, recorder)
            last_result = episode.run()
        return last_result
