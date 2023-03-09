# ナップサック
N, W = [int(i) for i in input().split()]
vv = [[int(i) for i in input().split()]for _ in range(n)]
dp = [[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(n):
    w, v = vv[i]
    for j in range(W+1):
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+w < w+1:
            dp[i+1][j+w] = max(dp[i+1][j], dp[i][j]+v)
# LCS(最長共通部分列)
s = input()
t = input()
dp = [[0]*(len(t)+1)for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
print(dp[-1][-1])
