from give_bmi import give_bmi, apply_limit


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    try:
        main()
    except TypeError as e:
        print(f"An TypeError occurred: {e}")
    except ValueError as e:
        print(f"An ValueError occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
