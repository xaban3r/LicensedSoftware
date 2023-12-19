import sys

from db import Database
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from form import Ui_MainWindow

db = Database()
db.connect()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Учёт лицензионного ПО")
        combobox_style = "QComboBox { font-weight: bold; text-align: center; font-size: 16px; }"
        self.ui.tables_comboBox.addItems(
            ["Организации", "Подразделения", "Компьютеры", "ПО", "Продавец", "Адреса"])
        self.ui.reports_comboBox.addItems(
            ["Список подразделений с нелицензионным ПО", "Список ПО", "Список подразделений"])
        self.ui.tables_comboBox.setStyleSheet(combobox_style)
        self.ui.reports_comboBox.setStyleSheet(combobox_style)
        self.show()

    def show_table(self, rows):
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(len(rows[0]))

        # Заполняем таблицу данными
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                self.ui.tableWidget.setItem(i, j, item)


# Обработчик кнопки
# def on_button_click():
#     query = "SELECT * FROM table"
#     db.execute(query)
#     rows = db.cur.fetchall()


def on_app_exit():
    db.close()


if __name__ == "__main__":
    app = QApplication()
    widget = MainWindow()
    widget.show()
    app.aboutToQuit.connect(on_app_exit)
    sys.exit(app.exec_())
