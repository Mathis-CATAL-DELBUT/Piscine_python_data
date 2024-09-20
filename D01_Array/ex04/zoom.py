import numpy as np


def zoom(X: int, Y: int, array_image: np.array):
    """
    Zoom the image to the specified dimensions.
    """
    middle = []
    middle.append(array_image.shape[0] // 2)
    middle.append(array_image.shape[1] // 2)
    if (
        (X / 2 + middle[0] > array_image.shape[0])
        or (middle[0] - X / 2 < 0)
        or (Y / 2 + middle[1] > array_image.shape[1])
        or (middle[1] - Y / 2 < 0)
    ):
        print("The zoom is not possible")
    start_x = array_image.shape[0] // 2 - X // 2
    end_x = array_image.shape[0] // 2 + X // 2
    start_y = array_image.shape[1] // 2 - Y // 2
    end_y = array_image.shape[1] // 2 + Y // 2
    new_image = array_image[start_x:end_x, start_y:end_y]
    return np.array(new_image)
