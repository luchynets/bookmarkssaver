# 📑 Bookmark Manager API v1.0

Сучасний веб-додаток для збереження та організації ваших закладок. Побудований на **FastAPI**, **PostgreSQL** та чистому **JavaScript**.



## 🚀 Особливості
- **Повний CRUD:** Додавання та перегляд закладок через зручний інтерфейс.
- **Організація:** Створення власних категорій для закладок.
- **Динамічна фільтрація:** Перегляд закладок за категоріями без перезавантаження сторінки.
- **Modern UI:** Темна тема, адаптивна сітка карт та модальні вікна.
- **Асинхронність:** Швидка взаємодія з API через `fetch`.

## 🛠 Технологічний стек
- **Backend:** Python 3.10+, FastAPI, Uvicorn.
- **Database:** PostgreSQL, Psycopg2.
- **Frontend:** HTML5, CSS3 (Flexbox/Grid), Vanilla JavaScript.



## 📦 Встановлення та запуск

### 1. Клонування репозиторію
```bash
git clone [https://github.com/luchynets/bookmarkssaver.git](https://github.com/luchynets/bookmarkssaver.git)
cd bookmarkssaver
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```
# Приклад підключення
```bash
self.conn = psycopg2.connect(
    dbname="bookmarks_db",
    user="postgres",
    password="your_password",
    host="localhost"
)
```

```bash
uvicorn main:app --reload
```

## 📡 API Ендпоінти
| Метод | Шлях | Опис |
| :--- | :--- | :--- |
| `GET` | `/bookmarks` | Отримати всі закладки |
| `GET` | `/categories` | Список всіх категорій |
| `POST` | `/addbookmark` | Додати нову закладку |
| `POST` | `/addcategory` | Додати нову категорію |

## 📝 Майбутні оновлення
- **Видалення та редагування закладок.**
- **Авторизація користувачів (OAuth2).**
- **Пошук за назвою закладки.**
