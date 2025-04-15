from typing import List
from no import No

class Grafo:
    def __init__(self, raiz: No):
        self.raiz = raiz
        # Lista de nós do grafo, iniciando pela raiz e logo após, os filhos
        self.nos: List[No] = [raiz]

    def __str__(self):
        saida = ["Grafo:"]
        for idx, no in enumerate(self.nos):
            saida.append(f"Nó {idx}:")
            saida.append(str(no))
            saida.append("-" * 30)
        return "\n".join(saida)

    
    # Expande o nó gerando seus filhos
    def expandir_no(self):

        for no in self.nos:
            # print(f"\n=========FATHER=========\n")
            # print(no)
            # print(f"\n=========END_FATHER=========\n")
            for a in no.acoes_possiveis:
                filho = no.mover(a)
                filho.pai = no
                
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
                    no.filhos.append(filho)
                    self.nos.append(filho)
                    # print(filho)
