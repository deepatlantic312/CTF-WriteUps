# Шифровальщик - 30
_Сегодня мы должны были получить инструкции для начала работы над нашим проектом. Но, к сожалению, сама инструкция была перехвачена злоумышленниками и зашифрована. Они просят перевести им пару биткоинов, а в качестве подтверждения честности сделки прислали код своего шифровальщика. Как по мне, банальщина, и шифр перестановки. Тебе такое по зубам? Даем код программы-вредоноса и сам шифротекст. Ждем от тебя мануала по этой утилите, ее название и будет ответом и разгадкой_

_[cipher.py](cipher.py)_

_[ciphertext.txt](ciphertext.txt)_

### Solution
Обращаем своё внимание в cipher.py на 
`data = data[:j-prev] + data[j:] + data[j-prev:j]`

Мы можем сделать вывод о том, что длина изначальной строки совпадает с данной в условии и что длина меняющихся блоков не зависит от первоначальной строки.

Напишем скрипт, чтобы узнать, какие элементы поменялись местами, затем в обратном порядке поменяем их и получим исходные данные:

```python
data = "ih uelaguyptoa sUeNstihn  Ur efGifaoer   n.o cnirfGonNs tdcdtsrehe eoeehi avt rteho gietdrp siatrtavgcy tnnet un-rgoosb an eiav eenl rntigetsriicx oleep   f oh ctnme,gfi snurtaohd pceget Oe  outo nrelrsfe (eRcsndeT SuctPioOe e oA EtiRt,dto)l naceh is   noh mswe ekdt el(shisfn)tir nd  atlorfefasrnw ooefr,aopu itto, i etoco epra hm hpi tienavsd oifnn eiot nshn ntelxe me nffts. man-I iuo,t ri e o gi fietcds mpidi.ssdcv`a'sa  nTmsdeh."
steps = [7,11,5,19,2,26,12,3,11,40,4,18,9,17,32]
data = list(data)

d = []

for i in steps:
    for j in range(len(data)):
        if j % i == 0:
            if j + i < len(data):
                d.append((j, j + i))
            else:
                continue
d = d[::-1]

for i, j in d:
    [data[i], data[j]] = [data[j], data[i]]
print("".join(data))
```

На выходе получаем:

``This manual page documents the GNU version of find. GNU find searches the directory tree rooted at each given starting-point by evaluating the given expression from left to right, according to the rules of precedence (see section OPERATORS), until the outcome is known (the left hand side is false for and operations, true for or), at which point find moves on to the next file name. If no starting-point is specified, `.' is assumed.``

Это мануал по утилите `find` 