from pwn import remote

r = remote("62.84.118.87", 9001)

for i in range(49):
    r.recvuntil("Раунд ".encode())
    r.recvline()
    dots = list(map(int, r.recvline().decode().strip().split(";")))
    xl = dots[2] - dots[0]
    yl = dots[3] - dots[1]
    answer = round((xl ** 2 + yl ** 2) ** 0.5, 2)
    r.sendline(str(answer).encode())
r.interactive()
