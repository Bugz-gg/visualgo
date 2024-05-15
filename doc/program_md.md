# `Program` class

The `Program` class has by default two attributes :
 - `historic`: an array used to store every step of the program,
 - `worker`:

## Saving variables
An important method of the `Program` class is `log`. Everytime it is called, all variables of the program except the two previously mentionned are saved inside historic.
Everytime something within the program happens, `log` is called to keep track of every changement.


## Adding and modifying variables
When a user wants to keep track of a variable, he has to declare as an attibute of an instance of `Program`. For instance, the following code show how
to declare and add the variable `x` of value `5` to a `Program` named `p`:
```python
p.x = 5
```

In Python, new attributes can be freely created by simply affecting a value to it. When Python tries to the set a value of an attribute, it checks if the attribute exists.
If it does, the value is simply changed, otherwise the attribute is created and its value set. This is done implicitly done with the `__setattr__` method. Here, the method is
overrided in order to do additionnal operations:
- Everytime `__setattr__` is called, the `log` method is also called in order to take into account the new state of the whole program.
- The type of the value is checked in order to apply needed transformations (such as `int` or `float` into `Number`) and to raise en error if the type is not supported.


## Accesing a value
Any attribute can easely be accessed via the usual way:
```python
p.x
```
But behind the scene, the `__getattr__` method is called. This method also save the state of the program by calling `log`.