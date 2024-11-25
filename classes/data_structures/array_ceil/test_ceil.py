import pytest
from array_ceil import get_ceil

def test_empty_array():
    arr = []
    assert get_ceil(arr,2) == None


def test_uniform_array_and_parameter():
    arr = [2 for i in range(5)]
    assert get_ceil(arr,2) == 2

def test_uniform_array_and_smaller_parameter():
    arr = [2 for i in range(5)]
    assert get_ceil(arr, 1) == 2

def test_uniform_array_and_bigger_parameter():
    arr = [2 for i in range(5)]
    assert get_ceil(arr, 3) == None


def test_even_regular_array_and_regular_parameter():
    arr = [1, 2, 4, 6, 6, 8]
    assert get_ceil(arr, 3) == 4

def test_even_regular_array_and_smaller_parameter():
    arr = [1, 2, 4, 6, 6, 8]
    assert get_ceil(arr, 0) == 1

def test_even_regular_array_and_bigger_parameter():
    arr = [1, 2, 4, 6, 6, 8]
    assert get_ceil(arr, 9) == None


def test_odd_regular_array_and_regular_parameter():
    arr = [1, 4, 6, 6, 6, 8, 10]
    assert get_ceil(arr, 5) == 6

def test_odd_regular_array_and_smaller_parameter():
    arr = [1, 4, 6, 6, 6, 8, 10]
    assert get_ceil(arr, 0) == 1

def test_odd_regular_array_and_bigger_parameter():
    arr = [1, 4, 6, 6, 6, 8, 10]
    assert get_ceil(arr, 11) == None
