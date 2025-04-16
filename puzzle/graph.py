from typing import List
from no import No
import copy

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

          
    def generate_one_depth_graph(self):
        self.raiz.expandir_no()
        for child in self.raiz.filhos:
            self.nos.append(child)
        return     

    def generate_graph(self, estado_final: No) -> No:
        visitados = set()
        fila = [self.raiz]

        while fila:
            no_atual = fila.pop(0)

            if no_atual == estado_final:
                print(f"ultimo no{no_atual}")
                return no_atual

            if no_atual in visitados:
                continue

            visitados.add(no_atual)

            # print(f"\n=========FATHER=========\n")
            # print(no_atual)
            # print(f"\n=========END_FATHER=========\n")

            filhos = no_atual.expandir_no()

            # for f in filhos:
            #     print(f)
            
            for filho in filhos:
                if filho not in visitados:
                    self.nos.append(filho)
                    fila.append(filho)

        return None

    def refazer_caminho(self, ultimo_estado: No):
        caminho: List[No] = []

        # Reconstroi o caminho do final até a raiz
        while ultimo_estado is not None:
            caminho.append(ultimo_estado)
            ultimo_estado = ultimo_estado.pai

        # Inverte o caminho para ir da raiz até o final
        for node in reversed(caminho):
            print(f"Ação: {node.acao_realizada}")
            print(node)
            print("-" * 40)        

    # def refazer_caminho(ultimo_estado: No):
    #     caminho : List[No] = []
    #     caminho.append(ultimo_estado)

    #     while ultimo_estado.pai != None:
    #         caminho.append(copy(ultimo_estado.pai))
    #         ultimo_estado = ultimo_estado.pai

    #     for node in reverse(caminho):
    #         print(node)

       