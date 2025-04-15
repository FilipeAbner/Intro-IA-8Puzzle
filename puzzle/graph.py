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

          
    def generate_graph(self):
        self.raiz.expandir_no()
        for child in self.raiz.filhos:
            self.nos.append(child)
        return      
    