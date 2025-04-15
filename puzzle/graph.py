from typing import List
from no import No

class Grafo:
    def __init__(self, raiz: No):
        self.raiz = raiz
        # Lista de nós do grafo, iniciando pela raiz e logo após, os filhos
        self.nos: List[No] = [raiz]

    # Expande o nó gerando seus filhos
    def expandir_no(self, no: No):
        for a in no.acoes_possiveis:
            # Cria o filho de acordo com as ações possíveis
            filho = no.mover(a)
            filho.acao_realizada = a
            if filho:
                no.filhos.append(filho)
                self.nos.append(filho)
