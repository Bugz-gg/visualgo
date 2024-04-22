from visualgo.flow_control.program import Program
from visualgo.data_structures.stack import Stack


def test_program_stack():
    p = Program()
    p.s = Stack()
    assert type(p.s) == Stack
    p.s.push(5)
    p.s.push(6)
    assert p.s.size() == 2
    assert p.s.pop() == 6
    assert p.s.size() == 1
    assert p.s.pop() == 5
    assert p.s.size() == 0
    assert p.s.isEmpty()
