from netmiko import ConnectHandler

cisco_switch1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.100',
    'username': 'admin',
    'password': 'cisco',
}

net_connect = ConnectHandler(**cisco_switch1)
output = net_connect.send_command('show ip int brief')
print(output)