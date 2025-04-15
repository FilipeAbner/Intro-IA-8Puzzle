from no import No
from graph import Grafo

def main():
    estado_inicial = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    no_inicial = No(estado_inicial)
    grafo = Grafo(no_inicial)
    grafo.generate_graph()
        
    # print(grafo)

if __name__ == "__main__":
    main()
