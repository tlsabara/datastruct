import pytest
from bases_vectors import UnordenetVector

def test_show_values_shold_return_a_string_always() -> None:
    """Testa se o vetor esta restornando uma string
    """
    vector_size = 5

    instace_empty = UnordenetVector(vector_size)
    instace_valid = UnordenetVector(vector_size)

    instace_valid.values[0] = 11
    instace_valid.last_pos = vector_size - 1

    assert type(instace_empty.show_values()) == str
    assert type(instace_valid.show_values()) == str


def test_insert_a_clear_number_should_not_return_error() -> None:
    """O Vetor deve permitir ao usuário inserir um numero qualquer
    """
    instace = UnordenetVector(3)
    instace.insert(1)
    assert len(instace) == 1

    instace.insert(2)
    assert len(instace) == 2


def test_insert_should_raise_error_on_try_insert_a_not_int() -> None:
    """A classe não deve permitir ser inserido um valor que não seja um inteiro
    """
    instace = UnordenetVector(3)
    with pytest.raises(ValueError) as e:
        instace.insert("Carro")


def test_insert_should_raise_error_on_try_insert_more_than_len_of_size() -> None:
    """A classe não deve permitir inserir numeros além do tamanho do vetor
    """
    instace = UnordenetVector(3)

    instace.insert(1)
    instace.insert(2)
    instace.insert(3)

    with pytest.raises(IndexError) as e:
        instace.insert(4444)

def test_vector_shold_be_indexable() -> None:
    """A classe deve permitir o apontamento do index(como uma lista em python
    """
    instace = UnordenetVector(3)

    instace.insert(10)
    instace.insert(20)
    instace.insert(30)

    assert instace[0] == 10
    assert instace[1] == 20
    assert instace[2] == 30

def test_vector_shold_be_sliceble() -> None:
    """A classe deve comportar-se como uma lista em um slice
    """

    instace = UnordenetVector(3)

    instace.insert(10)
    instace.insert(20)
    instace.insert(30)

    assert len(instace[0:2]) == 2
    assert len(instace[1:]) == 2
    assert len(instace[:-2]) == 1

def test_vector_shold_be_exclude_a_value() -> None:
    """A classe deve permitir a remoção de um item, sem deixar posições vazlias"""

    instace = UnordenetVector(7)

    instace.insert(10)
    instace.insert(20)
    instace.insert(30)
    instace.insert(40)
    instace.insert(50)

    instace.exclude(20)

    assert len(instace) == 4
    assert instace[1] == 30

