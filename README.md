![Документация](head.png)
# Учебный проект по «API для Yatube»

:small_orange_diamond: **Пояснение.**
> API_YAMDB информационный ресурс с оценками и отзывами, на книги, фильмы, музыку. Реализованная на фреймворке Django.
API для неё реализованно на Django Rest Framework (DRF).

Целью проекта является создание API для API_YAMDB. При помощи такой мощной разработки,
мы без проблем, сможем подружить бэкенд с фронтендом!!! :fire:

:yellow_circle: Когда вы запустите проект, по адресу  http://127.0.0.1:8000/redoc/ будет доступна :book: документация для API

:yellow_circle: Для аутентификации используются JWT-токены. 


## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/chillentano/api_yamdb.git
```

```
cd api_yamdb
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/bin/activate
```

### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
python manage.py migrate
```

### Запустить проект:

```
python manage.py runserver
```
