def kruskal(adj: dict, start=None):
    _ = start

    edges = []
    seen = set()

    # Ubah adjacency list (list of dict) menjadi edge list tanpa duplikasi.
    for u in adj:
        for connection in adj[u]:
            v, w = list(connection.items())[0]
            edge_key = tuple(sorted((u, v)))
            if edge_key in seen:
                continue
            seen.add(edge_key)
            edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])

    parent = {node: node for node in adj}
    rank = {node: 0 for node in adj}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    mst = []
    cost = 0

    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
            cost += w
            if len(mst) == len(adj) - 1:
                break

    return mst, cost

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
