# for x in '0123456789abcdefghi':
#     res = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
#     if res % 18 == 0:
#         print(res//18)

x = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
k = 0
while x:
    if x%25 == 0:
        k += 1
    x //= 25
print(k)