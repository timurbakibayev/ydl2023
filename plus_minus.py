from dataframe import DataFrame
from array import Array
from combinations import generate_combinations
"""
Model
receives: X, y
X - any number of columns
y - one column

Find coefficients a0, a1, ... only -1, 0, 1, s.t.:
a0 * x0 + a1 * x1 + ... + an * xn = y
"""


class PlusMinus:
    def __init__(self):
        self.combination = None

    def fit(self, X: DataFrame, y: Array):
        n = len(X.columns)
        for combination in generate_combinations(n):
            result = Array.zero(y.len)
            for i, col in enumerate(X.columns):
                result += X[col] * combination[i]

            if result == y:
                self.combination = combination
                return
        raise Exception("Could not find a solution")

    def predict(self, X: DataFrame) -> Array:
        if self.combination is None:
            raise Exception("Please call fit first")

        result = Array.zero(X.len())
        for i, col in enumerate(X.columns):
            result += X[col] * self.combination[i]
        return result

    def score(self, X: DataFrame, y: Array) -> float:
        y_pred = self.predict(X)
        return sum((y + (y_pred * -1)) ** 2) / y.len
