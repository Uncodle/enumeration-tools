#!/usr/bin/python

import socket
import sys

port = 25
target = sys.argv[1]
username = sys.argv[2]

if len(sys.argv) != 3:
	print(".:                                SMTP Users Enumerator                                   :.")
	print(".:                       Modo de uso: python enum-smtp.py 0.0.0.0 username                :.")
	sys.exit(0)

# TODO: Add logic to loop a list of usernames
# TODO: Create conditional to show the message "User discover! instead the response of the VRFY"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((target, port))

banner = tcp.recv(1024)

tcp.send("VRFY " + username + " \r\n")

response = tcp.recv(1024)

print response

