import LogicCircuitSimulator.src as comps

a = comps.ConstOut('Cst1', 0)

b = comps.ConstOut('Cst2', 1)

c = comps.ConstOut('Cst3', 1)

d = comps.Gate('And1', 'and')

e = comps.Gate('And2', 'and')

f = comps.Gate('And3', 'and')

g = comps.Gate('And4', 'and')

connection_dict = {a: [], b: [], c: [], g: [c, d], d: [a, b, c], e: [b, c], f: [d, e]}


def order1(connection_dict):
    layer1 = []

    for key in connection_dict:

        if connection_dict[key] == []:
            layer1.append(key)

    return layer1


def order2(connection_dict, layer_list):
    layer = []

    for key in connection_dict:

        count = 0

        for value in connection_dict[key]:

            if value not in layer_list:

                break

            else:

                count += 1

        if count >= 1 and key not in layer:
            layer.append(key)

    return layer


def layer_list(connection_dict):
    layers = [order1(connection_dict)]

    index = 0

    comps = 0

    while comps != len(connection_dict):

        layers.append(order2(connection_dict, layers[index]))

        index += 1

        comps = 0

        for layer in layers:
            comps += len(layer)

    return layers


print(layer_list(connection_dict))
