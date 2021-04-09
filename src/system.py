import itertools as it

_LINE_STR = '\n-------------------------------------------------------------------------------\n'


class DigitalSystem:
    """
    The digital system class. Its role is to evaluate the system.

    It basically runs through every component to get the current run in that
    run. With that, it creates a file that display how the system was running
    in each iteration.
    """

    def __init__(self, name, system_connections, num_of_runs=20):

        self.name = name
        self.layered_comps = []
        self.run_max = num_of_runs + 1
        self.sys_connections = system_connections

        self.organize_system()

    def organize_system(self):
        """
        This method traverses through the connections it was given to determine
        an order of execution for the components in the system.
        """

        for comp in self.sys_connections:
            if comp.layer_num is None:
                self._traverse_system(comp)

    def run_system(self):
        """
        Run the digital system.

        It creates the simulation text by running the system. The results of
        these will depend on what components you handed to the system.

        It does the following to do this:

        - It creates the simulation header. That is, the starting
          text and it shows the components initial conditions.

        - It later runs through each component and gets the current run of
          the component.

        - With all the information it has gathered, it will build the text file
          with all the runs of the simulation.
        """

        sim_text = self._create_simulation_header()
        for run_str in self._run_components():
            sim_text += run_str
        self._create_simulation_file(sim_text)

    def _create_simulation_file(self, sim_text):

        sim_text += 'Simulation End\n\n'
        with open(f'{self.name}.txt', 'w') as sim_file:
            sim_file.write(sim_text)

    def _create_simulation_header(self):

        start_str = f'This text file is a simulation of the system {self.name}.\n\n' \
                    'The following is the network layout of the system:\n\n'

        init_out_str = ""
        for layer_num, dig_comp_layer in enumerate(self.layered_comps):  # Get layer number and components in layer
            start_str += f'Layer {layer_num + 1}:\n\n'
            for dig_comp in dig_comp_layer:
                start_str += f'\t{dig_comp.name}'
                init_out_str += dig_comp.component_print()
            start_str += "\n\n"

        return start_str + _LINE_STR + 'Initial Component States:\n\n' \
               + init_out_str + _LINE_STR + "Simulation Start\n" + _LINE_STR

    def _map_component_to_layer(self, comp):

        comp_inputs = self.sys_connections[comp]
        if len(comp_inputs) == 0:  # If component does not have any inputs, put in first layer
            comp.layer_num = 0
        else:  # Verify the inputs layer numbers and use the highest number + 1 as the current component's layer number
            comp.layer_num = max(comp_input.layer_num for comp_input in comp_inputs) + 1

        if len(self.layered_comps) <= comp.layer_num:
            self.layered_comps.append([])
        self.layered_comps[comp.layer_num].append(comp)

    def _run_components(self):
        """
        To simplify a few things in the code, this method was made into a
        generator that returns a string of the run of the components. It stops
        early if it encounters a problem.
        """

        run_count = 1
        while run_count != self.run_max:
            run_str = ""  # String to save the run of components
            for dig_comp in it.chain.from_iterable(self.layered_comps):  # Go through each component in each layer
                dig_comp_inputs = [comp_input.run for comp_input in self.sys_connections[dig_comp]]  # Get inputs
                try:
                    dig_comp.run(dig_comp_inputs)
                    run_str += dig_comp.component_print()  # Add run of component to current run string

                # This creates an early stop to prevent any invalid data from appearing in the simulation
                except TypeError:
                    return
            yield f'RUN {run_count}:\n\n\n' + run_str + _LINE_STR
            run_count += 1

    def _traverse_system(self, comp):

        for comp_input in self.sys_connections[comp]:
            if comp_input.layer_num is None:
                self._traverse_system(comp_input)
        self._map_component_to_layer(comp)
