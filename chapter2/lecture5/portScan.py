# !/usr/bin/python

'''
TCP Port scanner with socket 
'''

import sys
import socket

def scanner(target, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)
	if s.connect_ex((target, port)) == 0:
		print "Port %d open" %(port)
	else:
		pass
	s.close()

def main():
	try:
		target = raw_input("Input your target: ")
		list_port = [80, 21, 22, 23, 443, 110]
		for port in list_port:
			scanner(target, port)
	except socket.error:
                print "Network error!"
        except KeyboardInterrupt:
                print "You pressed Ctrl+C"
                sys.exit()


if __name__ == "__main__":
	main()
