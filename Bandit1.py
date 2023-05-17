#!/usr/bin/python3

from pwn import *

session = ssh('bandit1', 'bandit.labs.overthewire.org', password='NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL', port=2220)

io = session.process(['sh', '-c', 'cat ./-'])
print(io.recvline())