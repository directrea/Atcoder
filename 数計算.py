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
    facts = [1, 1]
    for i in range(2, n+1):
        facts.append(facts[-1]*i)
        if MOD:
            facts[-1] %= MOD
    res = facts[n]
    if MOD:
        res *= pow(facts[r]*facts[n-r], MOD-2, MOD)
        res %= MOD
    else:
        res //= facts[r]*facts[n-r]
    return res
