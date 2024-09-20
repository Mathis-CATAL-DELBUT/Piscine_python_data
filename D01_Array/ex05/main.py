from load_image import load_image
from matplotlib import pyplot as plt
import numpy as np


def to_gray(image: np.array):
    """
    Convert an image to grayscale
    """
    grey_image = np.zeros((image.shape[0], image.shape[1], 1), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            grey_image[i][j][0] = int(
                round(
                    image[i][j][0] * 0.2989
                    + image[i][j][1] * 0.587
                    + image[i][j][2] * 0.114
                )
            )

    return grey_image


def main():
    path = "animal.jpeg"
    image = load_image(path)

    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    main()
