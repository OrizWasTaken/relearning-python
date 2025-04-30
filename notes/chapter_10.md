# Files and Exceptions

## Reading from a file

- pathlib is an os-independent module (library) for working with files and directories.

- `read_text()`: a `Path` method that opens a file in text mode, reads it, and closes the file; returns contents of a file as a string.

- forward slash (/) instead of a backslash (\\) should be used when displaying file paths, as the backslash is primarily used as an escape character.

- `splitlines()`: string methods that returns a list of the lines in the string, breaking at line boundaries.

## Writing to a file

- `write_text()`: a `Path` method that opens a file in text mode, writes to it, and closes the file.

- The `write_text()` method takes only string arguments as Python can only write strings to a text file.

## Exceptions

- The `else` block in a `try-except` statements contains code that depends on the `try` block executing successfully, allowing the `try` block to contain only the code that might cause the error.

## Storing Data

- `json.dumps()`: a `json` function that converts simple Python data structures into JSON-formatted strings

- `json.loads()`: a `json` function that converst JSON-formatted strings into Python objects
