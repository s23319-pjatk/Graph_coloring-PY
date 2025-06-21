from itertools import product

def brute_force(graph, max_colors):
    nodes = list(graph.keys())
    best = None
    best_cost = float('inf')

    # Generujemy wszystkie możliwe kombinacje kolorów (0 do max_colors-1) dla każdego wierzchołka
    for coloring_tuple in product(range(max_colors), repeat=len(nodes)):
        coloring = dict(zip(nodes, coloring_tuple)) #przypisanie kolorow w->k
        conflicts = sum(
            1 for u in graph for v in graph[u] if u < v and coloring[u] == coloring[v]
        )
        if conflicts < best_cost:
            best = coloring
            best_cost = conflicts
            if best_cost == 0:      #sprawdzenie konfliktow 0 najlepsze
                break

    return best, best_cost
#pelny przeglad wykonany