"""Dictionary related utility functions."""

__author__ = "730573834"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")  # "r" means read
  
    # Prepare to read the data dile as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(inputs: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """This function takes in a integer and dictionary and returns a new dictionary that stored all the columns(keys) with the first N items(values)."""
    output: dict[str, list[str]] = {}

    # initialize a counter var
    i: int = 0
    # access keys of inputs dict
    for column in inputs:
        # create new list
        values: list[str] = []
        i = 0
        # while the counter is less than the given N and less than the length of the values in the each key's value
        while ((i < N) and (i < len(inputs[column]))):
            # add the the items in values list of keys to a new list
            values.append(inputs[column][i])
            # add 1 to the counter variable
            i += 1
        # add new key-value pairs to new dict
        output[column] = values
    # return new dict
    return output
    

def select(selection: dict[str, list[str]], selected: list[str]) -> dict[str, list[str]]:
    """This function takes in a dictionary and list to return a dictionary with only the columns specified in the given list(as keys) and the values it is paired to."""
    # create a new dict
    output: dict[str, list[str]] = {}

    # iterate through the given list's items which serve as the keys in the dict
    for column in selected:
        # iterate through the associated values of the dictionary
        for row in selection[column]:
            # add the key-value pair to the output dict
            output[column] = selection[column]
    # return new dict
    return output


def concat(dict_a: dict[str, list[str]], dict_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function takes in two dictionaries and returns a dictionary that combined them but for duplicate keys, the values of the two are just added together; otherwise, the key-value pairs were added to the new dictionary as is."""
    # create a new dict
    output: dict[str, list[str]] = {}

    # iterate through one dict's keys
    for column in dict_a:
        # add the key-value pairs to the output dict
        output[column] = dict_a[column]
    # iterate through the second dict's keys
    for column in dict_b:
        # if the key already in output dict, then add the key's values to the existing value
        if column in output:
            output[column] += dict_b[column]
        # add the key-value pairs to the output dict
        else:
            output[column] = dict_b[column]
    # return new dict
    return output


def count(inputs: list[str]) -> dict[str, int]:
    """This function takes in a list and returns a dictionary with the strings in the list as the keys and the values as the number times the string appeared in the list."""
    # create a new dict
    output: dict[str, int] = {}

    # iterate through items of the list
    for item in inputs:
        # if item is already in the output, then go into the then block 
        if item in output:
            # add one to the value associated with the key 
            output[item] += 1
        # if item is not already in the output, then go into this then block
        else:
            # assign the value associated with the key 1
            output[item] = 1
    # return new dict
    return output
