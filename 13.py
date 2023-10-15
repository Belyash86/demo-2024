from ipaddress import ip_network as net
k = 0
for ip in net('192.168.32.160/28'):
    if bin(int(ip))[2:].count('1') % 2 == 0: k += 1
print(k)