from visualgo.data_structures.queue import Queue
from visualgo.data_structures.number import Number
from visualgo.data_structures.data import Status

import pytest



def test_stack_init():
    stack = Queue()
    assert stack.isEmpty()
    
def test_stack_add():
    stack = Queue()
    stack.add(1)
    assert stack.isEmpty() == False
    assert stack.size() == 1
    assert stack.value[0] == 1

def test_stack_remove():
    stack = Queue()
    
    assert stack.isEmpty()
    
    # testing error case
    with pytest.raises(AssertionError) as exc_info:
        stack.remove()
    assert exc_info.value.args[0] == "queue is empty"
    
    
    stack.add(1)
    value = stack.remove()
    assert value == 1    
    
# --------------- Status tests ---------------

def test_number_status_created():
    s = Queue()
    assert s.get_status() == Status.CREATED
    s.add(Number(1))
    assert s.get_status() != Status.CREATED
    assert s.get_status() == Status.READ
    
def test_number_affected():
    s = Queue()
    q = Queue()
    s.assign(q)
    assert s.get_status() == Status.AFFECTED

def test_number_compared():
    s1 = Queue()
    s2 = Queue()
    s1 == s2
    assert s1.get_status() == Status.EQUAL
    