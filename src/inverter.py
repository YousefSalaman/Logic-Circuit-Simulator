from .base_comp import DigitalComponent


class Inverter(DigitalComponent):
    """
    Inverter component.
    
    This component inverts the values it is given.
    """

    def run(self, inputs):

        self.output = int(not inputs[0])

    def verify(self, inputs):

        if len(inputs) != 1:
            raise AttributeError("An inverter component must only have 1 input.")
