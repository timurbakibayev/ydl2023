from typing import List


class Array:
    ALLOWED_TYPES = [int, float]

    def __init__(self, values: List):
        self._values = values
        if len(values) == 0:
            return
        t = type(values[0])
        if t not in self.ALLOWED_TYPES:
            raise TypeError(f"Unsupported type {t}")
        for v in values:
            if type(v) != t:
                raise TypeError("All values must be of the same type")

    @classmethod
    def zero(cls, length: int):
        return cls([0] * length)

    @property
    def len(self):
        return len(self._values)

    def avg(self):
        return sum(self._values) / self.len

    def __getitem__(self, item):
        return self._values[item]

    def __add__(self, other):
        if isinstance(other, Array):
            assert self.len == other.len
            return Array([self[i] + other[i] for i in range(self.len)])

        elif type(other) in self.ALLOWED_TYPES:
            return Array([self[i] + other for i in range(self.len)])

        raise TypeError(f"Cannot add Array and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Array):
            assert self.len == other.len
            return Array([self[i] * other[i] for i in range(self.len)])

        elif type(other) in self.ALLOWED_TYPES:
            return Array([self[i] * other for i in range(self.len)])

        raise TypeError(f"Cannot multiply Array and {type(other)}")

    def __pow__(self, power, modulo=None):
        return Array([self[i] ** power for i in range(self.len)])

    def __eq__(self, other):
        return isinstance(other, Array) and self._values == other._values
