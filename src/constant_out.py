from .base_comp import DigitalComponent


class ConstOut(DigitalComponent):
    """
    Constant value component.
    
    This component will run a constant value of either 0 or 1.
    """

    def run(self, inputs):

        if inputs:
            raise AttributeError("Constant run objects cannot have any inputs.")
