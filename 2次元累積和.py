class PrefixSum2D:
    def __init__(self, vv) -> None:
        self.data = self.build(vv)

    def build(self, vv):
        data = [[0]*(len(vv[0])+1)for _ in range(len(vv)+1)]
        for i in range(len(vv)):
            for j in range(len(vv[i])):
                data[i+1][j+1] += vv[i][j]
                data[i+1][j+1] += data[i][j+1]+data[i+1][j]
                data[i+1][j+1] -= data[i][j]
        return data

    def query(self, q):
        ans = self.data[q[2]][q[3]]
        ans -= self.data[q[0]-1][q[3]]+self.data[q[2]][q[1]-1]
        ans += self.data[q[0]-1][q[1]-1]
        return ans


h, w = [int(i) for i in input().split()]
vv = [[int(i) for i in input().split()]for _ in range(h)]
qn = int(input())
qs = [[int(i) for i in input().split()]for _ in range(qn)]

ps2 = PrefixSum2D(vv)
for q in qs:
    print(ps2.query(q))
