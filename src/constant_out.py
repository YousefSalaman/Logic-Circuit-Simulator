from .base_comp import DigitalComponent


class ConstOut(DigitalComponent):
    """
    Constant value component.
    
    This component will run a constant value of either 0 or 1.
    """

    def run(self, inputs):

        pass

    def verify(self, inputs):

        if len(inputs) != 0:
            raise AttributeError("A constant output component cannot have any inputs.")
