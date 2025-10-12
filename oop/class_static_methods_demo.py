# class_static_methods_demo.py

class Calculator:
    """A simple calculator class demonstrating class and static methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Returns the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Returns the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Returns the quotient of two numbers. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
