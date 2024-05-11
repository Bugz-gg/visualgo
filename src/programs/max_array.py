from visualgo.data_structures.array import Array

global p

p.array = Array()
array_size = 3
for p.i in range(array_size):
    p.array.append(p.i)

p.max = 0
for p.i in range(array_size):
    p.current = p.array.get(p.i)
    if p.current > p.max:
        p.max = p.current

