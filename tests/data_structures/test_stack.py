from visualgo.data_structures.stack import Stack
from visualgo.data_structures.data import Status
from visualgo.data_structures.number import Number

import pytest


def test_stack_init():
    stack = Stack()
    assert stack.isEmpty()
    
def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.isEmpty() == False
    assert stack.size() == 1
    assert stack.value[0] == 1

def test_stack_pop():
    stack = Stack()
    
    assert stack.isEmpty()
    
    # testing error case
    with pytest.raises(AssertionError) as exc_info:
        stack.pop()
    assert exc_info.value.args[0] == "stack is empty"
    
    
    stack.push(1)
    value = stack.pop()
    assert value == 1    
    
def test_stack_peep():
    stack = Stack()
    assert stack.isEmpty()

    stack.push(42)
    assert stack.isEmpty() != True
    assert stack.peep() == 42

# --------------- Status tests ---------------

def test_number_status_created():
    s = Stack()
    assert s.get_status() == Status.CREATED
    s.push(Number(1))
    assert s.get_status() != Status.CREATED
    assert s.get_status() == Status.READ
    
def test_number_affected():
    s = Stack()
    s.value = []
    assert s.get_status() == Status.AFFECTED

def test_number_compared():
    s1 = Stack()
    s2 = Stack()
    s1 == s2
    assert s1.get_status() == Status.COMPARED
    