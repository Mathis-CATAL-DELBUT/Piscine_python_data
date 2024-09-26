from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey


def main():
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"An ValueError occurred: {e}")
    except TypeError as e:
        print(f"An TypeError occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
