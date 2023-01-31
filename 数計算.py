def fast_pow(n, m, MOD=None):  # n^mを高速で行う
    jyou = [n]
    while 1 << len(jyou) <= m:
        jyou.append(jyou[-1]**2)
        if MOD:
            jyou[-1] %= MOD
    ans = 1
    for i in range(len(bin(m))-2):
        if m & (1 << i):
            ans *= jyou[i]
            if MOD:
                ans %= MOD
    return ans


def Combination(n, r, MOD=None):  # MODが素数
    if n-r < r:
        r = n-r
    num = 1
    for i in range(1, r+1):
        if MOD:
            num *= (n-i+1) * pow(i, MOD-2, MOD) % MOD
        else:
            num *= (n-i+1)//i
        num %= MOD
    return num
