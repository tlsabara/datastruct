import numpy as np

class Stacks:
    def __init__(self, size: int) -> None:
        """Esta classe representa a estrutura de uma pilha de tamanho predefinido.

        :param size:
        """
        self.size: int = size
        self.top_pos: int = -1
        self.values: np.array = np.empty(self.size, dtype=int)

    def __is_full(self) -> bool:
        """Avalia se a pilha esta cheia

        Esta função não deve estar acessível para classes externas
        """
        if self.top_pos == self.size -1:
            return True
        return False

