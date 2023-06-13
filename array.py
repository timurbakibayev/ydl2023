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

    def at(self, index: int):
        return self._values[index]

    def __getitem__(self, item):
        return self._values[item]

    def slice(self, from_index: int, to_index: int):
        return Array(self._values[from_index:to_index])

    def __add__(self, other):
        if isinstance(other, Array):
            assert self.len == other.len
            # return Array([self.at(i) + other.at(i) for i in range(self.len)])
            c = []
            for i in range(self.len):
                c.append(self.at(i) + other.at(i))
            return Array(c)
        elif type(other) in self.ALLOWED_TYPES:
            c = []
            for i in range(self.len):
                c.append(self.at(i) + other)
            return Array(c)
        raise TypeError(f"Cannot add Array and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Array):
            assert self.len == other.len
            # return Array([self.at(i) * other.at(i) for i in range(self.len)])
            c = []
            for i in range(self.len):
                c.append(self.at(i) * other.at(i))
            return Array(c)
        elif type(other) in self.ALLOWED_TYPES:
            c = []
            for i in range(self.len):
                c.append(self.at(i) * other)
            return Array(c)
        raise TypeError(f"Cannot add Array and {type(other)}")

    def __pow__(self, power, modulo=None):
        c = []
        for i in range(self.len):
            c.append(self.at(i) ** power)
        return Array(c)

    def __eq__(self, other):
        return isinstance(other, Array) and self._values == other._values

    def avg(self):
        return sum(self._values) / self.len
