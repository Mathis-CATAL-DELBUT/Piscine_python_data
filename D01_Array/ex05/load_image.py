from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    Load an image from a given path
    """
    if type(path) is not str or Image.open(path) is None:
        print("Invalid path")
        exit(1)
    return np.array(Image.open(path))
