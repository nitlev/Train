class Experiment:
    def __init__(self, agent):
        self.agent = agent

    def run(self, nb_run=1):
        last_result = None
        for i in range(nb_run):
            last_result = self._run_once()
        return last_result

    def _run_once(self):
        while True:
            actions = self.agent.possible_actions()
            if actions.is_empty():
                return 1
            else:
                action = self.agent.choose_best_action(actions)
                self.agent.update_state(action)
