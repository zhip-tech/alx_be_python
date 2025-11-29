def safe_divide(numerator, denominator):
    """Safely divide two values while handling numeric and zero-division errors."""

    # Convert inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Perform the division
    try:
        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
