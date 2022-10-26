"""This is exercise seven - EX07 - Dictionary Functions!"""

__author__ = "730573834"


def invert(dict_one: dict[str, str]) -> dict[str, str]:
    """This function takes a dictionary and outputs a dictionary that switches/inverts the places of the keys and the values."""
    inv_dict_one: dict[str, str] = {}
    inv_dict_one = dict((dict_one[keys], keys) for keys in dict_one)

    if (len(inv_dict_one) != len(dict_one)):
        raise KeyError

    return inv_dict_one


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """This function takes in a dictionary and outputs a string with the value that was most frequently assigned to values in the dictionary inputted."""
    color_counts: dict[str, int] = {}

    if names_and_colors == {}:
        return ""
    else:
        for color in names_and_colors.values():
            if (color in color_counts):
                color_counts[color] += 1
            else:
                color_counts[color] = 1 
    values = list(color_counts.values())
    keys = list(color_counts.keys())
    return keys[values.index(max(values))]


def count(numbers: list[str]) -> dict[str, int]:
    """This function takes in a list of strings and outputs a dictionary with the items in the list as the keys in the dictionary and the values in the dictionary are the frequencies of the items from the list."""
    counting_list: dict[str, int] = {}
    
    for num in numbers:
        if (num in counting_list):
            counting_list[num] += 1
        else:
            counting_list[num] = 1
        
    return counting_list 
