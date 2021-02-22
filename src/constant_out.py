from .base_comp import DigitalComponent


class ConstOut(DigitalComponent):  # Constant output class

    def __init__(self, name, init_state):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        if inputs:
            raise AttributeError("Constant output objects cannot have any inputs.")
