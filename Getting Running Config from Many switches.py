import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()


hostlist = open("hostlist.py")
for n in hostlist:
	HOST = n.strip()
	print("Connecting to and getting Running Config " + (HOST) )
	tn = telnetlib.Telnet(HOST)
	
	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	
	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")
	
	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	tn.write(b"terminal length 0\n")
	tn.write(b"show running\n")
	tn.write(b"exit\n")
	readoutput = tn.read_all().decode("ascii")
	saveoutput = open("switch" + HOST, "w")
	saveoutput.write(readoutput)
	saveoutput.write("\n")
	saveoutput.close
	print(tn.read_all().decode("ascii"))