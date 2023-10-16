for A in range(1, 1000):
    k = 0
    for x in range(1, 100+1):
        for y in range(1, 100+1):
            f = ((x + 2*y) < A) or (y>x) or (x>60)
            if f == 1: k += 1
    if k == 100*100:
        print(A)
        exit()