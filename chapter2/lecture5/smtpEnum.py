# !/usr/bin/python

'''
SMTP enumeration with Python socket
'''

import sys
import socket

def enum(target, user):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, 25))
		s.recv(1024)
		s.sendall("VRFY " + user + " \r\n")
		result = s.recv(2048)
		if "252" in result:
			print result
		else:
			pass
		s.close()
	except socket.error:
		pass

def main():
	try:
		target = raw_input("Input your target: ")
		data = open("usernames.txt").read()
		users = data.split("\n")
		for user in users:
			enum(target, user)
        except KeyboardInterrupt:
                print "You pressed Ctrl+C"
                sys.exit()


if __name__ == "__main__":
	main()
