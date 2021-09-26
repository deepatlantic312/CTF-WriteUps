# Секретное задание - 20
_В лапы наших оперативников попал этот шифротекст. Эти балбесы даже не понимают, что здесь написано. Может, тебе удастся разобраться и найти ключ? Только дело до ключа нам нет, нам нужно понять, о какой организации в тексте идет речь. Она там часто упоминается. Не перепутай, ключ не **вижен**, важна само название организации_

_[encrypted](encrypted)_

### Solution

По подсказке из условия таска (`ключ не ВИЖЕН`) можно понять, что используется шифр Виженера.

Используем [онлайн тулзу](https://www.guballa.de/vigenere-solver) для брута ключа и декода.

Получаем:
```WikiLeaks is a multi-national media organization and associated library. It was founded by its publisher Julian Assange in 2006.
WikiLeaks specializes in the analysis and publication of large datasets of censored or otherwise restricted official materials involving war, spying and corruption. It has so far published more than 10 million documents and associated analyses.
“WikiLeaks is a giant library of the world's most persecuted documents. We give asylum to these documents, we analyze them, we promote them and we obtain more.” - Julian Assange, Der Spiegel Interview
WikiLeaks has contractual relationships and secure communications paths to more than 100 major media organizations from around the world. This gives WikiLeaks sources negotiating power, impact and technical protections that would otherwise be difficult or impossible to achieve.
Although no organization can hope to have a perfect record forever, thus far WikiLeaks has a perfect in document authentication and resistance to all censorship attempts.```
```

По условию нам нужно название организации: `WikiLeaks`