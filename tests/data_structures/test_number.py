from visualgo.data_structures.number import Number
from visualgo.data_structures.number import Status

# --------------- Operator tests ---------------

def test_number_init():
    x = Number(1)
    assert x.value == 1
    
def test_number_add():
    x = Number(1)
    y = Number(2)
    assert x.value == 1 
    assert y.value == 2
    z = x + y
    assert z.value == 3
    
def test_number_sub():
    x = Number(1)
    y = Number(2)
    assert x.value == 1 
    assert y.value == 2
    z = x - y
    assert z.value == -1
    
def test_number_pow():
    x = Number(4)
    y = Number(2)
    assert x.value == 4
    assert y.value == 2
    z = x**y
    assert z.value == 16
    
def test_number_mul():
    x = Number(4)
    y = Number(2)
    assert x.value == 4
    assert y.value == 2
    z = x*y
    assert z.value == 8
    
def test_number_iadd():
    x = Number(1)
    y = Number(1)
    assert x.value == 1
    x += y
    assert isinstance(x, Number)
    assert x.value == 2
    
def test_number_isub():
    x = Number(1)
    y = Number(1)
    assert x.value == 1
    x -= y
    assert isinstance(x, Number)
    assert x.value == 0
    
def test_number_imult():
    x = Number(2)
    y = Number(3)
    assert x.value == 2
    x *= y
    assert isinstance(x, Number)
    assert x.value == 6

# --------------- Status tests ---------------

def test_number_status_created():
    n = Number(1)
    assert n.get_status() == Status.CREATED
    
def test_number_affected():
    n = Number(1)
    n.value = 3
    assert n.get_status() == Status.AFFECTED
    
def test_number_compared():
    x = Number(1) 
    y = Number(1)   
    x == y
    assert x.get_status() == Status.COMPARED
    