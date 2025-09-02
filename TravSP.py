import itertools

def tsp(graph):
    n = len(graph)
    dp = {}
    for i in range(n):
        dp[(1<<i, i)] = (graph[0][i], [0, i])

    for r in range(2, n+1):
        for subset in itertools.combinations(range(n), r):
            if 0 not in subset: continue
            mask = sum([1<<i for i in subset])
            for j in subset:
                if j == 0: continue
                prev_mask = mask ^ (1<<j)
                min_cost, path = min([(dp[(prev_mask, k)][0] + graph[k][j], dp[(prev_mask, k)][1] + [j]) 
                                      for k in subset if k != j], key=lambda x: x[0])
                dp[(mask, j)] = (min_cost, path)

    mask = (1<<n) - 1
    min_cost, path = min([(dp[(mask, j)][0] + graph[j][0], dp[(mask, j)][1] + [0]) 
                          for j in range(1, n)], key=lambda x: x[0])
    return min_cost, path

n = int(input("Enter number of cities: "))
graph = [list(map(int, input().split())) for _ in range(n)]
cost, path = tsp(graph)
print("Minimum Cost:", cost)
print("Path:", path)

# Complexity: O(n^2 * 2^n) (Exponential, DP optimized)
