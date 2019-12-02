# Python Journey - Chapter 19
# Define a function to be used in a unit test

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()