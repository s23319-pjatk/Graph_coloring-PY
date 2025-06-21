import random
from utils.solution_utils import cost, get_neighbour, random_solution

def tabu_search(graph, num_colors, tabu_size=None, max_iterations=1000):
    current_solution = random_solution(graph, num_colors)  # wygeneruj losowe
    best_solution = current_solution
    best_cost = cost(graph, best_solution)
    tabu_list = []                                      #lista tabu przechowuje poprzednie rozwiazania

    for _ in range(max_iterations):
        neighbors = [get_neighbour(current_solution, num_colors) for _ in range(100)]   #rozwazamy 100 losowych sasiadow
        neighbors = [(n, cost(graph, n)) for n in neighbors]
        neighbors.sort(key=lambda x: x[1])  # sortuj po koszcie

        next_solution = None
        for sol, sol_cost in neighbors:
            if sol not in tabu_list or sol_cost < best_cost:
                next_solution = sol
                break

        if next_solution is None:
            break  # nie ma lepszych opcji

        current_solution = next_solution
        current_cost = cost(graph, current_solution)

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        tabu_list.append(current_solution)
        if tabu_size is not None and len(tabu_list) > tabu_size:
            tabu_list.pop(0)                                     #utrzymujemy rozmiar listy tabu

    return best_solution, best_cost     #zwracamy najlepsze rozwiazanie
