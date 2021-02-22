from .base_comp import DigitalComponent


class UniversalReg(DigitalComponent):

    def __init__(self, name, size, load_input=None, init_state=0):

        super().__init__(name, init_state)
        self.prev_state = (0, 0)
        if load_input:
            self.reg_bits = _RegisterBits(load_input)
        else:
            self.reg_bits = _RegisterBits([None] * size)

    def component_output(self, inputs):

        s0, s1, reg_enable, crtl_enable, clear, *reg_inputs = inputs

        if clear:  # If the clear input is enabled, then the register resets its internal storage
            self.reg_bits.clear()
        if reg_enable == crtl_enable == 1:  # If the reg_inputs below are active, then the register will change
            curr_state = (s0, s1)
            self._reverse_register_bits(curr_state)
            self._register_outputs(s0, s1, reg_inputs)
            if curr_state != (0, 0):
                self.prev_state = curr_state

    def component_print(self):

        run_str = super().component_print().replace("\n\n", "")
        if self.prev_state == (1, 0):
            self.reg_bits.reverse()
            run_str += f'; Current registry: {self.reg_bits}'
            self.reg_bits.reverse()
        else:
            run_str += f'; Current registry: {self.reg_bits}'
        return run_str + '\n\n'

    def _register_outputs(self, s0, s1, reg_inputs):
        """
        The possible outputs of the register.

        Note that s0 = 1 and s1 = 0 or s0 = 0 and s1 = 1 access
        the same method instead of having a special case for this.
        This is because the bits were adjusted/"reversed" to adjust
        the bits beforehand.
        """

        if s0 != s1:
            self.output = self.reg_bits.shift_serial(reg_inputs)
        elif s0 and s1:
            self.output = self.reg_bits.shift_parallel(reg_inputs)

    def _reverse_register_bits(self, curr_state):
        """
        This reverses the register bits before applying the appropiate
        translation with RegisterBits methods.
        """

        if self.prev_state != curr_state and (curr_state == (1, 0) or self.prev_state == (1, 0)):
            self.reg_bits.reverse()


class _RegisterBits(list):
    """
    Helper class for register.

    This extends some of the funcionalities of the list class,
    so it behaves like internal registry of a shift register
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
