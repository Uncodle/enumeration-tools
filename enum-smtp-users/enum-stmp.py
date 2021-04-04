#!/usr/bin/python
#coding:utf-8

import socket, sys, re

port = 25
target = sys.argv[1]
filename = sys.argv[2]

wordlist = open(filename)

if len(sys.argv) != 3:
	print ".:                                SMTP Users Enumerator                                   :."
	print ".:              Modo de uso: python enum-smtp.py 0.0.0.0 wordlist.txt	                 :."
	sys.exit(0)

# TODO: Add possibility to execute the script with an wordlist file or a single username

for username in wordlist:
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((target, port))
	banner = tcp.recv(1024)
	tcp.send("VRFY " + username)
	user = tcp.recv(1024)
	if re.search("252", user):
		print "[+] Usuário descoberto! -> " + user.strip("252 2.0.0")
