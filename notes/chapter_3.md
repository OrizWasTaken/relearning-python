# Introducing List

## Modifying, Adding, and Removing Elements

- Unlike strings, lists are mutable, meaning the contents of a list can be modified

- Adding Elements to a List

  `.append(object)`: append object to the _end of a list_.

  `.insert(index, object)`: Insert object _before index._

- Removing Elements from a List

  `.pop(self, index=-1)`: remove and _return_ item at index _(default last)_.

  `.remove()`: remove _first occurrence_ of value.

## Organizing a List

- `.sort(reverse=False)`: sort list in ascending order (descending order if `reverse=True`); _the list itself is modified_.

- `sorted(reverse=False)`: return a new list containing all items from the iterable in ascending order (descending order if `reverse=True`); _the original list is not modified_.

- `.reverse()`: reverse list order

## Avoiding Index Errors When Working with Lists

- `IndexError`: occurs when there is no item at the requested or specified index in an iterable.
