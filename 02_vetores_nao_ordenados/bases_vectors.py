import numpy as np

class UnordenetVector:
    def __init__(self, size: int) -> None:
        """Esta classe representa um vetor não ordenado de tamanho prefixado.

        Este vetor aceita apenas numeros.
        """
        self.size = size
        self.last_pos = -1
        self.values = np.empty(self.size, dtype=int)

    def __len__(self):
        return self.last_pos + 1

    def __getitem__(self, item):
        return self.values[item]

    def show_values(self):
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

    def insert(self, add_value: int) -> None:
        """Método para inserir um valor dentro do vetor
        """
        if self.last_pos < self.size:
            self.last_pos += 1
            self.values[self.last_pos] = add_value
        else:
            raise IndexError("O limite do vetor foi atingido.")

    def linear_search(self, value) -> int:
        """Realiza a varredura do vetor em busca do valor passado.

        Retona a posição do item, ou -1 para valores não localizados
        """
        for i in range(self.last_pos +1):
            if value == self[i]:
                return i
        return -1

    def exclude(self, value) -> int:
        """Função para remover um item do vetor, caso não seja localizado o item, retorna -1
        """
        if position := self.linear_search(value) == -1:
            return position
        else:
            for i in range(position, self.last_pos):
                self.values[i] = self.values[i + 1]
            self.last_pos -= 1
            return self.last_pos
