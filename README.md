
# 📝 Notes (Django + PostgreSQL + Docker)

Простой Django-сервис для заметок с использованием моделями. Контейнеризирован через Docker. Настроен панель Admin.
Подключен интерфейс с базами данных.

---

## 📦 Стек технологий

- Python 3.10
- Django 5.2.4
- PostgreSQL 14
- Docker / Docker Compose
- python-dotenv 1.1.1
---

## 🚀 Запуск
### 1. Клонируй репозиторий и перейди в директорию

```bash
git clone https://github.com/Solva-technology/solva-notes-models-toqsyn.git
cd db_django
```
2. Создай .env файл в корне проекта:
```bash
POSTGRES_DB=notes_db
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
DB_HOST=db
DB_PORT=5432
DJANGO_SECRET_KEY = 'django-insecure-gx=r9g%%7_lb11*a@j5z3&z(!*)&q($5vax77k-fw2!rq97j3m'


LANGUAGE_CODE=ru
TIME_ZONE=Asia/Almaty
```
3. Построй и запусти проект
```bash
docker-compose up -d --build
```
После запуска:

Главная страница доступен по адресу: http://localhost:8000
Пользователи: http://localhost:8000/users/
Информаця про пользователя(вместо 1 пишите id): http://localhost:8000/users/1
Детали записки(вместо 1 пишите id): http://localhost:8000/notes/1/
Панель админ: http://localhost:8000/admin

База данных PostgreSQL работает внутри контейнера db.

4. Применение миграций
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
4. Создание администратора
```bash
docker-compose exec web python manage.py createsuperuser
```
Придумайте пароль и логин
Панель администратора доступен по адресу http://localhost:8000/admin

⚙️ Структура моделей
User — имя, email

UserProfile — OneToOne с User: bio, дата рождения

Note — текст, дата создания, author (FK), status (FK), categories (M2M)

Status — имя, is_final

Category — заголовок, описание

📁 Структура проекта
```bash
db_django/
│
├── app/
│   ├── apps.py
│   ├── models.py
│   └── constants.py
│
├── db_django/
│   └── settings.py
│
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── .gitignore
```
📌
Все параметры подключения к БД читаются из .env через os.getenv() в settings.py.

Author: Arsen Toksyn
Github: github.com/toqsyn
