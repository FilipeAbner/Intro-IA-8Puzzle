from no import No
from graph import Grafo

def main():

    estado_inicial = [
        [1, 2, 6],
        [7, 3, 0],
        [4, 5, 8]
    ]

    estado_final = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    raiz = No(estado_inicial,estado_final)
    grafo = Grafo(raiz)
    ultimo_estado = grafo.generate_graph()

    if ultimo_estado:
        grafo.refazer_caminho(ultimo_estado)
    else:
        print("Estado final não encontrado no grafo.")

if __name__ == "__main__":
    main()
