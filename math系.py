import math

# θ=rad
math.radians()
# θから辺の日を求める
math.cos()
# cosの逆関数 辺の比からθを求める
math.acos()


def lcm(x, y):  # 最小公倍数
    return (x*y)//math.gcd(x, y)


def circleXY(d, r):
    rad = math.radians(d)
    x = r*math.cos(rad)
    y = r*math.sin(rad)
    return [x, y]


def dis(a, b):
    res = 0
    for i in range(len(a)):
        res += (a[i]-b[i])**2
    return math.sqrt(res)
