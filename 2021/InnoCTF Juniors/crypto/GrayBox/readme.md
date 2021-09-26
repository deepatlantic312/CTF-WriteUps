# Graybox - 50
_Наши аналитики работают с шифровальщиком. Уже известно, что это бинарный файл, он выполняет некоторые побитовые операции над текстом, а на выходе выплевывает всё как есть, то есть ascii-текст, включая непечатаемые символы. Для того, чтобы узнать ключ, придется потратить немало времени. В приложении мы даем функцию генерации этого самого ключа, которую нам удалось заполучить методом реверс-инженерии, а также зашифрованный текст, который является разгадкой к задаче. Сам бинарный файл мы не даем, так как еще не закончили анализировать его. Узнай ключ и восстанови оригинальный текст. seed=40_

_[prng.c](prng.c)_

_[cipher](cipher)_
### Solution
Так как нам дан изначальный сид, то мы можем восстановить ключ.

Скрипт:
```python
seeds = [40]
for i in range(39):
    seed = seeds[-1]
    seeds.append((seed * 5 + (seed - 9) + 6) % 300)
keys = list(map(lambda x: x % 25 + 65, seeds))
print(keys)
```

В условии сказано, что выполняются некоторые побитовые операции.
Первое, что пришло в голову, это **xor**, пишем скрипт:

```python
with open("cipher", "rb") as f:
    data = f.read()
s = ""
for i in range(len(data)):
    s += chr(data[i] ^ keys[i % 40])
print(s)
```

Получаем строку:

`Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with like CTF{GR4YB0XCRypt0} and other things`

и флаг: `CTF{GR4YB0XCRypt0}`