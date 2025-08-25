class Graph:
   def __init__(self, vertices):
       self.vertices = vertices
       self.graph = {i: [] for i in range(vertices)}


   def add_edge(self, u, v):
       self.graph[u].append(v)
       self.graph[v].append(u)


   def dfs(self, start):
       visited = [False] * self.vertices
       self._dfs_util(start, visited)


   def _dfs_util(self, v, visited):
       visited[v] = True
       print(v, end=" ")
       for neighbor in self.graph[v]:
               self._dfs_util(neighbor, visited)
           if not visited[neighbor]:


vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))
g = Graph(vertices)


for _ in range(edges):
   u, v = map(int, input("Enter edge (u v): ").split())
   g.add_edge(u, v)


start_node = int(input("Enter starting node for DFS: "))
print("DFS traversal:")
g.dfs(start_node)
