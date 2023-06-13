from lesson1.lec.dataframe import DataFrame
from lesson1.lec.array import Array


def test_dataframe_init():
    age = Array([18, 20, 22, 25])
    height = Array([1.72, 1.80, 1.68, 1.90])

    df = DataFrame({"age": age, "height": height})

    assert isinstance(df, DataFrame)
    assert df.columns == ["age", "height"]
    assert df.get("age") == age
    assert df.get("height") == height

    df.set("age_plus_10", df.get("age") + 10)
    assert df.columns == ["age", "height", "age_plus_10"]
    assert df["age_plus_10"] == Array([28, 30, 32, 35])


def test_dataframe_set():
    a = Array([1, 2, 3, 4])
    b = Array([5, 6, 7, 8])
    df = DataFrame({"a": a, "b": b})
    assert df.columns == ["a", "b"]
    df["c"] = df["a"] + df["b"]
    assert df.columns == ["a", "b", "c"]
    assert df.get("c") == Array([6, 8, 10, 12])
