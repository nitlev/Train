import numpy as np

from train.learning.transition import Transition


class Recorder(object):
    def __init__(self):
        self.episodes = {}
        self.current_episode = None

    def record(self, episode):
        self.current_episode = episode
        self.episodes.setdefault(self.current_episode.episode_id,
                                 {"states": [],
                                  "transitions": []})

    def record_state(self, state):
        episode = self.episodes[self.current_episode.episode_id]
        episode_states = episode["states"]
        episode_states.append(state)
        if len(episode_states) > 1:
            transition = Transition(episode_states[-1], state, None, None)
            episode["transitions"].append(transition)

    @property
    def all_transitions(self):
        return (transition for episode in self.episodes.values()
                for transition in episode["transitions"])

    @property
    def all_states(self):
        return (transition for episode in self.episodes.values()
                for transition in episode["states"])

    def some_transitions(self, size):
        return np.random.choice(list(self.all_transitions), size=size)


class EmptyRecorder(Recorder):
    def __init__(self):
        super(EmptyRecorder, self).__init__()

    def record(self, episode):
        self.current_episode = episode

    def record_state(self, state):
        pass
