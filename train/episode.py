class Episode(object):
    def __init__(self, agent, episode_id, verbosity=0):
        self.agent = agent
        self.episode_id = episode_id
        self.verbosity = verbosity

    def run(self):
        actions = self.agent.possible_actions()

        while not actions.is_empty():
            if self.verbosity:
                print(self.agent.state)
            actions = self.agent.possible_actions()
            best_action = self.agent.choose_best_action(actions)
            self.agent.update_state(best_action)

        print("End of episode.")
        return 1
