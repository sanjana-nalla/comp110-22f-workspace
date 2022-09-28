"""This is exercise EX04 - `list` Utility Functions."""

__author__ = "730573834"


def all(nums: list[int], given_num: int) -> bool:
    """This function iterates through the list and inspects the list to see if each value of the list is equal to a given number."""
    i: int = 0
    checker_var: bool = True
    if (len(nums) == 0):
        return False
    while (i < len(nums)):
        if (nums[i] != given_num):
            checker_var = False
            return checker_var
        i += 1
    return checker_var


def max(input: list[int]) -> int:
    """This function compares the values inside the list and returns the maximum number or the highest value in the list while using iteration as well."""
    if (len(input) == 0):
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_val = input[0]
    while (i < len(input)):
        if (input[i] > max_val):
            max_val = input[i]
        i += 1
    return max_val


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """This function comapres to two lists and inspects as each item of the lists to check if they are equal at each index using iteration again."""
    i: int = 0
    while (i < len(str(list_one))):
        if (list_one == list_two):
            return True
        i += 1
    return False