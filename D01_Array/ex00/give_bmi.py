def give_bmi(height: list[int | float], weight: list[int | float]):
    lenght = len(height)
    if len(height) > len(weight):
        lenght = len(weight)
    return [weight[i] / height[i] ** 2 for i in range(lenght)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [True if i > limit else False for i in bmi]
