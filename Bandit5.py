#!/usr/bin/python3

from pwn import *

session = ssh('bandit5', 'bandit.labs.overthewire.org', password='lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR', port=2220)
io=session.process('sh')
#io.interactive()
io.sendline(b'find . -size 1033c -type f ! -executable | xargs file | grep "ASCII"')
print(f'File to cat:   {io.recvline()}')
io.sendline(b'cat ./inhere/maybehere07/.file2')
print(f'Password:   {io.recvline()}')