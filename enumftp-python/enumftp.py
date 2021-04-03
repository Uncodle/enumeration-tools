#!/usr/bin/python
# coding=utf-8

import socket
import sys

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],21))

print("[+] Conectando ao servidor [...] \n")

banner = tcp.recv(1024)

print banner

print("[+] Entrando com o usuário anonymous [...] \n")

tcp.send("USER anonymous\r\n")
user = tcp.recv(1024)

print user

print("[+] Entrando com a senha [...] \n")

tcp.send("PASS \r\n")

response = tcp.recv(1024)

print response
