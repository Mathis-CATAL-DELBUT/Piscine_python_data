import numpy as np
import matplotlib.pyplot as plt


def display(array, message) -> None:
    """
    Display
    """
    print("The shape of the image is: ", array.shape)
    print(array)
    print(message)
    plt.imshow(array)
    plt.show()


def ft_invert(array) -> np.array:
    """
    Invert the colors of an image
    """
    display(255 - array, "Inverts the color of the image received.")
    return 255 - array


def ft_red(array) -> np.array:
    """
    Keep only the red channel of an image
    """
    red_array = np.zeros(array.shape, dtype=np.uint8)
    red_array[:, :, 0] = array[:, :, 0]
    display(red_array, "Keeps only the red channel of the image received.")
    return red_array


def ft_green(array) -> np.array:
    """
    Keep only the green channel of an image
    """
    green_array = np.zeros(array.shape, dtype=np.uint8)
    green_array[:, :, 1] = array[:, :, 1]
    display(green_array, "Keeps only the green channel of the image received.")
    return green_array


def ft_blue(array) -> np.array:
    """
    Keep only the blue channel of an image
    """
    blue_array = np.zeros(array.shape, dtype=np.uint8)
    blue_array[:, :, 2] = array[:, :, 2]
    display(blue_array, "Keeps only the blue channel of the image received.")
    return blue_array


def ft_grey(array) -> np.array:
    """
    convert an image to grayscale
    """
    grey_array = np.zeros((array.shape[0], array.shape[1], 1), dtype=np.uint8)
    grey_array[:, :, 0] = (np.sum(array, axis=2) / 3).astype(np.uint8)
    plt.imshow(grey_array, cmap="gray")
    plt.show()
    print("Converts the image to grayscale")
    return grey_array
