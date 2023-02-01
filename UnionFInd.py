class UnionFind:
    def __init__(self, n) -> None:
        self.nodes = [i for i in range(n)]

    def unite(self, x, y):
        if x > y:
            x, y = y, x
        rootx = self.root(x)
        rooty = self.root(y)
        self.nodes[rooty] = rootx

    def same(self, x, y):
        if self.root(x) == self.root(y):
            return 1
        else:
            return 0

    def root(self, x):
        leafs = []
        while x != self.nodes[x]:
            leafs.append(x)
            x = self.nodes[x]
        for i in range(len(leafs)-1):
            self.nodes[leafs[i]] = x
        return x
