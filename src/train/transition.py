class Transition:
    def __init__(self, previous_state, next_state, reward_function):
        self.previous_state = previous_state
        self.next_state = next_state
        self.rewad_function = reward_function
        self._reward = None

    @property
    def reward(self):
        if self._reward is None:
            self._reward = self.rewad_function(self.previous_state,
                                               self.next_state)
        return self._reward
