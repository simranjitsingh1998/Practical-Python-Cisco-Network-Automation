import netmiko
from netmiko import ConnectHandler

cisco_switch1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.100',
    'username': 'admin',
    'password': 'cisco',
}
cisco_switch2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.102',
    'username': 'admin',
    'password': 'cisco',
}
cisco_switch3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.103',
    'username': 'admin',
    'password': 'cisco',
}
cisco_switch4 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.104',
    'username': 'admin',
    'password': 'cisco',
}


with open('iosv_l2_config1') as f:
    lines = f.read().splitlines()
print (lines)

cisco_devices = [cisco_switch1,cisco_switch2,cisco_switch3,cisco_switch4]

for devices in cisco_devices:
    print("Connecting to " + str(devices))
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)