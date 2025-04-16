from enum import Enum

class Acao(Enum):
    ESQUERDA = 1
    CIMA = 2
    DIREITA = 3
    BAIXO = 4

    def oposta(self) -> 'Acao':
        opostos = {
            Acao.ESQUERDA: Acao.DIREITA,
            Acao.DIREITA: Acao.ESQUERDA,
            Acao.CIMA: Acao.BAIXO,
            Acao.BAIXO: Acao.CIMA
        }
        return opostos[self]

CUSTO_ACAO = {
    Acao.ESQUERDA: 1,
    Acao.CIMA: 1,
    Acao.DIREITA: 1,
    Acao.BAIXO: 1
}