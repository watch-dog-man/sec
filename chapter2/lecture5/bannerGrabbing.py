# !/usr/bin/python

'''
Banner Grabbing ports with socket
'''

import sys
import socket

def scanner(target, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		if port == 80:
			s.sendall("GET HTTP/1.1 \r \n")
		else:
			s.sendall("Hello \r \n")
		print s.recv(1024)
		s.close()
	except socket.error:
		pass

def main():
	try:
		target = raw_input("Input your target: ")
		list_port = [80, 21, 22, 23, 443]
		for port in list_port:
			scanner(target, port)
        except KeyboardInterrupt:
                print "You pressed Ctrl+C"
                sys.exit()


if __name__ == "__main__":
	main()
