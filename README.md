DjangoSong Project

Описание проекта

DjangoSong — это веб-приложение, разработанное на Django, которое позволяет управлять информацией о песнях, а также отображать детальную информацию о каждой песне через веб-интерфейс. Проект включает в себя базу данных, шаблоны, маршруты и представления для работы с музыкальными данными.

Основные функции

Просмотр информации о песнях.

Использование шаблонов для отображения страниц.

Управление медиафайлами, включая добавление и отображение видео.

Детализированный просмотр каждой песни.

Установка и настройка

1. Клонирование репозитория

Склонируйте проект на локальный компьютер:

git clone <ссылка-на-репозиторий>
cd djangosong

2. Создание виртуального окружения

Создайте и активируйте виртуальное окружение Python:

python -m venv venv
source venv/bin/activate # Для Linux/MacOS
venv\Scripts\activate  # Для Windows

3. Установка зависимостей

Установите все зависимости из файла requirements.txt:

pip install -r requirements.txt

4. Применение миграций базы данных

Примените миграции к базе данных:

python manage.py makemigrations
python manage.py migrate

5. Создание суперпользователя

Создайте суперпользователя для доступа к админ-панели:

python manage.py createsuperuser

6. Запуск сервера разработки

Запустите сервер разработки:

python manage.py runserver

Перейдите в браузере по адресу http://127.0.0.1:8000.

Структура проекта

djangosong/
├── djangosong/
│   ├── __init__.py
│   ├── settings.py      # Конфигурация проекта
│   ├── urls.py          # Маршруты проекта
│   ├── wsgi.py          # Точка входа для WSGI
│   └── asgi.py          # Точка входа для ASGI
├── music/
│   ├── migrations/      # Миграции базы данных
│   ├── templates/       # Шаблоны HTML
│   │   └── djangosong/
│   │       └── base_generic.html  # Главный шаблон
│   ├── views.py         # Логика представлений
│   ├── urls.py          # Маршруты приложения
│   ├── models.py        # Модели базы данных
│   └── admin.py         # Админ-панель
├── db.sqlite3           # База данных
├── manage.py            # Управление проектом
└── requirements.txt     # Список зависимостей

Решение ошибок

Ошибка TemplateDoesNotExist

Убедитесь, что шаблон base_generic.html находится по пути music/templates/djangosong/base_generic.html.

Проверьте, что настройка TEMPLATES в файле settings.py указана корректно:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'music', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

Отсутствие миграций

Если возникают проблемы с миграцией, выполните:
