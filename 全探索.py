n = 0
for bit in range(1 << n):
    for i in range(n):
        if bit & (1 << i):
            pass
