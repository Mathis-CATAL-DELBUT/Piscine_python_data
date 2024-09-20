import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if (
        family is None
        or type(family) is not list
        or type(start) is not int
        or type(end) is not int
    ):
        return None
    family = np.array(family)
    print(f"My shape is : {family.shape}")
    family = family[start:end]
    print(f"My new shape is : {family.shape}")
    family = family.tolist()
    return family
