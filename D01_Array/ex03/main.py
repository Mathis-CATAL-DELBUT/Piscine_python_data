from load_image import load_image
from zoom import zoom
from PIL import Image
from matplotlib import pyplot as plt


def main():
    path = "animal.jpeg"
    image, array_image = load_image(path)
    plt.imshow(image)
    plt.show()
    print(f"The shape of the image is: {array_image.shape}")
    print(array_image)
    image_zoom = zoom(10, 500, array_image)
    print(f"New shape after slicing: {image_zoom.shape}")
    new_image = Image.fromarray(image_zoom)
    plt.imshow(new_image)
    plt.show()


if __name__ == "__main__":
    main()
