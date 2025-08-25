from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {}
nodes = int(input("Enter number of nodes: "))

print("\nEnter adjacency list (neighbors separated by space):")
for i in range(nodes):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node}: ").split()
    graph[node] = neighbors

start = input("\nEnter starting node for BFS: ")

# Run BFS
print()
bfs(graph, start)
