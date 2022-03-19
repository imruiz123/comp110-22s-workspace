""" __author__: 730335383."""


from utils import only_evens
from utils import sub
from utils import concat 


def test_only_evens():
    assert only_evens([1, 2, 3]) == [2]


def test_sub():
    assert sub([10, 20, 30, 40], 1, 3) == [20,30]


def test_concat():
    assert concat([1, 2, 3], [4, 5, 6])


concat
sub
only_evens
