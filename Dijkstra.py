import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        for neigh, w in graph[node]:
            if dist[node] + w < dist[neigh]:
                dist[neigh] = dist[node] + w
                heapq.heappush(pq, (dist[neigh], neigh))
    return dist

n = int(input("Enter number of vertices: "))
graph = {i: [] for i in range(n)}
e = int(input("Enter number of edges: "))
for _ in range(e):
    u,v,w = map(int,input("Enter edge u v w: ").split())
    graph[u].append((v,w))
    graph[v].append((u,w))  # for undirected
start = int(input("Enter start node: "))
print("Shortest distances:", dijkstra(graph, start))

# Complexity:
# Time: O((V+E) log V)
# Space: O(V)
