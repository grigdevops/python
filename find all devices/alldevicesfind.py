import socket
import nmap

def get_network_space():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    subnet = '.'.join(ip.split('.')[:-1]) + '.0/24'
    return subnet

def find_devices(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')
    hosts = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    return hosts

network = get_network_space()
devices = find_devices(network)
print(devices)