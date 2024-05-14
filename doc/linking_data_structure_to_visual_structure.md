# Linking data structures to visual structures

Once you have your new data structure and your desired, potentially new, visual structure, it is time to link them together.
Head towards `visualgo/visu/programState.py`, and inside the `resolve_visual_structure` function, add a new case for 
your structure.
```python
if isinstance(value, YourNewDataStructure):
    return ChosenVisualWidget(value)
```

You are now good to go.