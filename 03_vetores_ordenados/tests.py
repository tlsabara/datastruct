import pytest
from bases import OrdenedVector
import numpy as np


DEFINED_VALUES = [4, 13, 1, 4, 3, 4, 23, 2, 100, 33]
def _insert_values(vector: OrdenedVector):
    for i in DEFINED_VALUES:
        vector.insert(i)
    return vector

@pytest.fixture
def ordered_vector_without_uniques():
    return _insert_values(OrdenedVector(10))


@pytest.fixture
def ordered_vector_with_uniques():
    return _insert_values(OrdenedVector(10, uniques=True))


def test_vectors_shold_be_limited():
    limited_vector = OrdenedVector(5)

    limited_vector.insert(1)
    limited_vector.insert(2)
    limited_vector.insert(3)
    limited_vector.insert(4)
    limited_vector.insert(5)

    with pytest.raises(IndexError) as e:
        limited_vector.insert(6)

def test_insert_without_uniques(ordered_vector_without_uniques):
    arr = np.array(DEFINED_VALUES)
    assert ordered_vector_without_uniques.values.all() == arr.all()


def test_insert_with_uniques(ordered_vector_with_uniques):
    arr = np.array(list(set(DEFINED_VALUES)))
    assert ordered_vector_with_uniques.values.all() == arr.all()

def test_linear_search(ordered_vector_without_uniques):
    assert ordered_vector_without_uniques.linear_search(1) == 0
    assert ordered_vector_without_uniques.linear_search(100) == 9

def test_binary_search(ordered_vector_without_uniques): # COM ERRO
    assert ordered_vector_without_uniques.binary_search(1) == 0
    assert ordered_vector_without_uniques.binary_search(100) == 9