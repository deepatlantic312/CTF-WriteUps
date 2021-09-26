# get the flag - 20
_Мы перехватили интересный дамп трафика. Посмотри его, и попробуй получить флаг_

[20.pcapng](20.pcapng)

### Solution

Проанализировав трафик, находим, что нужно сделать запрос на http://62.84.118.87:3000 и получить ключ авторизации, затем сделать запрос на http://62.84.118.87:3000/getFlag с ключём в headers.

Приведу скрипт:
```python
from requests import get

key = get("http://62.84.118.87:3000").json()["key"]
print(get("http://62.84.118.87:3000/getFlag", headers={"Authorization": f"Bearer {key}"}).json()["flag"])
```

Получаем флаг: `CTF{Rn2E7BXHtKtDmfgC}`
