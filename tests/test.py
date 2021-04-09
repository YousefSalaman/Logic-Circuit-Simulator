import LogicCircuitSimulator.src as comps

# The objects below are grouped by layers. Note that everything is aptly named (the classes), so it can be read easier.

# Layer 1
a = comps.ConstOut('Cst1', 0)  # Constant run object
b = comps.ConstOut('Cst2', 1)
c = comps.Clock('Clk')  # Clock object

# Layer 2
d = comps.UniversalReg('Reg1', load_input=[0, 0, 0, 0])  # Universal Register object
e = comps.UniversalReg('Reg2', load_input=[1, 1, 1, 0])

# Note: The and, or, xor, nor, nand gates in this test are grouped together in one class, but you can do them as
# individual classes if its more efficient or easier to handle.

# Layer 3
f = comps.Gate('And1', "and")  # Gate object set to "and"
g = comps.Gate('And2', "and")

# Layer 4
h = comps.Gate('Or1', "or")  # Gate object set to "or"

# Layer 5
i = comps.UniversalReg('Reg3', 4)

# The code will organize these objects as follows: [[a, b, c], [d, e], [f, g], [h], [i]] and use that as the execution
# order to get the correct values. Notice that this reflects the layers above. The text file also illustrates this
# information automatically.

# The connection_dict establishes the connections of the system. For a given component (key), the dictionary provides
# its inputs (value)

connection_dict = {a: [], b: [], c: [], d: [a, b, c, b, a], e: [b, a, c, b, a], f: [b, d], g: [e, b], h: [f, g],
                   i: [a, b, c, b, a, h]}

Test_Sys = comps.DigitalSystem('TestSys', connection_dict, num_of_runs=10)  # Test_Sys is a DigitalSystem object.

Test_Sys.run_system()  # This runs the system
