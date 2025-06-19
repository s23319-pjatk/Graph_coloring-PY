import random
import copy

def random_solution(graph, max_colors):
    return {node: random.randint(0, max_colors - 1) for node in graph}

def get_neighbour(solution, max_colors):
    new_sol = solution.copy()
    node = random.choice(list(new_sol.keys()))
    current_color = new_sol[node]
    new_color = random.choice([c for c in range(max_colors) if c != current_color])
    new_sol[node] = new_color
    return new_sol

def cost(graph, coloring):
    conflicts = 0
    for node in graph:
        for neighbor in graph[node]:
            if coloring[node] == coloring[neighbor]:
                conflicts += 1
    return conflicts // 2  # każda para liczona podwójnie
