
graph = {"a":["b", "e"],
        "b":["c"],
        "c":["d"],
        "d":[],
        "e":[]}

path = []
def explore (start, end, graph):
    path.append(start)
    if start == end:
        return True
    for neighbour in graph[start]:
        if not neighbour in path:
            if explore(neighbour, end, graph):
                return True
    return False

explore("a", "e", graph)
print(path)
