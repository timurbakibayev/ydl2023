from dataframe import DataFrame
from array import Array

"""
Model
receives: X, y
X - any number of columns
y - one column

Find coefficients a0, a1, ... only -1, 0, 1, s.t.:
a0 * x0 + a1 * x1 + ... + an * xn = y
"""


class PlusMinus:
    ...
    def fit(self, X: DataFrame, y: Array):
        ...

    def predict(self, X: DataFrame) -> Array:
        ...

    def score(self, X: DataFrame, y: Array) -> float:
        ...


