def safe_divide(numerator, denominator):
    """Safely divide two values, handling numeric errors and zero division."""

    # Convert inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Both inputs must be numeric."

    # Perform the division
    try:
        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
