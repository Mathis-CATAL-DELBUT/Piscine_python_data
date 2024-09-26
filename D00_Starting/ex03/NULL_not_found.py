def NULL_not_found(value=-1):
    if value == -1:
        return 1
    type_value = type(value)
    if value is None:
        print(f"Nothing: {value} {type_value}")
        return 0
    elif isinstance(value, float) and value != value:
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
