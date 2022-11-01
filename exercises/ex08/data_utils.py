"""Dictionary related utility functions."""

__author__ = "730573834"

# Define your functions below
from csv import DictReader
from turtle import fd


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


def column_values(table:list[dict[str,str]], column: str) -> list[str]:
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


def head(inputs:dict[str, list[str]], N:int) -> dict[str, list[str]]:
    """This function takes in a integer and dictionary and returns a new dictionary with ____ ."""
    output: dict[str, list[str]] = {}

    i: int = 0
    for column in inputs:
        values:list[str] = []
        i = 0
        while ((i < N) and (i < len(inputs[column]))):
            values.append(inputs[column][i])
            i += 1
        output[column] = values

    return output
    

def select(selection: dict[str, list[str]], selected: list[str]) -> dict[str, list[str]]:
    """This function __."""
    output: dict[str, list[str]] = {}

    for column in selected:
        for row in selection[column]:
            output[column] = selection[column]

    return output


def concat(dict_a: dict[str, list[str]], dict_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function ___."""
    output: dict[str, list[str]] = {}

    for column in dict_a:
        output[column] = dict_a[column]
    for column in dict_b:
        output[column] = dict_b[column]

    return output


def count(inputs:list[str]) -> dict[str, int]:
    """This function ___."""
    output: dict[str, int] = {}

    return output
