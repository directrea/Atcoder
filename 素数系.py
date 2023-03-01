def isPrime(n):  # 試し割り法
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n+1, 2):
        if i*i > n:
            return True
        if n % i == 0:
            return False
    return False


def prime_fact(n):
    pf = []
    while n % 2 == 0:
        n //= 2
        pf.append(2)
    for i in range(3, n+1, 2):
        if i*i > n:
            if n > 1:
                pf.append(n)
            break
        while n % i == 0:
            n //= i
            pf.append(i)
    return pf
