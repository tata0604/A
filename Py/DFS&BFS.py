
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


#dfs

visited=set()

def DFS(node,visited,graph):
  if node not in visited:
      print(node,end=" ")
      visited.add(node)
  for i in graph[node]:
     DFS(i,visited,graph)

print("DFS search is : ",end="")
DFS('5',visited,graph)
print()
print("---------------------------------")


#bfs

visited=[]
queue=[]

def BFS(node,visited,graph):
   visited.append(node)
   queue.append(node)
   while queue:
      m=queue.pop(0)
      print(m,end=" ")
      for neighbour in graph[m]:
         if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

print("BFS search is : ",end="")
BFS('5',visited,graph)
            