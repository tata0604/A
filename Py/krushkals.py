def kruskal(graph):
    mst = []
    edges = [(cost, frm, to) for frm, to_dict in graph.items() for to, cost in to_dict.items()]
    edges.sort()
    parent = {node: node for node in graph}

    def find_root(node):
        if parent[node] == node:
            return node
        parent[node] = find_root(parent[node])
        return parent[node]

    for cost, frm, to in edges:
        root1 = find_root(frm)
        root2 = find_root(to)
    
        if root1 != root2:
            parent[root1] = root2
            mst.append((frm, to, cost))
    return mst
    

graph = {
 'A': {'B': 2, 'C': 3},
 'B': {'A': 2, 'C': 1, 'D': 1},
 'C': {'A': 3, 'B': 1, 'D': 4},
 'D': {'B': 1, 'C': 4},
}
print(kruskal(graph))