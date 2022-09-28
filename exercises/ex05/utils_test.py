"""EX05 - `list` Utility Function - Function Test."""

__author__ = "730573834"

from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Unit test for empty list."""
    list_int: list[int] = []
    assert only_evens(list_int) == []


def test_only_evens_single_odd() -> None:
    """Unit test for odd number."""
    list_int: list[int] = [9]
    assert only_evens(list_int) == []


def test_only_evens_single_even() -> None:
    """Unit test for even number."""
    list_int: list[int] = [8]
    assert only_evens(list_int) == [8]


def test_only_evens_many() -> None:
    """Unit test for multiple even numbers in a large list."""
    list_int: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert only_evens(list_int) == [0, 2, 4, 6, 8]


def test_concat_both_empty() -> None:
    """Unit test for combining two empty lists."""
    list_a: list[int] = []
    list_b: list[int] = []
    assert concat(list_a, list_b) == []


def test_concat_a_empty() -> None:
    """Unit test for combining one empty list with one list with items."""
    list_a: list[int] = []
    list_b: list[int] = [1, 2, 3]
    assert concat(list_a, list_b) == [1, 2, 3]


def test_concat_b_empty() -> None:
    """Unit test for combining one list with items with a second empty list."""
    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = []
    assert concat(list_a, list_b) == [1, 2, 3]


def test_concat_working() -> None:
    """Unit test for combine two lists with items."""
    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = [4, 5, 6]
    assert concat(list_a, list_b) == [1, 2, 3, 4, 5, 6]


def test_sub_empty() -> None:
    """Unit test for empty list."""
    list_int: list[int] = []
    a: int = 1
    b: int = 3
    assert sub(list_int, a, b) == []


def test_sub_negative_start_val() -> None:
    """Unit test for negative start integer."""
    list_int: list[int] = [0, 1, 2, 3, 4, 5, 6]
    a: int = -1
    b: int = 3
    assert sub(list_int, a, b) == [0, 1, 2]


def test_sub_negative_end_val() -> None:
    """Unit test for negative end integer."""
    list_int: list[int] = [0, 1, 2, 3, 4, 5, 6]
    a: int = -3 
    b: int = -1
    assert sub(list_int, a, b) == []


def test_sub_many() -> None:
    """Unit test for working inputs result in proper output."""
    list_int: list[int] = [0, 1, 2, 3, 4, 5, 6]
    a: int = 1
    b: int = 3
    assert sub(list_int, a, b) == [1, 2]