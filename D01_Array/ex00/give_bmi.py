def give_bmi(height: list[int | float], weight: list[int | float]):
    """
    Calculate the BMI of a list of people
    """
    if len(height) < 1 or len(weight) < 1:
        raise ValueError("Empty list")
    if len(height) != len(weight):
        raise ValueError("Lists are not the same size")
    if any([True for i in height if i <= 0]):
        raise ValueError("Values must be greater than 0")
    if any([True for i in weight if i <= 0]):
        raise ValueError("Values must be greater than 0")
    if type(height) is not list or type(weight) is not list:
        raise TypeError("Invalid type")
    return [weight[i] / height[i] ** 2 for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI
    """
    if type(bmi) is not list:
        raise TypeError("Invalid type")
    if len(bmi) < 1:
        raise ValueError("Empty list")
    return [True if i > limit else False for i in bmi]
