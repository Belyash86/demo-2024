f = open('files/24/24_2024.txt').readline()
# f = '123T1234T12T12T12T123456789'
a = [x+1 for x in range(len(f)) if f[x] == 'T']
maxt = a[100]-1
for i in range(101, len(a)):
    l = a[i] - a[i-101] - 1
    maxt = max(maxt, l)
maxt = max(maxt, len(f)-a[-3])
print(maxt)