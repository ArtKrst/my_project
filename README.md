# Проект bank_card_project

## Описание:

Проект bank_card_project - это виджет банковских операций клиента
Данный проект предназначен для обработки данных, включая функции маскировки номеров карт и счетов, а также функции фильтрации и сортировки данных.

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/ArtKrst/my_project.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

### Маскировка номера карты

python
from src.mask import getmaskcardnumber

maskedcard = getmaskcardnumber("7000792289606361")
print(maskedcard)  # Вывод: 7000 79  6361
### Маскировка номера счета

python
from src.mask import getmaskaccount

maskedaccount = getmaskaccount("73654108430135874305")
print(maskedaccount)  # Вывод: 4305
### Фильтрация по состоянию

python
from src.processing.processing import filterbystate

data = 
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},


executeditems = filterbystate(data)
print(executeditems)  # Вывод: {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
