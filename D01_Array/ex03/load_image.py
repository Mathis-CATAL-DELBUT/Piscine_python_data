from PIL import Image
import numpy as np


def load_image(path: str):
    """
    Load an image from a given path
    """
    if type(path) is not str or Image.open(path) is None:
        print("Invalid path")
        exit(1)
    return Image.open(path), np.array(Image.open(path))
