import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a list of lists
    """
    if (
        family is None
        or type(family) is not list
        or type(start) is not int
        or type(end) is not int
    ):
        raise TypeError("Invalid type")
    if start > len(family) or end > len(family):
        raise ValueError("Out of range")
    family = np.array(family)
    print(f"My shape is : {family.shape}")
    family = family[start:end]
    print(f"My new shape is : {family.shape}")
    family = family.tolist()
    return family
