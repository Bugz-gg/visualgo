# Adding visual structure

## Requirements
### get_flat_data()
Any new visual structure should implement the abstract class `VisualWidget`.

You must correctly implement the `get_flat_data()` method that return a list of **all** the instances of `VisualWidget` contained 
within your new class.

If your class contain a singular value, it should be something along :
```python
return [self]
```
If your class is container of some sort, you should return the instance of the container as well as the 
instances of the contained attributes
```python
return [self] + self.list_of_contained_values
```

## Other features
There are two very useful features that you should be aware of :

### size_hint()
This method allow you to specify to the visualizer the size that your structure needs. It returns a QSize of pyQt5.

### zoom
Handling zoom is essential in order for your structure to react well with user interactions.
Refer to the `WidgetWithZoom` class to get more details. 
