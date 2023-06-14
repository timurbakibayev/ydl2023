from lesson1.lec.array import Array
import pytest


def test_is_instance():
    assert isinstance(Array([1, 2, 3]), Array)


def test_values():
    a = Array([1, 2, 3, 4])
    assert a[0] == 1
    assert a[1] == 2
    assert a[2] == 3
    assert a.len == 4

    s = Array(a[1:3])
    assert isinstance(s, Array)
    assert s[0] == 2
    assert s[1] == 3
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
    assert c[0] == 6
    assert c[1] == 8
    assert c[2] == 10
    assert c[3] == 12
    assert c.len == 4


def test_multiply():
    a = Array([1, 2, 3, 4])
    b = Array([5, 6, 7, 8])
    c = a * b
    assert isinstance(c, Array)
    assert c[0] == 5
    assert c[1] == 12
    assert c[2] == 21
    assert c[3] == 32
    assert c.len == 4


def test_plus_number():
    a = Array([1, 2, 3, 4])
    b = 5
    c = a + b
    assert isinstance(c, Array)
    assert c[0] == 6
    assert c[1] == 7
    assert c[2] == 8
    assert c[3] == 9
    assert c.len == 4

    c = a * b
    assert isinstance(c, Array)
    assert c[0] == 5
    assert c[1] == 10
    assert c[2] == 15
    assert c[3] == 20
    assert c.len == 4


def test_errors():
    with pytest.raises(TypeError):
        Array([1, 2, 3, 4.0])

    with pytest.raises(TypeError):
        Array([1, 2, 3, 4, "aaa"])

    with pytest.raises(TypeError):
        Array(["aaa", "bbb"])

    a = Array([])
    assert a.len == 0
