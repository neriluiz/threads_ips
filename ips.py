# Ponto de partida para montar: buffer overflow, verificador de ip,
# calculo de ip, teste de stress, scan simultâneo.

import  ipaddress

ip1 = '192.168.0.0'
ip2 = '192.168.0.0/24'
ip3 = '192.168.0.100/24'

endereco1 = ipaddress.ip_address(ip1)
rede1 = ipaddress.ip_network(ip2)
rede2 = ipaddress.ip_network(ip3, strict=False)

print(endereco1 + 257)
print(rede1)
print(rede2)

for ip in rede1:
    print(ip)