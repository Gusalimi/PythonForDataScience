def square(x: int | float) -> int | float:
    """Return the square of x."""
    return (x * x)


def pow(x: int | float) -> int | float:
    """Return x to the power of x."""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Return a function that will apply function to x n times."""
    count = 0

    def inner() -> float:
        """Apply function to x n times."""
        nonlocal count
        count += 1
        ret = x
        for i in range(count):
            ret = function(ret)
        return ret
    return inner
