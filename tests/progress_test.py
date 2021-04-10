
import itertools as it

import LogicCircuitSimulator.src as comps


a = comps.ConstOut('Cst1', 0)

b = comps.ConstOut('Cst2', 1)

c = comps.ConstOut('Cst3', 1)

d = comps.Gate('And1', 'and')

e = comps.Gate('And2', 'and')

f = comps.Gate('And3', 'and')

g = comps.Gate('And4', 'and')

connection_dict = {a: [], b: [], c: [], g: [c, d], d: [a, b, c], e: [b, c], f: [d, e]}


def organize_comps(connections):

    # Create comp_layers and append the first layer
    layers = [[comp for comp in connections if connections[comp] == []]]

    comp_count = len(layers[0])
    num_of_comps = len(connections)
    while comp_count != num_of_comps:

        # Create new layer and update component counter
        new_layer = _create_layer(connections, layers)
        layers.append(new_layer)
        comp_count += len(new_layer)

    return layers


def _create_layer(connections, layer_list):

    # List of components that have been organized/mapped into a layer
    mapped_comps = list(it.chain.from_iterable(layer_list))

    layer = []
    for comp, input_comps in connections.items():
        if comp not in layer \
                and comp not in mapped_comps \
                and all(input_comp in mapped_comps for input_comp in input_comps):

            layer.append(comp)

    return layer


comp_layers = organize_comps(connection_dict)
print(comp_layers)
