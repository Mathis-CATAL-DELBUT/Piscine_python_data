import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print(f"File {path} not found.")
        return None

    image = np.array(image)
    print(f"The shape of image is: {image.shape}")
    return image
