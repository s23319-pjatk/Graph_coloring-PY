import argparse
from utils.graph_io import load_graph
from utils.solution_utils import cost
from algorithms import brute_force

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Ścieżka do pliku z grafem (lub '-' dla stdin)", required=True)
    parser.add_argument("--colors", help="Liczba kolorów", type=int, required=True)
    parser.add_argument("--method", help="Metoda: brute, hill", required=True)
    parser.add_argument("--tabu_size", type=int, help="Rozmiar listy tabu (opcjonalnie)", default=None)


    args = parser.parse_args()
    graph = load_graph(args.file if args.file != '-' else 0)

    if args.method == "brute":
        solution, c = brute_force.brute_force(graph, args.colors)

    elif args.method == "hill":
        from algorithms.hill_climbing import hill_climbing
        solution, c = hill_climbing(graph, args.colors)

    elif args.method == "tabu":
        from algorithms.tabu_search import tabu_search
        solution, c = tabu_search(
            graph,
            args.colors,
            tabu_size=args  # jesli None Można dodać --tabu_size później
        )
    else:
        print("Nieznana metoda.")
        return

    print("Rozwiązanie:", solution)
    print("Koszt:", c)

if __name__ == "__main__":
    main()
