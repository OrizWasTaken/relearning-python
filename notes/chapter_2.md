# Variables and Simple Data Types

## Variables

- `NameError`: usually means a variable is misspelled or undefined.

## String

- Strings are immutable. Therefore, methods called on strings do not change the original strings, but create new strings.

- Whitespace refers to any nonprinting characters, such as
  spaces, tabs (`\t`), and newline (`\n`) symbols.

- `removeprefix()` and `removesuffix()` are two new methods helpful when working with files and URLs.

## Numbers

- The quotient of two numbers, even if both numbers are integers, is _always_ a float.

- The output of any operation that involves a float is _always_ a float.

- Multiple variable can be declared on a single line, a technique used most often when initializing a set of numbers

  ```python
  x, y, z = 0, 0, 0
  ```

- Python doesn't have a _constant_ data type, but python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed.
