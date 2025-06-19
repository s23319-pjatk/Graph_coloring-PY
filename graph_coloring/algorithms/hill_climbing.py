import random
from utils.solution_utils import cost, get_neighbour, random_solution

def hill_climbing(graph, num_colors, max_iterations=1000):
    current_solution = random_solution(graph, num_colors)
    current_cost = cost(graph, current_solution)

    for _ in range(max_iterations):
        neighbors = [get_neighbour(current_solution, num_colors) for _ in range(100)]
        best_neighbor = min(neighbors, key=lambda sol: cost(graph, sol))
        best_cost = cost(graph, best_neighbor)

        if best_cost < current_cost:
            current_solution = best_neighbor
            current_cost = best_cost
        else:
            break

    return current_solution, current_cost
