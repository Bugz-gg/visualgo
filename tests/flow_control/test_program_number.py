from visualgo.flow_control.program import Program
from visualgo.data_structures.number import Number


# Test if number can be added to program
def test_program_number():
    p=Program()
    x = Number(5)
    p.x = x
    p.y = 5
    assert p.y.value == 5
    assert p.x.value == 5
    assert p.y.value == p.x.value


# Number not fully implemented so not working
# Test if number can be added/substracted/multiplied/divised together
# def test_program_number_op():
#     p = Program()
#     p.x = 10
#     p.y = 5
#     p.z = p.x + p.y
#     assert p.z.value == 15
