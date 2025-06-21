import argparse #biblioteka do obslugi z argumentow z lini komend
from utils.graph_io import load_graph #funkcja wczytania grafu z pliku
from utils.solution_utils import cost # import funkcji obliczeniowej kolorowa
from algorithms import brute_force #algorytm zaimportowany
def main():
    parser = argparse.ArgumentParser() #argumenty do odczytaia z terminala
    parser.add_argument("--file", help="Ścieżka do pliku z grafem (lub '-' dla stdin)", required=True)
    parser.add_argument("--colors", help="Liczba kolorów", type=int, required=True)
    parser.add_argument("--method", help="Metoda: brute, hill, tabu", required=True)
    parser.add_argument("--tabu_size", type=int, help="Rozmiar listy tabu (tylko dla metody 'tabu')", default=None)

    args = parser.parse_args()
    graph = load_graph(args.file if args.file != '-' else 0)

    if args.method == "brute":
        solution, c = brute_force.brute_force(graph, args.colors)

    elif args.method == "hill":
        from algorithms.hill_climbing import hill_climbing
        solution, c = hill_climbing(graph, args.colors)

    elif args.method == "tabu":
        from algorithms.tabu_search import tabu_search
        solution, c = tabu_search(graph, args.colors, tabu_size=args.tabu_size)

    else:
        print("Nieznana metoda.")
        return

    print("Rozwiązanie:", solution)
    print("Koszt:", c)

if __name__ == "__main__":
    main()
