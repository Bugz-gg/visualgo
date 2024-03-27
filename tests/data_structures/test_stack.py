from visualgo.data_structures.stack import Stack

def test_stack_init():
    stack = Stack(True)
    assert stack.isEmpty() == True
    
def test_stack_push():
    stack = Stack(True)
    stack.push(1)
    assert stack.isEmpty() == False
    assert stack.size() == 1
    assert stack.data[0] == 1

def test_stack_pop():
    stack = Stack(True)
    # stack.Pop() # test error case
    assert stack.isEmpty() == True
    
    stack.push(1)
    value = stack.pop()
    print(stack.data)
    assert value == 1    
    