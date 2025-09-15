from collections import defaultdict

class TarjanSCC:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        self.index = 0
        self.stack = []
        self.on_stack = [False]*n
        self.indexes = [-1]*n
        self.lowlink = [-1]*n
        self.result = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def strongconnect(self, v):
        self.indexes[v] = self.index
        self.lowlink[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.on_stack[v] = True

        for w in self.graph[v]:
            if self.indexes[w] == -1:
                self.strongconnect(w)
                self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
            elif self.on_stack[w]:
                self.lowlink[v] = min(self.lowlink[v], self.indexes[w])

        if self.lowlink[v] == self.indexes[v]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            self.result.append(scc)

    def get_scc(self):
        for v in range(self.n):
            if self.indexes[v] == -1:
                self.strongconnect(v)
        return self.result

g = TarjanSCC(5)
g.add_edge(1,0)
g.add_edge(0,2)
g.add_edge(2,1)
g.add_edge(0,3)
g.add_edge(3,4)
print("SCC:", g.get_scc())
