# Testing Your Code

## Installing pytest with pip

- upgrading a package

  ```shell
  $ pip install --upgrade package_name
  ```

- Installing a package

  ```shell
  $ pip install package_name
  ```

## Testing a Function

- Pytest is a Python testing framework used to write, organize, and run test cases efficiently.

- To run tests with `pytest`, navigate to the directory containing the test files and run the command: `pytest` in the terminal.

- Test file names should start with `test_` to be auto-discovered by pytest.

- Test functions should start with `test_` so pytest can automatically detect and run them.

- An assertion is a condition that pytest checks to verify the correctness of the code during testing.

- An assertion is created by using the assert keyword followed by a condition:

  ```python
  assert jesus > circumstances
  ```

## Testing a class

- A fixture is a function in pytest used to set up and provide resources or test dependencies before tests run.

- Fixtures are created by using the `@pytest.fixture` decorator (accessible on pytest import) before the fixture function:

  ```python
  import pytest

  @pytest.fixture
  def fixture_name():
      # Setup code goes here
    ...
  ```

- A decorator is a function that modifies or extends the behavior of another function without changing its code.

- For a fixture to be used in a test, include its name as a parameter in the test function; this automatically injects the fixture's return value into the test function:

  ```python
  import pytest

  @pytest.fixture
  def fixture_name():
    --snip--
    return value

  def test_function(fixture_name):
    ...
  ```
