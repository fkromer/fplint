class StatefulClass(Object):
    """Class is stateful due to instance attribute."""
    def __init__(self, value):
        self.instance_attribute = value

    def change_state(self, value):
        self.instance_attribute = value

    def get_state(self):
        return self.instance_attribute


class StatelessClass(StatefulClass):
    """Class intendent to be stateless, but actually isn't
    do to inheritance of statefulness of StatefulClass."""
    
    def stateless_instance_method():
        return 42
