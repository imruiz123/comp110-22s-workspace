"""__author__: 730335383."""


my_dictionary: dict[str, str] = dict()
my_dictionary2: dict[str, str] = dict()


def invert(my_dictionary: dict[str, str]) -> dict[str, str]: 
    result1: dict[str, str] = dict()
    value: str = ""
    for key in my_dictionary: 
        value = my_dictionary[key]  
        result1[value] = key 
    return result1 


def favorite_color(my_dictionary2: dict[str, str]) -> str: 
    fav_color: dict[str, int] = dict()
    color: str = ""
    value: int = 0
    popular_color: str = ""

    for person in my_dictionary2:
        color = my_dictionary2[person]
        if color not in fav_color.keys():
            fav_color[color] = 1
        else:
            fav_color[color] = fav_color[color] + 1

    for dict_color in fav_color:
        print(fav_color[dict_color])
        if fav_color[dict_color] > value:
            value = fav_color[dict_color]
            popular_color = dict_color

    return popular_color


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Itzel": "yellow"}))


def count(count_list: list[str]) -> dict[str, int]:
    count_dictionary: dict[str, int] = dict()
    for item in count_list:
        if item in count_dictionary.keys():
            count_dictionary[item] = count_dictionary[item] + 1
        else:
            count_dictionary[item] = 1
    return count_dictionary


print(count(["apple", "orange", "strawberry", "grape", "apple", "apple", "orange", "lemon"]))
