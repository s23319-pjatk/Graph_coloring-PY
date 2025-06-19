from itertools import product

def brute_force(graph, max_colors):
    nodes = list(graph.keys())
    best = None
    best_cost = float('inf')

    for coloring_tuple in product(range(max_colors), repeat=len(nodes)):
        coloring = dict(zip(nodes, coloring_tuple))
        conflicts = sum(
            1 for u in graph for v in graph[u] if u < v and coloring[u] == coloring[v]
        )
        if conflicts < best_cost:
            best = coloring
            best_cost = conflicts
            if best_cost == 0:
                break

    return best, best_cost
