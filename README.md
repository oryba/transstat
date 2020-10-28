:bangbang: | Stay tuned for updates, the system is under active development
:---: | :---

# Advanced transport statistics

## Overview

This script gets GPS tracking data for public transit in ukrainian cities 
using [Dozor](https://city.dozor.tech), compares to the public database 
[Transphoto](https://transphoto.org) and collects some cool stats from
[KStat](http://kstat.pp.ua).

## Available cities

 - Київ
 - Запоріжжя
 - Маріуполь
 - Біла Церква
 - Житомир
 - Чернігів
 - Львів
 - Тернопіль
 - Чернівці
 - Івано-Франківськ
 - Хмельницький
 - Рівне
 - Луцьк
 - Львівська обл.
 - Миколаїв
 - Одеса
 - Херсон
 - Кропивницький
 - Кривий Ріг
 - Кам'янське
 - Дніпро
 - Краматорськ
 - Суми
 - Полтава
 - Кременчук
 - Харків

## Getting started

Simply run the script to fetch the data to `trans.sqlite`:

```
python3 entry.py
```

OR

```
docker-compose up -d
```
