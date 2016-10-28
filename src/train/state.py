def identity(state, action):
    return state

class State:
    def __init__(self, state_values, update_function=None):
        self.state_values = state_values
        self.update_function = update_function if update_function is not None \
            else identity

    def update_function(self, function):
        return State(self.state_values, update_function=function)

    def to_list(self):
        return list(self.state_values)

    def update(self, action):
        new_state = State(self.update_function(self.to_list(), action),
                          update_function=self.update_function)
        return new_state
