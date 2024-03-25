from visualgo.data_structures.stack import Stack

def test_stack_init():
    stack = Stack(True)
    assert stack.IsEmpty() == True
    
def test_stack_push():
    stack = Stack(True)
    stack.Push(1)
    assert stack.IsEmpty() == False
    assert stack.Size() == 1
    assert stack.data[0] == 1

def test_stack_pop():
    stack = Stack(True)
    # stack.Pop() # test error case
    assert stack.IsEmpty() == True
    
    stack.Push(1)
    value = stack.Pop()
    print(stack.data)
    assert value == 1    
    