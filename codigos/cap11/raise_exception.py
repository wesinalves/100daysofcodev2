def non_negative_integer(n):
    """ Converts argument n into a nonnegative integer, if possible.
    Raises a ValueError if the argument is not convertible
    to a nonnegative integer. """
    result = int(n)
    if result < 0:
        raise ValueError(result)
    return result

if __name__ == "__main__":
    while True:
        try:
            x = non_negative_integer(
                input('Please enter a nonnegative integer:')
            )
            if x == 999:
                break
        except ValueError:
            print('exception raised!')
        