from dataframe import DataFrame
from array import Array
from plus_minus import PlusMinus
import pytest


def test_simple_line():
    """
    guess: a = 7
    :return:
    """
    a = Array([1, 2, 3, 4, 5])  # +
    b = Array([2, 3, 4, 5, 6])  # -
    c = Array([1, 1, 1, 1, 1])  # -
    y = Array([-2, -2, -2, -2, -2])
    pm = PlusMinus()
    df = DataFrame({"a": a, "b": b, "c": c})
    pm.fit(df, y)
    assert pm.score(df, y) == 0
    assert pm.predict(df) == y
