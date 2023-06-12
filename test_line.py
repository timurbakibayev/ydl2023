from dataframe import DataFrame
from array import Array
from line import Line
import pytest


def test_simple_line():
    """
    guess: a = 7
    :return:
    """
    x = Array([1, 2, 3, 4, 5])
    b = Array([2, 3, 4, 5, 6])
    y = Array([9, 17, 25, 33, 41])
    line = Line()
    df = DataFrame({"x": x, "b": b})
    line.fit(df, y)
    assert line._a == 7
    assert line.predict(df) == y
    assert line.score(df, y) == 0


def test_simple_line1():
    """
    guess: a = 7
    :return:
    """
    x = Array([1, 2, 3, 4, 5])
    b = Array([2, 3, 4, 15, 6])
    y = Array([9, 17, 25, 33, 41])
    line = Line()
    df = DataFrame({"x": x, "b": b})
    with pytest.raises(Exception):
        line.fit(df, y)
