import socket


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("Port : ",str(port),"is OPEN")
		sock.close()
	except:
		pass

def scanner(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)




print("Don\'t Misuse it")
targets = input("[*] Enter Target/s You To Scan(separate them by , ): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print("[*] Scanning Multiple Targets")
	for ip_addr in targets.split(','):
		scanner(ip_addr.strip(' '), ports)
else:
	scanner(targets,ports)
