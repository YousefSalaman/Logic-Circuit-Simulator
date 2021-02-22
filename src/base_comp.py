
from abc import abstractmethod, ABC


class DigitalComponent(ABC):
    """
    Base class for the project's digital components.
    """

    def __init__(self, name, init_state=0):

        self.name = name
        self.layer_num = None
        if init_state not in (0, 1):
            raise AttributeError('The "init_state" parameter must be either 0 or 1.')
        self.output = init_state

    def __repr__(self):

        return self.name

    def component_print(self):

        return f'{self.name} output: {self.output}\n\n'

    @abstractmethod
    def component_output(self, inputs):
        pass
