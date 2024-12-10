from collections import deque

def bfs(graph, to_visit, visited=set(), path=[]):
    current_node = to_visit.popleft()

    visited.add(current_node)
    path.append(current_node)

    neighbors = graph['edges'][current_node]

    for node in neighbors:
        if node not in to_visit and node not in visited:
            to_visit.append(node)

    if to_visit:
        return bfs(graph, to_visit, visited)
    return path
