# Functions

## Defining a Function

- Doctring: string literal that occurs as the _first statement_ in a module, function, class, or method definition; describes what the module, function, class or method does.

- Doctrings are usually enclosed in triple quotes, _which lets you write multiple lines of string_.

- parameter vs argument:\
   parameters are variables declared in a function's _definition_; whereas, arguments are values or data passed to a function when it's _called_ and assigned to corresponding parameters within the function.

## Passing Arguments

- Positional arguments are values passed to a function in the exact order the parameters are defined. Each argument is assigned to its corresponding parameter based on its position in the function call.

- Keyword arguments are values passed to a function by explicitly specifying the parameter names, allowing the arguments to be provided in any order.

- When calling functions, all keyword arguments must be passed after all positional arguments.

- When defining functions with default values, all parameters with defaults must come after all parameters without defaults.

## Return Value

- The `return` statement takes a value from inside a function and sends it back _to the line that called the function_.

## Passing an Arbitrary Number of Arguments

- Using an asterisk (\*) before a parameter in a function definition allows that parameter to collect an arbitrary number of positional arguments into a tuple.

- Using double asterisks (\*\*) before a parameter in a function definition allows that parameter to collect an arbitrary number of keyword (name-value pair) arguments into a dictionary.

## Storing Your Functions in Modules

- There a several ways to import and access functions from a module

  ### Importing Entire Module

  ```python
  import module_name

  module_name.fuction_name() # using imported fucntion
  ```

  ### Importing Specific Functions

  ```python
  from module_name import function_1, function_2

  function_1() # using imported fucntion
  ```

  ### Using `as` to Give a Function an Alias

  ```python
  from module_name import function_name as fn

  fn() # using imported fucntion
  ```

  ### Using `as` to Give a Module an Alias

  ```python
  import module_name as mn

  mn.function_name() # using imported fucntion
  ```

  ### Importing All Functions in a Module

  ```python
  from module_name import *
  function_name() # using imported fucntion
  ```
