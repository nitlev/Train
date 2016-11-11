from train.episode import Episode


class Experiment:
    def __init__(self, agent):
        self.agent = agent
        self.initial_state = self.agent.state

    def run(self, nb_run=1, verbose=0):
        last_result = None
        for i in range(nb_run):
            last_result = self.run_one_episode(verbose)
        return last_result

    def run_one_episode(self, verbose=0):
        self.agent = self.agent.set_state(self.initial_state)
        episode = Episode(self.agent, verbose)
        result = episode.run()
        return result
