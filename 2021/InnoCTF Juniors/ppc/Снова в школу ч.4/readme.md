# Снова в школу ч.4 - 40
_Решай задачи в удаленном терминале, 50 раундов и флаг твой_

_nc 62.84.118.87 9004_

### Solution
Задача: даны шесть точек на плоскости, являющиеся вершинами треугольника. В формате x1;y1;x2;y2;x3;y3
Найти все три угла вершин A,B,C, где l1 - между вершинами A и B, l2 - между B и C, l3 - между C и A.
x1;y1 - координаты точки A, x2;y2 - координаты точки B, x3;y3 - координаты точки C
Ответы округляются до двух знаков по правилам округления.

Для решения задачи воспользуемся формулой скалярного произведения векторов и выразим косунус угла:

![img](formula.jpg)

Скрипт:
```python
import math
from pwn import remote


def solve(x1, y1, x2, y2, x3, y3):
    cosC = ((x1 - x3) * (x2 - x3) + (y1 - y3) * (y2 - y3)) / (((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5 * ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5)
    cosA = ((x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1)) / (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)
    cosB = ((x1 - x2) * (x3 - x2) + (y1 - y2) * (y3 - y2)) / (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 * ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5)
    return [round(math.degrees(math.acos(cosA)), 2), round(math.degrees(math.acos(cosB)), 2), round(math.degrees(math.acos(cosC)), 2)]


r = remote('62.84.118.87', 9004)

for i in range(49):
    r.recvuntil("Раунд".encode())
    values = list(map(float, r.recvline().strip().decode().split(";")))
    answer = list(map(str, solve(*values)))
    answer = ";".join(answer)
    r.sendline(answer.encode())
r.interactive()

```

Запускаем скрипт и получаем флаг:
`CTF{VZIuER2VLfurspVq}`