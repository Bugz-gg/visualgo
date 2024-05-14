# Writing programs

The first thing to do is to create a python file (*.py* file). Let's say we have a file named "*my_program.py*".

In that file we have to import the Visualgo library:

```python
import Visualgo as v
```

Now modules from the library can be freely used. Then, a instance of the class **Program** can be created. To do so, use the constructor from the *flow_control* module:

```python
p = v.flow_control.program.Program()
```

Now we have a variable `p` which is going to be used to store variable that we want to visualize.


## Manipulate data structures

In order to have more information about variables, Visualgo brings its own implementation of usual data structures such as arrays and trees.
They be found in the *data_structures* module.

The following subsections are dedicated to data structures currently supported by Visualgo


### Number

Numbers act as regular numbers (can be either an `int` or a `float`). They can be created with a any real value:

```python
a = v.datastructures.number.Number(5) # The value of the Number "a" is 5
b = v.datastructures.number.Number(-17.6) # The value of the Number "b" is -17.6
```
The Number class supports usual operator such ass addition and substraction:
```python
c = (a + b) / (-a * b) # type of "c" is Number
```


All following data structures contains only Numbers. Pythons's `int` and `float` are automatically transformed into Numbers when added to those data structures.

### Array

Arrays act the same as Python's arrays. They are created from Python's array as such:
```python
l = v.datastructures.array.Array([1, 2, 3])
```

The Array class has methods such as `append` to add elements or `isEmpty` to check is the array is empty or not. Please check the rest of the documentation
for a more detailed explanation of Array's methods.

### Stack
The Stack class implements stacks. An empty stack is created by calling the corresponding constructor:
```python
s = v.datastructures.queue.Stack()
```

Elements can then be added onto the stack with the `push` method and removed with the `pop` method. Please check the rest of the documentation
for a more detailed explanation of Stack's methods.

### Queue
The Queue class implements queues. An empty queue is created by calling the corresponding constructor:
```python
s = v.datastructures.queue.Queue()
```

Elements can then be added at the beginning the queue with the `add` method and removed from the end with the `remove` method. Please check the rest of the documentation
for a more detailed explanation of Queue's methods.

### Tree
The Tree class allows you to created your own trees. An empty tree is created by calling the corresponding constructor:
```python
s = v.datastructures.tree.Tree()
```
Children can be added, remove and more with the corresponding methods.Please check the rest of the documentation
for a more detailed explanation of Tree's methods.


### And what about the Program class ?

Well, all previous data structures can be added as attribute to a Program like this:

```python
p.l = v.datastructures.array.Array([1, 2, 3])
```

All variables that as to be visualized have to be added to the the instance of the Program class. If at some point of the program there is no more need to visualize a specific variable, its vizualisation can be disable by changing its `is_visible` attribute to `False` (all data structures from Visualgo library possess such attribute).


## The first program (and the first visualization)

Let's write a function that determine that maximum value of an Array. Here is the code:

```python
def list_max(L):
    if L.isEmpty():
        return None
    else:
        p.m = L[0]
        for i in range(0, L.size()):
            if p.m < L[i]:
                p.m = L[i]
        return p.m
```

Now the function can be called on an Array variable:

```python
p.L = [5, 6, 8, 1, 2, 7] # The Python array is automatically converted into a Visualgo's Array by "p"

x = list_max(p.L)
```

Now there are two ways to display the algorithm running :
1. Using the `visualize` method from the Program class by simply adding `p.visualize()` at the end of the previous code.
2. Creating a new filed (let's say "*lauch.py*") in which Visualgo is imported and the static method `wrap_code_to_function` is called with `"./my_program.py"` as an argument.

The second option is better because it runs the graphic interface and the code of "*my_program.py*" in seperated thread. The is useful to still get a display even is the program displayed never end (infinite loop of whatever).