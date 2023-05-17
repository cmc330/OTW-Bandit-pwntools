#!/usr/bin/python3

from pwn import *

session = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)

io = session.process(['sh', '-c', 'cat readme'])
print(io.recvline())