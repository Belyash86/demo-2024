def f(c, e):
    if c > e or c == 11: return 0
    if c == e: return 1
    return f(c+1, e)+f(c*2, e)+f(c**2, e)

print(f(2,20))