
from collections import deque

from .base_comp import DigitalComponent


class UniversalReg(DigitalComponent):
    """
    Universal Shift Register (USR) component.

    This component behaves like a USR. It has the has the following pins:

    - s0 and s1: These two pins determine the mode of operation. Here are the
      possible combinations:

      - s0 = 0 and s1 = 0: Idle state (USR won't do anything)

      - s0 = 0 and s1 = 1: Right shift elements

      - s0 = 1 and s1 = 0: Left shift elements

      - s0 = 1 and s1 = 1: Parallel shift elements

    - clk: This pin must be 1 for the register to output a value.
    """

    _REG_SIZE = 4  # Size of register

    def __init__(self, name, load_input=None, init_state=0):

        super().__init__(name, init_state)
        if load_input is None:
            self.reg_bits = deque([None] * self._REG_SIZE)
        else:
            if len(load_input) != 4:
                raise ValueError("The length of the 'load_input' has to be 4")
            self.reg_bits = deque(load_input)

    def print(self):

        run_str = super().print().replace("\n\n", "")
        return run_str + f'; Current registry: {list(self.reg_bits)}\n\n'

    def verify(self, inputs):

        super().verify(inputs)

    # Running USR methods

    def run(self, inputs):

        s0, s1, clk, *reg_inputs = inputs
        if len(reg_inputs) == 0:
            reg_inputs = [None] * self._REG_SIZE

        if clk == 1:  # If clk is one, then the register will output values
            if not s0 and s1:
                self.output = self.reg_bits.popleft()
                self.reg_bits.append(reg_inputs[0])
            if s0 and not s1:
                self.output = self.reg_bits.pop()
                self.reg_bits.appendleft(reg_inputs[0])
            elif s0 == s1:  # Parallel load
                self.output = self.reg_bits
                self[:] = reg_inputs
