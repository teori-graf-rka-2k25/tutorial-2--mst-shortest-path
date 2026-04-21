def kruskal(graph):
    # Ekstrak nodes 
    nodes = set()
    for w, u, v in graph:
        nodes.add(u)
        nodes.add(v)
    
    #  Union-Find
    parent = {n: n for n in nodes}
    
    def find(n):
        if parent[n] != n:
            parent[n] = find(parent[n])
        return parent[n]

    # Urutkan graf berdasarkan bobot
    graph.sort()

    # Algoritma MST
    mst, total = [], 0
    for w, u, v in graph:
        if find(u) != find(v):
            parent[find(u)] = find(v)
            mst.append((u, v, w))
            total += w
            
    return mst, total


import heapq

def prims(adj: dict, start):
    visited = set([start])
    edges = []

    for connection in adj[start]:
        v, w = list(connection.items())[0]
        edges.append((w, start, v))

    heapq.heapify(edges)
    mst = []
    cost = 0

    while edges:
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue

        visited.add(v)
        mst.append((u, v, w))
        cost += w

        for connection in adj[v]:
            next_v, next_w = list(connection.items())[0]
            if next_v not in visited:
                heapq.heappush(edges, (next_w, v, next_v))

    return mst, cost
