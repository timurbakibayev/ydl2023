from lesson1.lec.dataframe import DataFrame
from lesson1.lec.array import Array


class Line:
    """
    Line Model
    Guess "a" in y = a * x + b

    Example:  y = 2 * x + b
        --------------
        | x | b | y  |
        --------------
        | 1 | 2 | 4  |
        | 2 | 3 | 7  |
        | 3 | 4 | 10 |
        | 4 | 5 | 13 |
        | 5 | 6 | 16 |
        --------------
    """
    def __init__(self):
        self._a = None

    def fit(self, X: DataFrame, y: Array):
        assert "x" in X.columns
        assert "b" in X.columns
        self._a = sum((y + (X['b'] * -1)) * X['x']) / sum(X['x']**2)    # solved with math!

    def predict(self, X: DataFrame) -> Array:
        assert self._a is not None, "Please call fit first"
        return X["x"] * self._a + X["b"]

    def score(self, X: DataFrame, y: Array) -> float:
        assert self._a is not None, "Please call fit first"
        y_pred = self.predict(X)
        return sum((y + (y_pred * -1)) ** 2) / y.len
