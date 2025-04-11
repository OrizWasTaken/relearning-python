# Dictionaries

## Working with Dictionaries

- Dictionary keys must be of an immutable object type, such as strings, numbers, and tuples.

- Dictionary values can be of any object type.

- Dictionaries, like lists, are mutable and retain the other in which they were defined.

- `.get(key, default=None)`: returns the value for a key if key exists; otherwise returns `default`; often preferable to the square bracket notation, which raises a `KeyError` for missing keys.

## Looping Through a Dictiobary

- `.items()`: returns a sequence of the key-value pairs in a dictionary.

- `.keys()`: returns a sequence of the keys in a dictionary

- looping through the keys of a dictionary is the default behavior when looping through a dictionary.

  That is:

  ```python
  for key in dictionary:
  ```

  is the same as:

  ```python
  for key in dictionary.keys():
  ```

- `.values()`:returns a sequence of the values in a dictionary.

- set: an unordered collection of unique elements. Like dictionary, sets are defined with curly braces.

- `set(iterable)`: converts an iterable to a set; useful for removing duplicate values, such as when working with `dictionary.values()`.
