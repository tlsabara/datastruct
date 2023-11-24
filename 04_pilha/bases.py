from __future__ import annotations
import numpy as np


class Stacks:
    def __init__(self, size: int) -> None:
        """Esta classe representa a estrutura de uma pilha de tamanho predefinido.

        :param size:
        """
        self.__size: int = size
        self.__top_pos: int = -1
        self.__values: np.array = np.empty(self.__size, dtype=float)

    def __is_full(self) -> bool:
        """Avalia se a pilha esta cheia

        Esta função não deve estar acessível para classes externas
        """
        if self.__top_pos == self.__size -1:
            return True
        return False

    def __getitem__(self, item):
        raise IndexError("Elements cannot be accessed")

    def stack_up(self):...

    def unstack(self):...

if __name__ == "__main__":
    pilha = Stacks(10)

    pilha[2]
