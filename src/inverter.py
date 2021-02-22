
from .base_comp import DigitalComponent


class Inverter(DigitalComponent):

    def __init__(self, name, init_state='off'):

        super().__init__(name, init_state)

    def component_output(self, inputs):

        self.output = int(not inputs[0])
