def ft_mean(*args: any) -> float:
    return sum(args) / len(args)


def ft_median(*args: any) -> float:
    if len(args) == 1:
        return args[0]
    else:
        args = sorted(args)
        n = len(args)
        if n % 2 == 0:
            return (args[n // 2] + args[n // 2 - 1]) / 2
        else:
            return args[n // 2]


def ft_quartile(*args: any) -> tuple:
    if len(args) == 1:
        return (args[0], args[0])
    else:
        args = sorted(args)
        n = len(args)
        q1 = args[n // 4] if n % 4 == 0 else args[n // 4]
        q3 = args[3 * n // 4] if n % 4 == 0 else args[3 * n // 4]
        return (q1, q3)


def ft_std(*args: any) -> float:
    return (sum((x - ft_mean(*args)) ** 2 for x in args) / len(args)) ** 0.5


def ft_var(*args: any) -> float:
    return sum((x - ft_mean(*args)) ** 2 for x in args) / len(args)


def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        stats_to_calculate = set(kwargs.values())

        if "mean" in stats_to_calculate:
            if len(args) < 1:
                print("ERROR")
            else:
                print("mean : ", ft_mean(*args))

        if "median" in stats_to_calculate:
            if len(args) < 1:
                print("ERROR")
            else:
                print("median : ", ft_median(*args))

        if "quartile" in stats_to_calculate:
            if len(args) < 1:
                print("ERROR")
            else:
                q1, q3 = ft_quartile(*args)
                print(f"quartile : [{q1}, {q3}]")

        if "std" in stats_to_calculate:
            if len(args) < 1:
                print("ERROR")
            else:
                print("std : ", ft_std(*args))

        if "var" in stats_to_calculate:
            if len(args) < 1:
                print("ERROR")
            else:
                print("var : ", ft_var(*args))

    except Exception:
        print("ERROR : bad arguments")
