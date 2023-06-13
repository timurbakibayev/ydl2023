from array import Array
from typing import Dict


class DataFrame:
    """
    Table of data with named columns
    """
    def __init__(self, from_dict: Dict[str, Array]):
        self._from_dict = from_dict
        self._columns = list(from_dict.keys())
        for k, v in from_dict.items():
            assert isinstance(k, str)
            assert isinstance(v, Array)
            assert v.len == from_dict[self._columns[0]].len

    def get(self, column: str) -> Array:
        return self._from_dict[column]

    def set(self, column: str, value: Array):
        assert isinstance(column, str)
        assert isinstance(value, Array)
        assert value.len == self._from_dict[self._columns[0]].len
        self._from_dict[column] = value
        if column not in self._columns:
            self._columns.append(column)

    def __getitem__(self, item):
        if item in self._columns:
            return self.get(item)
        raise AttributeError(f"Attribute {item} not found")

    def __setitem__(self, key, value):
        self.set(key, value)

    @property
    def columns(self) -> list[str]:
        """
        Returns the list of column names (Getter)
        :return:
        """
        return self._columns

    def len(self):
        return self._from_dict[self._columns[0]].len
