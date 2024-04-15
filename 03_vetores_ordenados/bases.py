from __future__ import annotations
import numpy as np


class OrdenedVector:
    def __init__(self, size: int, uniques: bool = False) -> None:
        """Esta classe representa um vetor ordenado de tamanho prefixado.

        Este vetor aceita apenas numeros.
        """
        self.size: int = size
        self.last_pos: int = -1
        self.values: np.array = np.empty(self.size, dtype=int)
        self.uniques: bool = uniques

    def __len__(self):
        return self.last_pos + 1

    def __getitem__(self, item):
        return self.values[item]

    def show_values(self) -> str:
        """Este método retorna a representação dos valores dentro do vetor

        Retorna apenas posições com dados. Posições vazias serão ignoradas.
        """
        if self.last_pos == -1:
            return "O Vetor está vazio"
        else:
            temp = []
            for i in range(self.last_pos + 1):
                 temp.append(f"[POS {i}]: {self.values[i]}\n")

            return "".join(temp)

    def insert(self, value) -> OrdenedVector:
        """Realiza o insert de forma ordeada
        """
        if self.last_pos < self.size:
            self.last_pos += 1
            pos = 0
            for i in range(self.last_pos + 1):
                pos = i
                if self.values[i] == value and self.uniques:
                    print(f"O valor {value} ja existe no vetor")
                    self.last_pos -= 1
                    return self
                if self.values[i] > value: break
            self.values[pos+1 : self.last_pos+1] = self.values[pos : self.last_pos]
            self.values[pos] = value
        else:
            raise IndexError("O limite do vetor foi aringido")
        return self

    def linear_search(self, value: int) -> int:
        """A pesquisa linear em um vetor ordenado tem vantagem pois pode avaliar o valor
        da posição para determinar se o vetor contém o valor procurado.
        """
        for i in range(self.last_pos +1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i


    def exclude(self, value: int) -> OrdenedVector:
        """A exclusão segue o padrão de anterior, mas aqui optei por utilizar uma forma mais pythonic
        """
        position = self.linear_search(value)
        if position == -1:
            return self
        self.values[position : self.last_pos] = self.values[position+1 : self.last_pos+1]
        self.last_pos -= 1
        return self

    def binary_search(self, value: int, l_down: int = None, l_up: int = None) -> int:
        """Método de procura que agiliza a procura no vetor ordenado.
        """
        l_down = l_down if l_down else 0
        l_up = l_up if l_up else self.last_pos

        actual_pos = int((l_up + l_down) / 2)

        if value == self.values[actual_pos]:
            return actual_pos

        if l_down >= l_up:
            return -1

        if value > self.values[actual_pos]:
            return self.binary_search(value, l_down=actual_pos+1, l_up=l_up)
        elif value < self.values[actual_pos]:
            return self.binary_search(value, l_down=l_down, l_up=actual_pos-1)
        else:
            return -1

if __name__ == '__main__':
    v = OrdenedVector(10)

    # Teste de inserção
    v.insert(4) \
        .insert(13) \
        .insert(1) \
        .insert(4) \
        .insert(3) \
        .insert(4) \
        .insert(23) \
        .insert(2) \
        .insert(100)
    print(v.show_values())


    v = OrdenedVector(10, uniques=True)

    # Teste de inserção
    v.insert(4) \
        .insert(13) \
        .insert(1) \
        .insert(4) \
        .insert(3) \
        .insert(4) \
        .insert(23) \
        .insert(2) \
        .insert(100)
    print(v.show_values())

    print(v.linear_search(4))
    print(v.linear_search(22))


    v.exclude(4)
    print(v.show_values())

    print(v.binary_search(23))
    print(v.binary_search(4))
    print(v.binary_search(3))
    print(v.binary_search(13))
    print(v.binary_search(100))
    print(v.binary_search(22))