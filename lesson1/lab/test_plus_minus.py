from lesson1.lec.dataframe import DataFrame
from lesson1.lec.array import Array
from lesson1.lab.plus_minus import PlusMinus


def test_simple_line():
    a = Array([1, 2, 3, 4, 5])  # +
    b = Array([2, 3, 4, 5, 6])  # -
    c = Array([1, 1, 1, 1, 1])  # -
    y = Array([-2, -2, -2, -2, -2])
    pm = PlusMinus()
    df = DataFrame({"a": a, "b": b, "c": c})
    pm.fit(df, y)
    assert pm.score(df, y) == 0
    assert pm.predict(df) == y
    assert pm.combination == [1, -1, -1]
