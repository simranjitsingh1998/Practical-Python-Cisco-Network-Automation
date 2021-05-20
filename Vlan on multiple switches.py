import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()


hostlist = open("hostlist.py")
for n in hostlist:
	HOST = n.strip()
	print("Connecting to " + (HOST) )
	tn = telnetlib.Telnet(HOST)
	
	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	
	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")
	
	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	tn.write(b"conf t\n")
	for n in range(1,11):
		tn.write(b"vlan " + str(n).encode("ascii") + "\n".encode("ascii"))
		tn.write(b"name Python_Vlan_" + str(n).encode("ascii") + "\n".encode("ascii"))	
	tn.write(b"end\n")
	tn.write(b"exit\n")
	print(tn.read_all().decode('ascii'))