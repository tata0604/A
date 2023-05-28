# def dfs(graph, node, visited):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs(graph, neighbor, visited)
            
# graph = {
#     'A':['B', 'C'],
#     'B':['A', 'D', 'E'],
#     'C':['A', 'F', 'G'],
#     'D':['B'],
#     'E':['C'],
#     'F':['C'],
#     'G':['C']
# }
# dfs(graph, 'A', set())

# print("\n")

graph = {
    'A':['B', 'C'],
    'B':['A', 'D', 'E'],
    'C':['A', 'F', 'G'],
    'D':['B'],
    'E':['C'],
    'F':['C'],
    'G':['C']
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s)
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                
bfs(visited, graph, 'A')