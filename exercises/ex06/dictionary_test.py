"""__author__: 730335383."""


import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_KeyError():
    try:
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)  
    except KeyError:
        print("duplicate")
        pytest.raises(KeyError)


def test_invert_case0():
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_case1():
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Itzel": "yellow"}) == "yellow"


def test_count_case2():
    assert count(["apple", "orange", "strawberry", "grape", "apple", "apple", "orange", "lemon"]) == {"apple": 3, "orange": 2, "strawberry": 1, "grape": 1, "lemon": 1} 