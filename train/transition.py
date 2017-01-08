class Transition:
    def __init__(self, previous_state, next_state, action, reward_function):
        self.previous_state = previous_state
        self.next_state = next_state
        self.action = action
        self.reward_function = reward_function
        self._reward = None

    @property
    def reward(self):
        if self._reward is None:
            self._reward = self.reward_function(self.previous_state,
                                                self.next_state)
        return self._reward

    def state_and_action_to_list(self):
        return self.previous_state.to_list() + [self.action]
