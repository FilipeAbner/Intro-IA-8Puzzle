from enum import Enum
from typing import List, Optional
import copy

class Acao(Enum):
    ESQUERDA = 1
    CIMA = 2
    DIREITA = 3
    BAIXO = 4

# Custos hipotéticos associados às ações
CUSTO_ACAO = {
    Acao.ESQUERDA: 1,
    Acao.CIMA: 1,
    Acao.DIREITA: 1,
    Acao.BAIXO: 1
}

class No:
    def __init__(self, state: List[List[int]], custo: int = 0):
        self.state = copy.deepcopy(state)
        self.acao = self.movimentos_possiveis()
        self.custo = custo
        self.prox: Optional[No] = None

    def __str__(self):
        return f"Ação: {self.acao}, Custo: {self.custo}, Estado:\n" + \
               "\n".join(str(linha) for linha in self.state)

    def movimentos_possiveis(self) -> List[Acao]:
        # Localiza o 0 (espaço vazio)
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    x, y = i, j
                    break

        acoes = []
        if x > 0:
            acoes.append(Acao.CIMA)
        if x < 2:
            acoes.append(Acao.BAIXO)
        if y > 0:
            acoes.append(Acao.ESQUERDA)
        if y < 2:
            acoes.append(Acao.DIREITA)

        return acoes

def mover(state: List[List[int]], acao: Acao) -> Optional[List[List[int]]]:
    # Encontra a posição do 0 (espaço vazio)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    # Define o novo valor de x, y com base na ação
    novo_x, novo_y = x, y
    if acao == Acao.CIMA:
        novo_x -= 1
    elif acao == Acao.BAIXO:
        novo_x += 1
    elif acao == Acao.ESQUERDA:
        novo_y -= 1
    elif acao == Acao.DIREITA:
        novo_y += 1

    # Verifica se a nova posição está dentro dos limites do tabuleiro
    if 0 <= novo_x < 3 and 0 <= novo_y < 3:
        novo_estado = copy.deepcopy(state)
        # Troca o 0 com o valor na nova posição
        novo_estado[x][y], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], novo_estado[x][y]
        return novo_estado
    else:
        return None  # Movimento inválido




# Estado inicial do puzzle
estado_inicial = [
    [1, 2, 3],
    [4, 0, 6],  # 0 representa o espaço vazio
    [7, 5, 8]
]


list_nos = No(estado_inicial,CUSTO_ACAO)

estado_final = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 representa o espaço vazio
]

if __name__ == "__main__":
    print(list_nos)
    # # Testando os movimentos
    # for acao in list_nos.acao:
    #     novo_estado = mover(list_nos.state, acao)
    #     if novo_estado:
    #         no_novo = No(novo_estado, acao, CUSTO_ACAO[acao])
    #         print(f"\nMovendo {acao.name}:")
    #         print(no_novo)
    #     else:
    #         print(f"\nMovimento {acao.name} inválido.")