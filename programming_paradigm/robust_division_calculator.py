def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result:.1f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
