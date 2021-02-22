
from .base_comp import DigitalComponent


class MUX(DigitalComponent):

    def __init__(self, name, init_state=0):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        s0, s1, *comp_inputs = inputs

        if not (s0 or s1):
            self.output = comp_inputs[0]
        elif not s0 and s1:
            self.output = comp_inputs[1]
        elif s0 and not s1:
            self.output = comp_inputs[2]
        else:
            self.output = comp_inputs[3]