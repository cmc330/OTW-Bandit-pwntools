#!/usr/bin/python3

from pwn import *

session = ssh('bandit2', 'bandit.labs.overthewire.org', password='rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi', port=2220)

io = session.process(['sh', '-c', 'cat "spaces in this filename"'])
print(io.recvline())