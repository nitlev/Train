from train.episode import Episode
from train.recorder import Recorder


class Experiment:
    def __init__(self, agent):
        self.agent = agent
        self.recorder = Recorder()
        self.initial_state = self.agent.state

    def run(self, nb_run=1, verbose=0):
        last_result = None
        for i in range(nb_run):
            self.agent = self.agent.set_state(self.initial_state)
            episode = Episode(self.agent, i, verbose)
            last_result = episode.run()
        return last_result
