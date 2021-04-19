
from .base_comp import DigitalComponent


class MUX(DigitalComponent):
    """
    A 4x1 MUX component.

    This component routes the data of 1 of 4 inputs depending on the number
    of the pins in s0 and s1:

    - If s0 = s1 = 0, then the first input will be routed.

    - If s0 = 0 and s1 = 1, then the second input will be routed.

    - If s0 = 1 and s1 = 1, then the third input will be routed.

    - If s0 = s1 = 1, then the fourth input will be routed.
    """

    def run(self, inputs):

        s0, s1, *comp_inputs = inputs

        if not (s0 or s1):
            self.output = comp_inputs[0]
        elif not s0 and s1:
            self.output = comp_inputs[1]
        elif s0 and not s1:
            self.output = comp_inputs[2]
        else:
            self.output = comp_inputs[3]

    def verify(self, inputs):

        if len(inputs) != 2:
            raise AttributeError("A MUX component can only have 2 inputs.")
