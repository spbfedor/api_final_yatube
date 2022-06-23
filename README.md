# API Yatube
## Интерфейс для социфльной сети Yatube

## Описание:

> совокупность инструментов и функций в виде интерфейса для создания новых приложений, 
> благодаря которому одна программа будет взаимодействовать с другой

## Установка Python 3.7:

#### Если у вас Ubuntu, то откройте терминал и выполните команды:

- Обновите список пакетов и установите необходимые компоненты:
```sh
sudo apt upgrade
sudo apt install software-properties-common
```
- Добавьте PPA deadsnakes в список ваших репозиториев:
```sh
sudo add-apt-repository ppa:deadsnakes/ppa
```
- При появлении запроса нажмите Enter, чтобы продолжить:
```sh
Press [ENTER] to continue or Ctrl-c to cancel adding it.
```
- После подключения репозитория установите Python 3.7:
```sh
sudo apt install python3.7
```
- Готово, Python 3.7 установлен в вашей Ubuntu и готов к использованию. 
Убедитесь в этом, выполните команду python3.7 --version
```sh
python3.7 -V
```

#### Если у вас другая операционная система, то воспользуйтесь инструкцией с сайта:

```sh
python.org/about/gettingstarted/
```

## Установка API Yatube:

- Склонируйте репозиторий на свою машину
```sh
git clone git@github.com:spbfedor/api_final_yatube.git
```
- Перейдите в папку проекта
```sh
cd api_final_yatube
```
- Установите пакет виртуального окружения python3.7
```sh
sudo apt install python3.7-venv
```
- В дирректории проекта проекта разверните виртуальное окружение
```sh
python -m venv venv
```
- или
```sh
python3 -m venv venv
```
- Акивируйте виртуальное окружение
- linux
```sh
source venv/bin/activate
```
- mac OS
```sh
source venv/Scripts/activate
```
- Обновите менеджер пакетов pip
```sh
python -m pip install --upgrade pip
```
- Установите зависимости
```sh
pip install -r  requirements.txt
```
- Выполните миграции из директории с файлом manage.py
```sh
python manage.py migrate
```
- Запустите сервер
```sh
python manage.py runserver
```

## Примеры некоторых запросов

- Установите Postman на свой компьютер
```sh
https://www.postman.com/downloads/
```

- Передайте в post запросе данные для создания учетной записи

```sh
POST http://127.0.0.1:8000/api/v1/users/
{
    "email": "caramba@yandex.ru",
    "username": "bart",
    "password": "hddkcmcis"
}
```
 - Ответ должен получиться примерно таким

 ```sh
 { "email" : " caramba@yandex.ru " , "имя пользователя" : "bart" , "id" : 6 }
```

- Отправьте второй запрос
```sh
GET http://127.0.0.1:8000//api/v1/jwt/create/
{
    "username": "bart",
    "password": "hddkcmcis"
}
```
 - В ответы вы получите токен. Этот токен нужно применять к следующим запросам,
 добавив перед ним 
 ```sh
 ?Authentication=Bearer%20
```

GET http://127.0.0.1:8000/api/v1/posts/?Authentication=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi

- Если все сделано правильно, в ответ должен придти пустой словарь.```sh
```sh
[]
```

Отлично! На примере создания учетной записи и получения словаря вы познакомились с запросами.
Словарь пуст т.к. в базе данных отсутствует информация, это отличная возможность потренироваться.
Заполните БД через post запросы.



### Контакты разработчика
- Цветков Федор
- spbfedor@yandex.ru
- Санкт-Петербург
