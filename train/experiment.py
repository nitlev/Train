class Experiment:
    def __init__(self, agent):
        self.agent = agent
        self.initial_state = self.agent.state

    def run(self, nb_run=1, verbose=0):
        last_result = None
        for i in range(nb_run):
            last_result = self._run_once(verbose)
        return last_result

    def _run_once(self, verbose=0):
        self.agent = self.agent.set_state(self.initial_state)
        while True:
            if verbose:
                print(self.agent.state)
            actions = self.agent.possible_actions()
            if actions.is_empty():
                print("End of episode.")
                return 1
            else:
                action = self.agent.choose_best_action(actions)
                self.agent.update_state(action)
