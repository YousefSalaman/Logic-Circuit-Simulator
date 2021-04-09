
from .base_comp import DigitalComponent


class Clock(DigitalComponent):
    """
    Clock component.
    
    
    It behaves like a digital clock. You set an initial value of 0 or 1 and the
    clock will alternate between these values for every run.
    """

    def run(self, inputs):

        if not inputs:
            self.output = int(not self.output)  # This alternates the run between 0 and 1
        else:
            raise Exception("Clock objects cannot have any inputs.")
