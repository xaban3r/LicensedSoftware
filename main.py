from db import Database

db = Database()
db.connect()


# Обработчик кнопки
def on_button_click():
    query = "SELECT * FROM table"
    db.execute(query)
    rows = db.cur.fetchall()
    # обрабатываем результат запроса


# Закрываем соединение с базой данных при выходе из приложения
def on_app_exit():
    db.close()
