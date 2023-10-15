def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin((n%3)*3)[2:]
    return int(r, 2)
min_r = 10**20
for n in range(1, 10000):
    if f(n) > 151: min_r = min(min_r, f(n))

print(min_r)