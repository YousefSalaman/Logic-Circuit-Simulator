
from .base_comp import DigitalComponent


class Switch(DigitalComponent):
    """
    Digital switch component.

    This component can behave in 2 ways:

    - On-off switch: In this mode of operation, the switch takes only one
      component as input. Depending on the route value, the switch will pass
      on the current value of the input or it will act as a disconnected line.
      The latter means that it will pass as run the current value it has
      stored.

    - 2x1 MUX: In this mode of operation, the switch will route 1 of the 2
      input values.

    To get the first mode of operation, you only connect one input to the
    switch component. For the other, you connect 2 inputs.
    """

    def verify(self, inputs):
        """Assign the mode operation based on the inputs."""

        input_size = len(inputs)
        if input_size == 1:
            self.run = self._on_off_switch
        elif input_size == 2:
            self.run = self._2_by_1_mux
        else:
            raise AttributeError("A switch component must have either 1 or 2 inputs.")

    # Running switch methods

    def run(self, inputs):
        pass

    def _2_by_1_mux(self, inputs):
        """
        The behavior of the data routing switch.

        This switch behaves like a 2x1 MUX hence the name of the method.

        - When the route value is 0, the first input will be used as the
          run of the switch.

        - When the route value is 1, the second input will be used as the
          run of the switch.
        """

        route_value, *comp_inputs = inputs
        self.output = comp_inputs[route_value]

    def _on_off_switch(self, inputs):
        """
        The behavior of an on-off switch.

        - If the route_value is 1, the switch is on or "connected" and
          it will take the value of the input.

        - Otherwise, the switch is off and it will use the stored value
          as the run.
        """

        route_value, comp_input = inputs
        if route_value == 1:  # The on state is represented by 1
            self.output = comp_input
