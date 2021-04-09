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

    - reg_enable and ctrl_enable: These two pins need to be enabled for the
      register to operate.

    - clear: If this pin is enabled, then the register will get cleared. That
      is, the register will be now full of 0's.
    """

    def __init__(self, name, size=None, load_input=None, init_state=0):

        super().__init__(name, init_state)
        self.prev_state = (0, 0)
        if load_input:
            self.reg_bits = _RegisterBits(load_input)
        elif size:
            self.reg_bits = _RegisterBits([None] * size)
        else:
            raise ValueError('Either "size" or "load_input" have to be specified to create a Register object.')

    def run(self, inputs):

        s0, s1, reg_enable, crtl_enable, clear, *reg_inputs = inputs

        if clear:  # If the clear input is enabled, then the register resets its internal storage
            self.reg_bits.clear()
        if reg_enable == crtl_enable == 1:  # If the reg_inputs below are active, then the register will change
            self._register_outputs(s0, s1, reg_inputs)
            curr_state = (s0, s1)
            if curr_state != (0, 0):
                self.prev_state = curr_state

    def print(self):

        run_str = super().print().replace("\n\n", "")
        if self.prev_state == (1, 0):
            self.reg_bits.reverse()
            run_str += f'; Current registry: {self.reg_bits}'
            self.reg_bits.reverse()
        else:
            run_str += f'; Current registry: {self.reg_bits}'
        return run_str + '\n\n'

    def _register_outputs(self, s0, s1, reg_inputs):
        """
        In here, you will find the possible outputs of the register.
        """

        self._reverse_register_bits((s0, s1))

        if s0 != s1:
            self.output = self.reg_bits.shift_serial(reg_inputs)
        elif s0 and s1:
            self.output = self.reg_bits.shift_parallel(reg_inputs)

    def _reverse_register_bits(self, curr_state):
        """
        This reverses the register bits before applying the appropriate
        translation with RegisterBits methods.
        """

        if self.prev_state != curr_state and (curr_state == (1, 0) or self.prev_state == (1, 0)):
            self.reg_bits.reverse()


class _RegisterBits(list):
    """
    Helper class for register.

    This extends some of the functionalities of the list class, so it behaves
    like internal registry of a shift register
    """

    def __init__(self, register_list):

        self.reg_size = len(register_list)
        super().__init__(register_list)

    def shift_serial(self, list_input):

        if not list_input:
            list_input = [None]
        last_item = self.pop(self.reg_size - 1)
        self.insert(0, list_input[0])
        return last_item

    def shift_parallel(self, new_list):

        if len(new_list) == 0:
            new_list = self.reg_size * [None]  # Default parameter

        if len(new_list) == self.reg_size:
            prev_reg_bits = self
            self[:] = new_list
            return prev_reg_bits

        raise Exception('The input list has to be the same size as the list within the object.')

    def clear(self):

        self[:] = [0] * self.reg_size
