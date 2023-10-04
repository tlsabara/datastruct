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
                    self.last_pos -= 1
                    return self
                if self.values[i] > value: break
            self.values[pos+1 : self.last_pos+1] = self.values[pos : self.last_pos]
            self.values[pos] = value
        else:
            raise IndexError("O limite do vetor foi aringido")
        return self

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

    3
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
