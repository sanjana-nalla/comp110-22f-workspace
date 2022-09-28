"""EX05 - `list` Utility Functions - Function Skeleton."""

__author__ = "730573834"


def only_evens(list_int: list[int]) -> list[int]:
    """This function iterates through a given list and generates a new list with only even items and returns that new list."""
    i: int = 0
    even_list: list[int] = []

    while (i < len(list_int)):
        if ((list_int[i] % 2) == 0):
            even_list.append(list_int[i])
        i += 1
    
    return even_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """This function adds the items from two lists in a new list and returns the new list."""
    total_list: list[int] = []
    total_list = list_a + list_b

    return total_list


def sub(list_int: list[int], a: int, b: int) -> list[int]:
    """This function iterates through the items in a given list from a designated start and end index into a new list which is then returned."""
    sub_list: list[int] = []
    i: int = a
    
    if (a < 0):
        a = 0
        i = 0
    elif (b > len(list_int)):
        b = len(list_int)
    elif (len(list_int) == 0):
        return []

    while (a <= i <= (b - 1)):
        sub_list.append(list_int[i])
        i += 1

    return sub_list