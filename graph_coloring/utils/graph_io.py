def load_graph(file) -> dict:
    edges = []
    with open(file, 'r') if isinstance(file, str) else file as f:
        lines = f.readlines()
        n = int(lines[0])
        edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]

    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v) #sasiedzi
        graph[v].add(u)
    return graph
