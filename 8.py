from itertools import product
k = 0
wrong = set()
for p in product('0246', repeat=2):
    wrong.add(''.join(p))
for p in product('1357', repeat=2):
    wrong.add(''.join(p))
for p in product('01234567', repeat=5):
    s = ''.join(p)
    if s[0] != '0' and s.count('1') == 0 and len(set(s)) == 5:
        for w in wrong:
            if w in s:
                break
        else:
            k += 1
print(k)