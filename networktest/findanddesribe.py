import pyshark

def find_devices_lldp(interface):
    cap = pyshark.LiveCapture(interface=interface)
    cap.sniff(packet_count=10)
    devices = []
    for packet in cap:
        if 'LLDP' in packet:
            device = {
                'device_id': packet.lldp.chassis_id,
                'port_id': packet.lldp.port_id,
                'system_name': packet.lldp.system_name
            }
            devices.append(device)
    return devices

network_interface = "eth0"  # Replace with the name of your personal computer's network interface
devices = find_devices_lldp(network_interface)

for device in devices:
    print("Device ID: {} | Port ID: {} | System Name: {}".format(device['device_id'], device['port_id'], device['system_name']))
