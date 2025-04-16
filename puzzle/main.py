from no import No
from graph import Grafo

def main():
    estado_inicial = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    estado_final = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    no_inicial = No(estado_inicial)
    grafo = Grafo(no_inicial)
    ultimo_estado = grafo.generate_graph(estado_final)
    # print(ultimo_estado)
    # if ultimo_estado:
    #     grafo.refazer_caminho(ultimo_estado)
    # else:
    #     print("Estado final não encontrado no grafo.")

if __name__ == "__main__":
    main()
