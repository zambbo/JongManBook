
class NavieDisjointset:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if u == self.parent[u]: return u

        return self.find(self.parent[u])
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v: return

        self.parent[root_u] = self.parent[root_v]


ndj = NavieDisjointset(5)

ndj.union(2, 3)
ndj.union(1, 3)
print(ndj.parent)