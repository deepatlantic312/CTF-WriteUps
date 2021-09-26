from pwn import remote

r = remote("62.84.118.87", 9002)

for i in range(49):
    r.recvuntil("Раунд".encode())
    r.recvline()
    x, y, rad = map(int, r.recvline().strip().decode().split(";"))
    count = 0
    if rad ** 2 - y ** 2 > 0:
        count += 2
    elif rad ** 2 - y ** 2 == 0:
        count += 1
    if rad ** 2 - x ** 2 > 0:
        count += 2
    elif rad ** 2 - x ** 2 == 0:
        count += 1
    answer = str(count).encode()
    r.sendline(answer)
r.interactive()
