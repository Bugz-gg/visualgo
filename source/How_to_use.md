# How to use Visualgo module ?

In this section, we are going to take a look at Visualgo module and study a simple utilization case.

## Installation

First, we are invitinig you to follow the **Getting started** guide in order to install Visualgo module on your device. You will then be able to freely import it in any *.py* file.


## How does it work ?

To explain how the module works, we are going to go over a simple example: implementing and visualizing `list_max` function which returns the maximum value of a list. Here is the pseudo-code of the function:
```

function list_max(L: list): number
    if is_empty(L)
        return null
    else
        m <- L[0]
        for i from 0 to size(L)
            if m < L[i]
                m = L[i]
        return m
```

Now, let's implement that with our module. The heart of Visualgo module is the **Program** class. It is an object to which any variable can be attached in order to keep track of their state and visualize them. At the beginning of your program, you first need to import Visualgo module with the following line :

```python
import visualgo as v
```

Then functions and classes of the module can be grabbed. Let's instantiate the **Program** class :
```
p = v.flow_control.Program()
```
You can notice in the previous line that the desired class comes from the submodule **flow_control** of Visualgo. That submodule is dedicated to keep track of the current program states. Now, we can implement the max function. In order to be added to the program, a variable has to be created as an attribute of the program. For instance, if one want a variable named **k** to have a value of 5 and to be part of the remembered variables of the program, it will be declared as the following:
```python
p.k = 5 # or p.k = v.data_structures.Number(5)
```
Visualgo module deal with data structures in its own way. It need an overlay to keep track of all information. Therefore it comes with its own data structres such as **Stack**, **Array** and **Number**. To make it easier for the user, number can be directly added as shown in the previous code line. However, special data structures such as **Tree** need to be declared with Visualgo submodule **data_structures**.

Now we can go further into the `list_max` function:
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

p.L = [5, 6, 8, 1, 2, 7]

x = list_max(p.L)

p.visualize()
```

In the previous code, the variable `m` that keeps track of the current maximum value encountered in the list `L` at each iteration of the for loop is declared as an attribute of the program. Usually, `m` would simply be a local variable of the function. However, Visualgo needs variable to be declared in such a way to keep track of their state. 

After the function was called, the method **visualize** of the **Program** class is used to display the execution of the whole program. Remember that only variable declared as attribute of the corresponding **Program** object will be displayed. Finally, each attribute of the **Program** class has an boolean attribute called **is_visualisable** that allow you to enable of disable the visualization of the said varaible at specific point of the program.
