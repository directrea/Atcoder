def fast_pow(n, m):  # n^mを高速で行う
    jyou = [n]
    while 1 << len(jyou) <= m:
        jyou.append(jyou[-1]**2)
    ans = 1
    for i in range(len(bin(m))-2):
        if m & (1 << i):
            ans *= jyou[i]
    return ans
