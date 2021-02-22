
from .base_comp import DigitalComponent


class Switch(DigitalComponent):

    def __init__(self, name, init_state=0):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        route_value, *comp_inputs = inputs

        input_len = len(comp_inputs)
        if input_len == 1:  # On-off switch mode
            self._on_off_switch(route_value, comp_inputs[0])
        elif input_len == 2:  # 2x1 MUX mode
            self._2_by_1_mux(route_value, comp_inputs)
        else:
            raise ValueError("There can only be up to 3 inputs for a switch component.")

    def _2_by_1_mux(self, route_value, comp_inputs):
        """
        The behavior of the data routing switch.

        This switch behaves like a 2x1 MUX hence the name of the method.

        - When the route value is 0, the first input will be used as the
          output of the switch.

        - When the route value is 1, the second input will be used as the
          output of the switch.
        """

        if route_value == 0:
            self.output = comp_inputs[0]
        else:
            self.output = comp_inputs[1]

    def _on_off_switch(self, route_value, comp_input):
        """
        The behavior of an on-off switch.

        - If the route_value is 1, the switch is on or "connected" and
          it will take the value of the input.

        - Otherwise, the switch is off and it will use the stored value
          as the output.
        """

        if route_value == 1:  # The on state is represented by 1
            self.output = comp_input
