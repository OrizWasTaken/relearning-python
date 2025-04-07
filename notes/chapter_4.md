# Working with Lists

## Avoiding Indentation Errors

- Variables declared in a `for` loop in Python persist after the loop ends and retain the last value they held during iteration.

## Making Numerical Lists

- `range(stop)`,\
  `range(start, stop[, step])`:\
  returns an object that produces a sequence of integers from `start` (inclusive, defaults to 0) to `stop` (exclusive) by `step` (defaults to 1)

- List comprehension: a concise way to create lists.

  Syntax:

  ```python
  list = [expression for item in iterable]
  ```

  each item in the `list` is the result of the `expression` applied to each `item` in the `iterable`.

## Working with part of a list

- slicing a list:

  Syntax:

  ```python
    list[start:stop:step]
  ```

  returns a subset of the `list`, sliced from `start` (inclusive, defaults to 0) to `stop` (exclusive, defaults to -1), stepping by `step` (defaults to 1).

- Assigning one list to another using `=` creates a new reference to the original list, not a new list. An actual, independent copy can be made by slicing the entire list:

  ```python
  new = old[:]
  ```

## Tuples

- Unlike lists, tuples are _immutable_.

- Tuples are defined by the presence of a comma; the parentheses make them
  look neater and more readable.

  ```python
  >>> tuple = 3,2
  >>> tuple
  >>> (3,2)
  ```
