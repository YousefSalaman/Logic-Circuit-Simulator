
from .base_comp import DigitalComponent


class Inverter(DigitalComponent):
    """
    Inverter component.
    
    This component inverts the values it is given.
    """
    

    def __init__(self, name, init_state=0):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        self.output = int(not inputs[0])
