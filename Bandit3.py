#!/usr/bin/python3

from pwn import *

session = ssh('bandit3', 'bandit.labs.overthewire.org', password='aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG', port=2220)

io = session.process(['sh', '-c', 'cd inhere; cat .hidden'])

print(io.recvline())