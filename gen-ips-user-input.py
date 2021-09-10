from ipaddress import ip_address

# Python - Generate a list of IP addresses from user input
# https://stackoverflow.com/questions/17641492/how-can-i-generate-all-possible-ips-from-a-list-of-ip-ranges-in-python

def ips(start, end):
    '''Return IPs in IPv4 range, inclusive.'''
    start_int = int(ip_address(start).packed.hex(), 16)
    end_int = int(ip_address(end).packed.hex(), 16)
    return [ip_address(ip).exploded for ip in range(start_int, end_int)]


lista = ips('172.16.0.1', '172.16.0.255')
for x in range(len(lista)):
        print(lista[x])
