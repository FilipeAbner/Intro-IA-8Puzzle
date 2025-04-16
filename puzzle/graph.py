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
    
    # Expande apenas para a proxima geração de filhos de um nó 
    def generate_one_depth_graph(self):
        self.raiz.expandir_no()
        for child in self.raiz.filhos:
            self.nos.append(child)
        return     

    # Expande todas as gerações de filhos de um nó até encontrar um estado igual ao estado final
    def generate_graph(self, estado_final: No) -> No:
        visitados = set()
        fila = [self.raiz]
        count = 0
        while fila:
            no_atual = fila.pop(0)

            if no_atual == estado_final:
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
                self.nos.append(filho)
                if filho == estado_final:
                    return filho
                if filho not in visitados:
                    fila.append(filho)

        return None

    def refazer_caminho(self, ultimo_estado: No):
        caminho: List[No] = []
        total_passos = 0
        # Reconstroi o caminho do final até a raiz
        while ultimo_estado is not None:
            caminho.append(ultimo_estado)
            ultimo_estado = ultimo_estado.pai
            total_passos+=1

        # Inverte o caminho para ir da raiz até o final
        for node in reversed(caminho):
            print(f"Ação: {node.acao_realizada}")
            print(node)
            print("-" * 40)        

        # Imprime o total de passos removendo o estado_inicial
        print(total_passos-1)
       