from netmiko import ConnectHandler

cisco_switch1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.100',
    'username': 'admin',
    'password': 'cisco',
}

net_connect = ConnectHandler(**cisco_switch1)

for n in range(2,10):
	print("Deleting VLAN " + str(n))
	config_commands = ["no vlan " + str(n), "name Python_VLAN " + str(n)]
	output = net_connect.send_config_set(config_commands)	
output = net_connect.send_command('show vlan brief')
print(output)