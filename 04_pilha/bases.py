from __future__ import annotations
import numpy as np


class Stacks:
    def __init__(self, size: int) -> None:
        """Esta classe representa a estrutura de uma pilha de tamanho predefinido.

        :param size:
        """
        self.__size: int = size
        self.__top_pos: int = -1
        self.__values: np.array = np.empty(self.__size, dtype=str)

    def __its_full(self) -> bool:
        """Avalia se a pilha esta cheia

        Esta função não deve estar acessível para classes externas
        """
        if self.__top_pos == self.__size -1:
            return True
        return False

    def is_empty(self) -> bool:
        """Avalia se a pilha esta vazia

        Esta função não deve estar acessível para classes externas
        """
        if self.__top_pos == -1:
            return True
        return False

    def __getitem__(self, item):
        raise IndexError("Elements cannot be accessed")

    def stack_up(self, value: float|int) -> None:
        """Insere um elemento no topo da pilha
        """
        if not self.__its_full():
            self.__top_pos += 1
            self.__values[self.__top_pos] = value
        else:
            raise IndexError("Stack is full")

    def unstack(self):
        """Retira um elemento do topo da pilha
        """
        if not self.is_empty():
            self.__values[self.__top_pos] = np.nan
            self.__top_pos -= 1
        else:
            raise IndexError("Stack is empty")

    def lookup_top(self) -> float:
        """Retorna o elemento do topo da pilha
        """
        if not self.is_empty():
            return self.__values[self.__top_pos]
        else:
            raise IndexError("Stack is empty")

if __name__ == "__main__":
    pilha = Stacks(10)

    pilha.stack_up(10)
    pilha.stack_up(20)
    pilha.stack_up(30)
    pilha.stack_up(40)
    pilha.stack_up(50)
    pilha.stack_up(60)
    pilha.stack_up(70)
    pilha.stack_up(80)
    pilha.stack_up(90)
    pilha.stack_up(100)


    print(pilha.lookup_top())

    for i in range(5):
        pilha.unstack()
        print(pilha.lookup_top())

    print(pilha.lookup_top())