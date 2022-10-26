"""This is the unit file for EX07."""

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None: 
    """Unit test for empty dictionary."""
    dict_one: dict[str, str] = {}
    assert invert(dict_one) == {}


def test_invert_many() -> None: 
    """Unit test for full dictionary with many keys and values."""
    dict_one: dict[str, str] = {"abc": "123", "def": "456", "xyz": "789"}
    assert invert(dict_one) == {"123": "abc", "456": "def", "789": "xyz"}


def test_invert_one() -> None: 
    """Unit test for dictionary with a key and value."""
    dict_one: dict[str, str] = {"abc": "123"}
    assert invert(dict_one) == {"123": "abc"}


def test_favorite_color_empty() -> None: 
    """Unit test for empty dictionary."""
    names_and_colors: dict[str, str] = {}
    assert favorite_color(names_and_colors) == ""


def test_favorite_color_many() -> None: 
    """Unit test for dictionary with many keys and values."""
    names_and_colors: dict[str, str] = {"sanjana": "red", "kris": "red", "mom": "blue", "dad": "green", "bro": "yellow", "sis": "black"}
    assert favorite_color(names_and_colors) == 'red'


def test_favorite_color_one() -> None: 
    """Unit test for dictonary with one key and one value."""
    names_and_colors: dict[str, str] = {"sanjana": "red"}
    assert favorite_color(names_and_colors) == 'red'


def test_count_empty() -> None: 
    """Unit test for empty list."""
    numbers: list[str] = []
    assert count(numbers) == {}


def test_count_many() -> None: 
    """Unit test for list with many items."""
    numbers: list[str] = ["x", "x", "x", "y", "z", "z"]
    assert count(numbers) == {"x": 3, "y": 1, "z": 2}


def test_count_one() -> None: 
    """Unit test for list with one item."""
    numbers: list[str] = ["x"]
    assert count(numbers) == {"x": 1}