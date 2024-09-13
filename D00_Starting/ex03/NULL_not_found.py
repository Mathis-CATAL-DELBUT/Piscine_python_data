import math

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False


def NULL_not_found(value):
    type_value = type(value)
    # print(value)
    if value is None:
        print(f"Nothing: {value} {type_value}")
        return 0
    elif isinstance(value, float) and math.isnan(value):
        print(f"Cheese: {value} {type_value}")
        return 0
    elif value is False:
        print(f"Fake: {value} {type_value}")
        return 0
    elif value == 0:
        print(f"Zero: {value} {type_value}")
        return 0
    elif value == "":
        print(f"Empty: {type_value}")
        return 0
    else:
        print("Type not found")
    return 1


NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
