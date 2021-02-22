from .base_comp import DigitalComponent


class ConstOut(DigitalComponent):
    """
    Constant value component.
    
    This component will output a constant value of either 0 or 1.
    """

    def __init__(self, name, init_state):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        if inputs:
            raise AttributeError("Constant output objects cannot have any inputs.")
