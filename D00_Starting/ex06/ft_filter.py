def ft_filter(function_to_apply, list_of_inputs):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None return the items that are true.
    """
    if function_to_apply is None:
        return (x for x in list_of_inputs if x)
    return [x for x in list_of_inputs if function_to_apply(x)]


def is_even(x):
    """
    is_even(x) --> bool
    """
    return x % 2 == 0


def is_odd(x):
    """
    is_odd(x) --> bool
    """
    return x % 2 != 0


def main():
    """
    test filter and ft_filter functions
    """
    # print(filter.__doc__)
    # print(ft_filter.__doc__)
    # print(is_even.__doc__)
    # print(is_odd.__doc__)

    f = ft_filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(f))
    f = filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(f))
    f = ft_filter(None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(f))
    f = filter(None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(f))
    f = ft_filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(f))
    f = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(f))


if __name__ == "__main__":
    main()
