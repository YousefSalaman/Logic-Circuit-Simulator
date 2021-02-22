
from .base_comp import DigitalComponent


class Clock(DigitalComponent):
    """
    Clock component.
    
    
    It behaves like a digital clock. You set an initial value of 0 or 1 and the
    clock will alternate between these values for every run.
    """

    def __init__(self, name, init_state=0):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        if not inputs:
            self.output = int(not self.output)  # This alternates the output between 0 and 1
        else:
            raise Exception("Clock objects cannot have any inputs.")
