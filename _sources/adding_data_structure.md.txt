# Adding data structures

## Requirements

Your new data structure must inherit from the `Data` class. 

Hence, you must add the method `get_flat_data`, that returns a list of all the instances of Data contained inside your data structure.
If it is a singular value, it should be something like
```python
return [self]
```
If you are building a container, it should resemble :
```python
return [self] + list_of_contained_data
```

The `get_flat_data` method is mainly used for status reset, if you encounter problem with status not resetting, it might
be the fault of get_flat_data not correctly implemented.

## Status handling
The tricky part is the status handling.

If you are building a container, you don't have to worry too much about it,
as the inside Data instances will handle their status.
Although, you can implement the following status :
- If there is access for a value inside, mark it as `Status.LOOKED_INSIDE`
- If a value is removed, mark is as `Status.REMOVED_INSIDE`

Otherwise, when the value is :
- created, mark it as `Status.CREATED`
- accessed, mark it as `Status.READ`,
- written, mark it as `Status.AFFECTED`
- compared, mark it with one of the comparator value, `Status.LESS_THAN`, `Status.GREATER_THAN`, `Status.EQUAL`, `Status.DIFFERENT`

The default status is `Status.None`.
