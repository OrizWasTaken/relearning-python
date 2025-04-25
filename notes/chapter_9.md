# Classes

## Creating and Using a Class

- Making an object from a class is called instantiation, and objects are instances of classes.

- Classes are declared in PascalCase

- Methods are funcions attached to a class, and available to the class' instances.

- Attributes are variables attached to a class, and available to the class' instances.

- During instantiation, python creates a new instance of a class, then calls its `__init__` method, passing the instance itself as the first argument.

  That is:

  ```python
  class Dog:
    def __init__(self, name):
      self.name = name

  dog = Dog('joe')
  ```

  results in:

  ```python
  dog = Dog.__new__(Dog, 'joe') # Dog is instantiated as dog
  dog.__init__(dog, 'joe') # dog is automatically passed as self
  ```

- Names with double leading and trailing underscores, like `__init__`, are reserved for special methods and attributes defined by Python.

- After instantiation, the first paremter of all instance methods, conventionally names `self`, points to the specific instance in memory

  That is:

  ```python
  self.name = name
  ```

  becomes

  ```python
  dog.name = name
  ```

## Working with Classes and Instances

- An attribute’s value can be modified:

  ### Directly through an Instance:

  ```python
  instance_name.attribute_name = value
  ```

  ### Through a Method:

  ```python
    class className:
        --snip--

        def update_value(self, value): # defining method for updating value
            self.attribute_name = value

        ---snip---

    instance_name.update_value(value) # calling method, passing new value
  ```

## Inheritance

- A child class is a specialized version of another class, called a parent class, that inherits any or all of the attributes and methods of the parent class.

- For a class to inherit attributes and methods from another class, the name of the parent class must be placed in parentheses when defining the child class.

- The `super()` function returns a temporary object of the parent class, giving access to its methods and properties without explicitly naming the parent.

- The `super()` function is most commonly used to call and initialize the parent class’s constructor(`__init__`) within the constructor of a child.

  ```python
    class Child(Parent): # inherit parent's methods & attributes
      """child"""
      def __init__(self, arg, arg2):
        """initialize parent when initialized"""
        super().__init__(arg) # super() gives access to Parent's constructor
  ```

- A child class can be customized by adding new attributes and methods or by overriding those inherited from its parent class.

- A class can have instances of other classes as attributes, allowing it to model complex relationships and behaviors.

  ```python
    class Battery:
      --snip--

    class Car:
      def __init__(self):
        self.battery = Battery() # create instance of Battery as battery
  ```

- Classes can be imported and accessed from a module in the same way as functions.
