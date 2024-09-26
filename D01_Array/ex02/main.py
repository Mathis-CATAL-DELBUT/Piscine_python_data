from load_image import ft_load


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"An ValueError occurred: {e}")
    except TypeError as e:
        print(f"An TypeError occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
