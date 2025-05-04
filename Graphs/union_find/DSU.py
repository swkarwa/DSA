class Solution:
    def find(self , x , par):
        if(x == par[x]):
            return x
        return self.find(par[x] , par)

    def union(self, a, b, parent):
        parent_a = self.find(a , parent)
        parent_b = self.find(b , parent)

        if (parent_a != parent_b):
            parent[parent_b] = parent_a

    def is_connected(self, a, b ,parent):
        return self.find(a , parent) == self.find(b , parent)

N = 5
parent = [0 if(N==0) else n for n in range(N+1)]
nodes = [0 if(N==0) else n for n in range(N+1)]

s = Solution()
s.union(1, 3, parent)
print(s.is_connected(1,2, parent))
s.union(1, 5, parent)
print(s.is_connected(1,5, parent))
