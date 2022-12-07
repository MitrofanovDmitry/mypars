import sqlite3
import requests
from bs4 import BeautifulSoup

# Устанавливаем прокси-сервер
proxy = {'http': 'http://user:password@proxy_server:port'}

# Отправляем HTTP-запрос к LinkedIn с использованием прокси-сервера
response = requests.get('https://www.linkedin.com/', proxies=proxy)

# Извлекаем данные с веб-страницы с помощью библиотеки bs4
soup = BeautifulSoup(response.text, 'html.parser')

# Обрабатываем данные и извлекаем необходимую информацию
for user in soup.find_all('div', class_='user'):
    print(user.get_text())
# Импортируем необходимые библиотеки
import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('linkedin.db')
cursor = conn.cursor()

# Создаем таблицу для хранения данных
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        job_title TEXT,
        company TEXT,
        location TEXT
    )
''')

# Извлекаем данные из парсера и сохраняем их в базе данных
for user in users:
    cursor.execute('''
        INSERT INTO users (name, job_title, company, location)
        VALUES (?, ?, ?, ?)
    ''', (user['name'], user['job_title'], user['company'], user['location']))

# Сохраняем изменения в базе данных
conn.
