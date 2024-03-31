from visualgo.flow_control import program
from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
p = program.Program()

x = Number(9)
p.x = 4
p.x = 5
print(p.historic)
