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
