"""EX05 - `list` Utility Functions - Function Skeleton"""

__author__ = "730573834"

def only_evens(list_int: list[int]) -> list[int]:
    i: int = 0
    even_list: list = []

    while i < len(list_int):
        if ((list_int[i] % 2)== 0 ):
            even_list.append(list_int[i])
        i += 1
    
    return even_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    total_list: list = []
    total_list = list_a + list_b

    return total_list


def sub(list_int: list[int], a: int, b: int) -> list[int]:
    sub_list: list = []
    i: int = a + 1
  
    if a < 0:
        i: int = 0
        while (a <= i <= b):
            sub_list.append(i)
            i += 1
    elif b < 1:
        return []
        
    while (a <= i <= b):
        sub_list.append(i)
        i += 1

    return sub_list
