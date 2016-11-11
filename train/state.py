def identity(state, action):
    return state


class State:
    def __init__(self, state_values, update_function=None):
        self.state_values = state_values
        self._update_function = update_function \
            if update_function is not None \
            else identity

    def update_function(self, function):
        return State(self.state_values, update_function=function)

    def to_list(self):
        return list(self.state_values)

    def update(self, action):
        new_state = State(self._update_function(self.to_list(), action),
                          update_function=self._update_function)
        return new_state

    def __getitem__(self, item):
        return self.state_values[item]

    def __repr__(self):
        strings = [str(value) for value in self.state_values]
        return "State({})".format(", ".join(strings))
