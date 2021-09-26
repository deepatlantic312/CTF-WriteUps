# Prime Game v1 - 25
_Помнишь какие числа называют простыми? Ну вот тут тоже все просто - тебе на вход число, а ты говоришь простое оно или нет._

_nc 62.84.119.240 5550_

### Solution
Задача определить, является ли число простым.

Единственная идея, которая используется для решения, о том, что если не существует делителей от 2 до n ^ 0.5, то число n - простое.
Скрипт:
```python
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
```

Флаг: `CTF{345y_70_f1nd_15_pr1m3_numb3r}`