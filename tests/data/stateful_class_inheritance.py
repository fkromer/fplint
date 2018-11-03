class StatefulClass(Object):
    def __init__(self, variable):
        self.variable = variable

    def change_state(self, value):
        self.variable = value

    def get_state(self):
        return self.variable


class StatelessClass(StatefulClass):
    """Class intendent to be stateless, but actually isn't
    do to inheritance of statefulness of StatefulClass."""
    
    def stateless_instance_method():
        return 42
