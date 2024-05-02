from visualgo.data_structures.number import Number

global p

p.x = Number(5)
p.y = Number(6)
p.comp = p.x < p.y
p.z = p.x + p.y
p.x = p.y
p.y -= Number(2)
