# docker compose task
```
Aplikacja zawiera trzy moduły:
 - backend
 - bazę danych
 - elasticsearch
 - kibana
1. Zrób Dockerfile do zbudowania obrazu backendu
    a) Backennd powinien mieć dwa endpointy
    - jeden dla bazy, żeby zwrócić tablice
    - drugi dla elasticsearch, żeby zwrócić index
2. Użyj docker composa
    a) Połącz cztery serwisy
    b) spraw żeby były widoczne mędzysobą
    c) niech backend odpali się na samym końcu
3. Zapisuj logi na swoim dysku
```


```
http://localhost:9201/reservations/_search?pretty=true
```