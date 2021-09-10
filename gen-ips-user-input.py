from ipaddress import ip_address

# Python - Generate a list of IP addresses from user input
# https://stackoverflow.com/questions/17641492/how-can-i-generate-all-possible-ips-from-a-list-of-ip-ranges-in-python
# https://ipinfo.io/

def ips(start, end):
    '''Return IPs in IPv4 range, inclusive.'''
    start_int = int(ip_address(start).packed.hex(), 16)
    end_int = int(ip_address(end).packed.hex(), 16)
    return [ip_address(ip).exploded for ip in range(start_int, end_int)]


results = ips('192.168.0.1', '192.168.0.255')
#for x in range(len(lista)):
 #       print(lista[x])

with open('test-resultado.txt', 'w') as f:
    for row in results:
        f.write("%s\n" % str(row))
print("Resultado salvo em test-resultado.txt")
