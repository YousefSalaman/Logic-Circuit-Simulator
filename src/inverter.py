from .base_comp import DigitalComponent


class Inverter(DigitalComponent):
    """
    Inverter component.
    
    This component inverts the values it is given.
    """

    def run(self, inputs):
        self.output = int(not inputs[0])
