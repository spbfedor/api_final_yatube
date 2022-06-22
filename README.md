# API Yatube
## Интерфейс для социфльной сети Yatube

## Описание:

> совокупность инструментов и функций в виде интерфейса для создания новых приложений, 
> благодаря которому одна программа будет взаимодействовать с другой

## Установка:

- Склонируйте репозиторий на свою машину
```sh
git clone <ссылка на репозиторий>
```
- Активируйте виртуальное окружение python3.7
```sh
python -m venv venv
```
- Обновите менеджер пакетов pip
```sh
python -m pip install --upgrade pip
```
- Установите зависимости
```sh
pip install -r  requirements.txt
```
- Выполните миграции
```sh
python manage.py migrate
```
- Запустите сервер
```sh
python manage.py runserver
```

## Примеры некоторых запросов
```sh
api/v1/posts/
api/v1/comment/
api/v1/group/
api/v1/jwt/create/
api/v1/jwt/users/