
from .base_comp import DigitalComponent


class Gate(DigitalComponent):  # This class uses the commutativity of the logical operators
    """
    The logic gate component class.

    From here, one can create the following gates: AND, OR, XOR, NAND, NOR.

    It uses the component's commutativity and the associativity of the AND, OR, XOR gates
    to simplify the calculations being done. To briefly explain, the output is "calculated"
    by looking up the classes look up table. By using the two properties above, one can
    write up all the gates in this one class since they function in a similar manner.
    """

    _truth_table = {"AND": (0, 0, 1),
                    "OR": (0, 1, 1),
                    "XOR": (0, 1, 0),
                    "NAND": (1, 1, 0),
                    "NOR": (1, 0, 0)}

    def __init__(self, name, gate, init_state=0):

        self._checked = False
        self._verify_gate_parameter(gate)

        super().__init__(name, init_state)

    def _verify_gate_parameter(self, gate):

        try:
            gate = gate.strip().upper()
            if gate not in self._truth_table:
                raise AttributeError("The gate parameter that was entered is not a valid gate. "
                                     f'You must enter one of the following: {", ".join(self._truth_table.keys())}')
            self.gate = gate
        except AttributeError as error:
            raise AttributeError('The parameter "gate" must be a string and it must be '
                                 f'one of the following: {", ".join(self._truth_table.keys())}') from error

    def verify_component_inputs(self, inputs):

        # Checks once if the gate has the correct amount of reg_inputs
        if not self._checked:
            input_len = len(inputs)
            if input_len == 1:
                raise AttributeError("A Gate component must have 2 or more reg_inputs.")
            elif input_len > 2 and self.gate in ["NAND", "NOR"]:
                raise AttributeError(f'"{self.name}", which is a {self.gate} gate, '
                                     'cannot receive more than two reg_inputs.')
            self._checked = True

    def component_output(self, inputs):

        self.verify_component_inputs(inputs)

        output = self._truth_table[self.gate][inputs[0] + inputs[1]]  # Lookup the value in the truth table

        # Since some of the components are associative, I can continually use the previous value and a new input to get
        # or lookup the new value for the component
        for comp_input in inputs[2:]:
            output = self._truth_table[self.gate][output + comp_input]
        self.output = output
