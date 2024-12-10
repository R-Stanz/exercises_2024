from search import bfs
from collections import deque

graph = {
        'begin' : 1,
        'nodes' : {i for i in range(8)},
        'edges' : {
            0 : [],
            1 : [0,2,3],
            2 : [5],
            3 : [],
            4 : [],
            5 : [3,6,7],
            6 : [4],
            7 : []
        }
}

to_visit = deque()
to_visit.append(1)

paths_found = bfs(graph=graph, to_visit=to_visit)

print(paths_found)
