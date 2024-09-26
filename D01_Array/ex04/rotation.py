import numpy as np


def rotate(image: np.array):
    """
    Rotate an image 90 degrees
    """
    if type(image) is not np.ndarray:
        raise TypeError("Invalid type")
    r_image = np.zeros((image.shape[1], image.shape[0], 1), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r_image[400 - j - 1][i][0] = image[i][j][0]

    return r_image
