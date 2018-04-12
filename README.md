# Devman project 03 - Closest bars
Simple script providing common information about Moscow's city bars.

Script's goals is:
1. Find biggest and smallest bars by seats count.
2. Find closest bar to current location based on longitude and latitude provided by user's input.
## Usage
Python >= 3.5 required.
Script requreid file with bars JSON Data provided by [data.mos.ru](https://data.mos.ru/)
### How to get data
There are several options
1. Download directly from [data.mos.ru](https://data.mos.ru/)
    1. Register at [data.mos.ru](https://data.mos.ru/) and get the API key.
    2. Download data <https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}>.
2.
    1. Download data from [http://data.mos.ru/opendata/7710881420-bary](http://data.mos.ru/opendata/7710881420-bary)
### Example use 
To run script open linux shell and run bars.py with required arguments.
```
$ python bars.py -filepath bars.json -latitude 31.435454 -longitude 32.7134  
```
Output example:
```
Category: Biggest bar, Name: Спорт бар «Красная машина»
Category: Smallest bar, Name: БАР. СОКИ
Category: Closest bar, Name: Staropramen
```
## Project goals
This project is created for educational purposes [DEVMAN.org](https://devman.org)
