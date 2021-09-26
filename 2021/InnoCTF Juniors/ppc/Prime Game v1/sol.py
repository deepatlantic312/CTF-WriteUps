from pwn import remote


def is_prime(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1


r = remote("62.84.119.240", 5550)
for i in range(200):
    r.recvuntil(b"Is")
    r.recvline()
    n = int(r.recvline().strip().decode())
    answer = [b"n", b"y"][is_prime(n)]
    r.sendline(answer)
r.interactive()
