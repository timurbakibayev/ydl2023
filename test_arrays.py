from array import Array
import pytest


def test_is_instance():
    assert isinstance(Array([1, 2, 3]), Array)


def test_values():
    a = Array([1, 2, 3, 4])
    assert a[0] == 1
    assert a.at(1) == 2
    assert a.at(2) == 3
    assert a.len == 4

    s = a.slice(1, 3)
    assert isinstance(s, Array)
    assert s.at(0) == 2
    assert s.at(1) == 3
    assert s.len == 2


def test_add_lists():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    c = a + b
    assert isinstance(c, list)
    assert c == [1, 2, 3, 4, 5, 6, 7, 8]


def test_plus():
    a = Array([1, 2, 3, 4])
    b = Array([5, 6, 7, 8])
    c = a + b
    assert isinstance(c, Array)
    assert c.at(0) == 6
    assert c.at(1) == 8
    assert c.at(2) == 10
    assert c.at(3) == 12
    assert c.len == 4


def test_multiply():
    a = Array([1, 2, 3, 4])
    b = Array([5, 6, 7, 8])
    c = a * b
    assert isinstance(c, Array)
    assert c.at(0) == 5
    assert c.at(1) == 12
    assert c.at(2) == 21
    assert c.at(3) == 32
    assert c.len == 4


def test_plus_number():
    a = Array([1, 2, 3, 4])
    b = 5
    c = a + b
    assert isinstance(c, Array)
    assert c.at(0) == 6
    assert c.at(1) == 7
    assert c.at(2) == 8
    assert c.at(3) == 9
    assert c.len == 4

    c = a * b
    assert isinstance(c, Array)
    assert c.at(0) == 5
    assert c.at(1) == 10
    assert c.at(2) == 15
    assert c.at(3) == 20
    assert c.len == 4


def test_errors():
    with pytest.raises(TypeError):
        a = Array([1, 2, 3, 4.0])

    with pytest.raises(TypeError):
        a = Array([1, 2, 3, 4, "ddd"])

    with pytest.raises(TypeError):
        a = Array(["ddd", "ddds"])

    a = Array([])
    assert a.len == 0
