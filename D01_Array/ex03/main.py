from load_image import load_image
from zoom import zoom
from PIL import Image
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
    image, array_image = load_image(path)
    print(f"The shape of the image is: {image.shape}")
    print(array_image)

    image_zoom = zoom(400, 400, array_image)
    new_image = Image.fromarray(image_zoom)
    new_image = np.array(new_image)
    gray_image = to_gray(new_image)
    print(f"New shape after slicing: {gray_image.shape}")
    print(gray_image)
    plt.imshow(gray_image, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
