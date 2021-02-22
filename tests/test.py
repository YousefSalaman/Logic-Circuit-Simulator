import LogicCircuitSimulator.src as comps

# The objects below are grouped by layers. Note that everything is aptly named,
# so it can be read easier.

a = comps.ConstOut('Cst1', 0)  # Constant output object
b = comps.ConstOut('Cst2', 1)
c = comps.Clock('Clk')  # Clock object

d = comps.UniversalReg('Reg1', 4, [0, 0, 0, 0])  # Universal Register object
e = comps.UniversalReg('Reg2', 4, [1, 1, 1, 0])

f = comps.Gate('And1', "and")
g = comps.Gate('And2', "and")

h = comps.Gate('Or1', "or")  # OrGate object

i = comps.UniversalReg('Reg3', 4)

# The connection_dict establishes the connections of the system and network_layout
# specifies the order in which the components need to be evaluated. Note that
# both of these could've been done with an ordered dict object from the
# python collection package, but I decided to use a list and dictionary for
# this task.

connection_dict = {a: [], b: [], c: [], d: [a, b, c, b, a], e: [b, a, c, b, a], f: [b, d], g: [e, b], h: [f, g],
                   i: [a, b, c, b, a, h]}

Test_Sys = comps.DigitalSystem('TestSys', connection_dict,
                               num_of_runs=10)  # Test_Sys is a DigitalSystem object.

Test_Sys.run_system()  # This runs the system
