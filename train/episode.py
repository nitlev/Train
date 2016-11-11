from train.recorder import EmptyRecorder


class Episode(object):
    def __init__(self, agent, episode_id, recorder=None):
        self.agent = agent
        self.episode_id = episode_id
        self.recorder = recorder or EmptyRecorder()

    def run(self):
        self.recorder.record(self)
        self.recorder.record_state(self.agent.state)

        actions = self.agent.possible_actions()
        while not actions.is_empty():
            best_action = self.agent.choose_best_action(actions)
            self.agent.update_state(best_action)
            self.recorder.record_state(self.agent.state)
            actions = self.agent.possible_actions()

        return 1
