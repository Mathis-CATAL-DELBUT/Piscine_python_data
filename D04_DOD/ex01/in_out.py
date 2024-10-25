def square(x: int | float) -> int | float:
    return x**2


def pow(x: int | float) -> int | float:
    return x**x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        try:
            nonlocal count
            res = x
            count += 1
            for _ in range(count):
                res = function(res)
            return res
        except Exception:
            print("ERROR")

    return inner
