
from .base_comp import DigitalComponent


class Clock(DigitalComponent):

    def __init__(self, name, init_state=0):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        if not inputs:
            self.output = int(not self.output)  # This alternates the output between 0 and 1
        else:
            raise Exception("Clock objects cannot have any inputs.")
