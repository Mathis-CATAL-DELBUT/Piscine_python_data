import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a given path
    """
    if type(path) is not str:
        raise TypeError("Invalid type")
    try:
        image = Image.open(path)
        image = np.array(image)
    except PermissionError:
        raise ValueError("Permission denied")
    except FileNotFoundError:
        raise ValueError("File not found")
    except Exception:
        raise ValueError("An error occurred")
    return image
