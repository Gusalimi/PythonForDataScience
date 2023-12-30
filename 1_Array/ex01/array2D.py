import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Prints the shape of a list and returns a sliced version"""
    if (not isinstance(family, list)):
        raise TypeError("family must be a list")
    if (not isinstance(start, int) or not isinstance(end, int)):
        raise TypeError("start and end must be ints")
    lst = np.array(family)
    print(f"My shape is : {lst.shape}")
    print(f"My new shape is : {lst[start:end].shape}")
    return list(family[start:end])
