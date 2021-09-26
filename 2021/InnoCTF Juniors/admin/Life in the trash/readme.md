# Life in the trash - 20
_Сможешь найти флаг в куче мусора? Не забывай про формат. Да пребудет с тобой grep!_

_[t.txt](t.txt)_

### Solution
Попробуем искать по известному формату флага:

```commandline
grep t.txt CTF{
```

Безрезультатно

А что если флаг перевёрнут?

Пробуем:
```commandline
grep {FTC t.txt | rev
```

Находим флаг: `CTF{+PX{FZSj_{/H@N@}-;o8wfxC]5Fq~L!}`
