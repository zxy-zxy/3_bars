# Devman project 03 - Closest bars
Simple script providing common information about Moscow's city bars.


### Usage
Python 3.5 required.
Data provided by [data.mos.ru](https://data.mos.ru/)
#### How to get data
1. Register at [data.mos.ru](https://data.mos.ru/) and get the API key.
2. Download data <https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}>.
3. Put the file with data in same catalog with bars.py.

### Example use 
```
$ python bars.py  
```
Input example:
```
Please input filename: bars.json
Please input longitude and lattitude divided by space: 31.435454 32.34345
```
Output example:
```
Biggest bar: Спорт бар «Красная машина»
Smallest bar: БАР. СОКИ
Closest bar: Staropramen
```

# About
Study project at [DEVMAN.org](https://devman.org)
