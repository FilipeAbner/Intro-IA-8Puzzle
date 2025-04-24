from util import Acao, CUSTO_ACAO
from typing import List, Optional
import copy

class No:
    def __init__(self, state: List[List[int]], objetivo: List[List[int]], pai: Optional['No'] = None, custo: int = 1, acao_realizada: Optional[Acao] = None):
        self.state = copy.deepcopy(state)
        self.pai = pai
        self.acoes_possiveis = self.movimentos_possiveis()
        self.objetivo = objetivo
        self.custo = self.distancia_manhattan()
        self.filhos: List[No] = []
        self.acao_realizada = acao_realizada

    def __str__(self):
        return f"Ação Realizada: {self.acao_realizada}\nAções Possíveis: {self.acoes_possiveis}, Custo: {self.custo}, Estado:\n" + \
               "\n".join(str(linha) for linha in self.state)

    def __eq__(self, other):
        if isinstance(other, No):
            return self.state == other.state \
                    # and self.custo == other.custo
        return False

    def __hash__(self):
        # Converte para que seja hashable para uso no set
        return hash(tuple(tuple(linha) for linha in self.state))


    # Calcula os movimentos possíveis a partir do estado atual, se é possível mover o 0 para as laterais
    def movimentos_possiveis(self) -> List[Acao]:
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

    """
    Move o 0 para a direção especificada.
    CIMA: Move o 0 para cima
    BAIXO: Move o 0 para baixo
    ESQUERDA: Move o 0 para a esquerda
    DIREITA: Move o 0 para a direita
    Retorna uma lista de ações possíveis
    """
    def mover(self, acao: Acao) -> Optional['No']:
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    x, y = i, j
                    break

        novo_x, novo_y = x, y
        if acao == Acao.CIMA:
            novo_x -= 1
        elif acao == Acao.BAIXO:
            novo_x += 1
        elif acao == Acao.ESQUERDA:
            novo_y -= 1
        elif acao == Acao.DIREITA:
            novo_y += 1

        # Garante que não será feito um movimento fora dos limites da matriz 3x3
        if 0 <= novo_x < 3 and 0 <= novo_y < 3:
            novo_estado = copy.deepcopy(self.state)
            novo_estado[x][y], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], novo_estado[x][y]
            # novo_custo = CUSTO_ACAO[acao]
            return No(novo_estado, objetivo=self.objetivo, pai=self, acao_realizada=acao)
        else:
            return None

    
    # Expande o nó gerando seus filhos
    def expandir_no(self) -> List['No']:
        child: List[No] = []

        for a in self.acoes_possiveis:
            filho = self.mover(a)
            # print(filho)
            """se o pai tem a acao oposta do filho significa que esta retornando a um estado anterior, por exemplo:
            [1, 2, 3]       [1, 2, 3]
            [4, 6, 0] ->    [4, 0, 6]   
            [7, 5, 8]       [7, 5, 8]
            portanto nao é necessario salvar o filho
                """
            if filho.pai.acao_realizada == filho.acao_realizada.oposta(): 
                continue
            else:
                filho.acao_realizada = a
                child.append(filho)
                self.filhos.append(filho)

        return child
    
    # heuristica a ser usada
    def distancia_manhattan(self) -> int:
        distancia = 0
        for i in range(3):
            for j in range(3):
                valor = self.state[i][j]
                if valor == 0:
                    continue
                for x in range(3):
                    for y in range(3):
                        if self.objetivo[x][y] == valor:
                            distancia += abs(x - i) + abs(y - j)
                            break
        return distancia
    

    def __lt__(self, other):
        return False  # Arbitrário, apenas necessário pro heapq não quebrar , sendo sincero eu não entendi o pq disso