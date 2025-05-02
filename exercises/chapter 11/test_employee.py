from employee import Employee
import pytest

@pytest.fixture
def joseph():
    joe = Employee('joseph', 'orisakwe', 250_000)
    return joe

def test_give_default_raise(joseph):
    """Test that give_raise increases salary by the default 5000."""
    initial_salary = joseph.salary

    joseph.give_raise()
    new_salary = joseph.salary

    assert new_salary - initial_salary == 5000

def test_give_custom_raise(joseph):
    """Test that give_raise adds a custom amount to salary when specified."""
    initial_salary = joseph.salary

    custom_raise = 50_000
    joseph.give_raise(custom_raise)
    new_salary = joseph.salary
    
    assert new_salary - initial_salary == custom_raise