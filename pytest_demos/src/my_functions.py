def add(num_one, num_two):
    """Add two numbers together."""
    return num_one + num_two

def divide(num_one, num_two):
    """Divide two numbers."""
    if num_two == 0:
        raise ValueError("Cannot divide by zero.")
    return num_one / num_two
