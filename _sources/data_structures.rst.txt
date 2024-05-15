Data Structures
===============

Data
----

.. autoclass:: data_structures.data.Data
   :members:
   :undoc-members:
   :show-inheritance:

Array
-----

.. autoclass:: data_structures.array.Array
   :members:
   :undoc-members:
   :show-inheritance:

Number
------

The `Number` class implement usual number, be it `int` or `float`. It allows visualgo to add behind the scene additional information for display purpose. The user can simply
deal with the `Number` class as they would with regular numbers. Especially the class supports standard operations (addition, substraction, multiplcation, power, division, euclidian
division and modulo) between `Number`, `int` and `float`.


.. autoclass:: data_structures.number.Number
   :members:
   :undoc-members:
   :show-inheritance:

Queue
-----

A queue is a simple data structure used to store value in a specific order. It follows the *First In First Out* (*FIFO*) rule which means that the first item added to the queue
is the first one to come out of the queue. The `Queue` class implement such data structure, providing useful methods described below such as `ìsEmpty` and `add`.


.. autoclass:: data_structures.queue.Queue
   :members:
   :undoc-members:
   :show-inheritance:

Stack
-----
A stack is a similar data structure to the queue. It follows the *First In Last Out* (*FILO*) rule also named the *Last In First Out* (*LIFO*) rule: the first element pushed onto 
the stack is the last one to be removed. It is implemented by the `Stack` class.

.. autoclass:: data_structures.stack.Stack
   :members:
   :undoc-members:
   :show-inheritance:

Tree
----
A tree is a data structure composed of a node and children. The node as a specific value while children are trees (or None). Trees are implmented by the `Tree` class.

.. autoclass:: data_structures.tree.Tree
   :members:
   :undoc-members:
   :show-inheritance:

Visualgo's tree implementation used a class named `Node`:

.. autoclass:: data_structures.tree.Node
   :members:
   :undoc-members:
   :show-inheritance: