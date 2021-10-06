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
docker-compose up
docker-compose logs > logs.txt
```


https://gist.github.com/ErikNovak/186e6021cf30db9160c673ee3145629f#file-logstash-pg-es-md
https://medium.com/@emreceylan/how-to-sync-postgresql-data-to-elasticsearch-572af15845ad


```
poetry export -f requirements.txt --output api/requirements.txt
```

```
https://github.com/deviantony/docker-elk/blob/main/docker-stack.yml
```

https://www.youtube.com/watch?v=TyixiRWJGmw
https://www.youtube.com/watch?v=PCvVCjC-wp0