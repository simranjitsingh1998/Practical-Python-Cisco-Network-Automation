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
config_commands = [ 'int lo0',
                    'ip add 10.1.1.1 255.255.255.0 ',
                    'end' ]
output = net_connect.send_config_set(config_commands)
print(output)
for n in range(2,10):
	print("Creating VLAN " + str(n))
	config_commands = ["vlan " + str(n), "name Python_VLAN " + str(n)]
	output = net_connect.send_config_set(config_commands)
	print(output)
output = net_connect.send_command('show vlan brief')
print(output)