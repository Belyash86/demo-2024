import csv
k = 0
for c in csv.reader(open('files/9/9_2024.csv'), delimiter=';'):
    s = [int(x) for x in c]
    rep = set()
    for x in s:
        if s.count(x) == 2: rep.add(x)
    if len(rep) == 2 and (sum(rep)/2 < sum(s)/7):
        k += 1
print(k)