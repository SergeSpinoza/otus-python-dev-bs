# Репозиторий по курсу Python Developer Basic

## Оглавление
1. [Домашнее задание #1](#01-homework)
2. [Домашнее задание #2](#02-homework)
3. [Домашнее задание #3](#03-homework)
4. [Домашнее задание #4](#04-homework)

<br><br>

## 01 HomeWork
- Реализованы 2 функции `power_numbers` и `filter_numbers` и 3 вспомогательные функции `is_even`, `is_odd`, `is_prime`
- Файл [homework_01/main.py](homework_01/main.py)

## 02 HomeWork
- решение задания находится в директории [homework_02](homework_02)
- в модуле `exceptions` объявлены исключения `LowFuelError`, `NotEnoughFuel`, `CargoOverload`
- доработал базовый класс `base.Vehicle` согласно заданию
- создан датакласс `Engine` в модуле `engine`
- в модуле `car` создан класс `Car`
- в модуле `plane` создан класс `Plane`

Для запуска теста выполнить команду `pytest testing/test_homework_02 -s -vv -rsx`

## 03 HomeWork
- решение задания находится в директории [homework_03](homework_03)
- создано приложение на FastAPI, созданы view для эндпоинтов `/` и `/ping/`
- приложение упаковано в Docker

Для запуска теста выполнить команды: 
- `docker build -t fastapi-app:latest .`
- `docker run -it --rm -p 8000:8000 fastapi-app:latest`

## 04 HomeWork
Для запуска базы в директории `homework_04` выполнить команду `docker-compose up -d`

- все запросы в сеть и БД выполняются асинхронно
- скрипт стягивает данные с API и складывает в БД
- объекты пользователей и постов добавляются в БД пачками, а не по одному
- созданы связи между пользователем и постом
- не происходит мутации глобальных объектов
- автоматический тест `test_homework_04` проходит
