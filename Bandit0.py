from pwn import *

session = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)

io = session.process('sh')
io.interactive()