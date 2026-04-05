# DRF Books API

Учебный backend API-проект на Django REST Framework для работы с книгами и категориями.

## Возможности проекта

### Books API
- просмотр списка книг
- просмотр одной книги
- создание книги
- полное обновление книги (`PUT`)
- частичное обновление книги (`PATCH`)
- удаление книги (`DELETE`)

### Дополнительно
- категории книг
- вложенный serializer для категории
- отдельное поле `category_id` для записи
- вычисляемое поле `is_big`
- фильтрация книг:
  - `?big=true`
  - `?category=<id>`

### Permissions
- чтение доступно всем
- создание, изменение и удаление доступны только авторизованным пользователям

---

## Стек

- Python
- Django
- Django REST Framework
- SQLite

---

## Что реализовано

- `ModelSerializer`
- `ModelViewSet`
- `DefaultRouter`
- `IsAuthenticatedOrReadOnly`
- nested serializer
- `PrimaryKeyRelatedField`
- фильтрация через `query_params`

---

## Модели

### Category
- `name`

### Book
- `title`
- `author`
- `pages`
- `category`

---

## Как запустить проект

### 1. Клонировать репозиторий
```bash
git clone https://github.com/zenixchernik-wq/drf-books-api.git
cd drf-books-api

2. Создать виртуальное окружение
python -m venv venv

3. Активировать виртуальное окружение
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate

4. Установить зависимости
pip install -r requirements.txt

5. Применить миграции
python manage.py makemigrations
python manage.py migrate

6. Создать суперпользователя
python manage.py createsuperuser

7. Запустить сервер
python manage.py runserver