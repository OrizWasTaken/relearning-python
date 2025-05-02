class Employee:
    """create an instance of an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """initialize employee object"""
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = annual_salary

    def give_raise(self, amount=5000):
        """adds to employee's annual salary"""
        self.salary += amount