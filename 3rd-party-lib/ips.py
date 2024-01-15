import ipaddress

#
# my_ip = ipaddress.ip_address('192.168.0.1')
#
#
# print(my_ip-2)

my_net = ipaddress.ip_network('192.168.0.1/0', strict=False)

c = 0
for ip in my_net:
    print(ip)
    c = c + 1
print(c)
