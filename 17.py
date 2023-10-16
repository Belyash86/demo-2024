a = [int(x) for x in open('files/17/17_2024.txt')]
max13 = max([x for x in a if str(x)[-2:] == '13'])
k, k_sum = 0, 0
for i in range(len(a)-2):
    x1, x2, x3 = a[i], a[i+1], a[i+2]
    if ((len(str(x1)) == 3 and len(str(x2)) == 3 and len(str(x3)) != 3) or \
        (len(str(x1)) == 3 and len(str(x3)) == 3 and len(str(x2)) != 3) or \
        (len(str(x2)) == 3 and len(str(x3)) == 3 and len(str(x1)) != 3)) and \
        x1+x2+x3 <= max13:
            k += 1
            k_sum = max(k_sum, x1+x2+x3)
print(k, k_sum)