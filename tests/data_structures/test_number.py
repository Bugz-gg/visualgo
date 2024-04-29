from visualgo.data_structures.number import Number
from visualgo.data_structures.number import Status

# --------------- Operator tests ---------------

def test_number_init():
    x = Number(1)
    assert x.value == 1
    
def test_number_assign():
    x = Number(1)
    y = Number(2)
    z = Number()
    
    x.assign(y)
    
    assert x.value == 2
    
    z.assign(x+y)
    
    assert z.value == 4
    
def test_number_add():
    x = Number(1)
    y = Number(2)
    z = Number()
    assert x.value == 1 
    assert y.value == 2
    z.assign(x + y)
    assert z.value == 3
    
def test_number_sub():
    x = Number(1)
    y = Number(2)
    z = Number()
    assert x.value == 1 
    assert y.value == 2
    z.assign(x - y)
    assert z.value == -1
    
def test_number_pow():
    x = Number(4)
    y = Number(2)
    z = Number()
    assert x.value == 4
    assert y.value == 2
    z.assign(x**y)
    assert z.value == 16
    
def test_number_mul():
    x = Number(4)
    y = Number(2)
    z = Number()
    assert x.value == 4
    assert y.value == 2
    z.assign(x*y)
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
    m = Number(2)
    n.assign(m)
    assert n.get_status() == Status.AFFECTED
    
def test_number_compared():
    x = Number(1) 
    y = Number(1)   
    x == y
    assert x.get_status() == Status.EQUAL
    assert y.get_status() == Status.EQUAL
    
def test_number_read():
    x = Number(1) 
    y = Number(1)
    z = Number()  
    assert x.get_status() == Status.CREATED
    assert y.get_status() == Status.CREATED
    assert z.get_status() == Status.CREATED    
    z.assign(x + y)
    assert x.get_status() == Status.READ
    assert y.get_status() == Status.READ
    assert z.get_status() == Status.AFFECTED    