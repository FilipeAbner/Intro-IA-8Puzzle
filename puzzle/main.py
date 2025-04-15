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
    grafo.expandir_no(no_inicial)

    print("Filhos do nó inicial:")
    for filho in no_inicial.filhos:
        print(filho)
        print("-" * 30)

if __name__ == "__main__":
    main()
