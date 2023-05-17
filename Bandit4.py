#!/usr/bin/python3

from pwn import *

session = ssh('bandit4', 'bandit.labs.overthewire.org', password='2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe', port=2220)
# Because we need to know if its human readable (Such as ASCII text) we need the file command which cannot accept input 
# so we can either use xargs to force it to or use sub commands $(find .) to pass the information we need as an argument to find.
# commands: find . | xargs file or file $(find .)
# this shows file07 is the only ASCII text file so we will cat that 
io = session.process(['sh', '-c', 'cd inhere; cat ./-file07'])

print(io.recvline())