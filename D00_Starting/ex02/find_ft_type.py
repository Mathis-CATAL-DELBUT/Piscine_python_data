ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

def all_thing_is_obj(object: any) -> int:
    type_obj = type(object)
    if type_obj == list:
        print(f"List : {type_obj}")
    elif type_obj == tuple:
        print(f"Tuple : {type_obj}")
    elif type_obj == set:
        print(f"Set : {type_obj}")
    elif type_obj == dict:
        print(f"Dict : {type_obj}")
    elif type_obj == str:
        print(f"{object} is in the kitchen : {type_obj}")
    else:
        print("Type not found")
    return 42


all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))