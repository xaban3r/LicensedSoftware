import sys

from PySide2 import QtCore

from db import Database
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from form import Ui_MainWindow
from widgets import StreetWidget
from values import tables, tables_queries

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
            ["", "Организации", "Подразделения", "Компьютеры", "ПО", "Продавцы", "Адреса"])
        self.ui.reports_comboBox.addItems(
            ["", "Список подразделений с нелицензионным ПО", "Список ПО", "Список подразделений"])
        self.ui.tables_comboBox.setStyleSheet(combobox_style)
        self.ui.reports_comboBox.setStyleSheet(combobox_style)
        self.ui.tables_comboBox.activated.connect(self.table_selecting)
        self.ui.add_street_pushButton.clicked.connect(self.open_street_widget)
        self.show()

    def open_street_widget(self):
        button_text = self.sender().text()
        if button_text == "Добавить улицу":
            new_widget = StreetWidget(self)
            new_widget.setWindowTitle('Добавить улицу')
        elif button_text == "Добавить тип улицы":
            pass
        elif button_text == "Добавить нас. пункт":
            pass
        elif button_text == "Добавить тип нас. пункт":
            pass
        elif button_text == "Добавить адрес":
            pass
        elif button_text == "Добавить ПО":
            pass
        elif button_text == "Добавить организацию":
            pass
        elif button_text == "Добавить отдел":
            pass
        elif button_text == "Добавить продавца":
            pass
        elif button_text == "Добавить компьютер":
            pass
        # Делаем окно модальным и отображаем его
        new_widget.setModal(True)
        new_widget.exec_()

    def show_table(self, rows, attributes):
        num_rows = len(rows)
        num_cols = len(rows[0]) if num_rows > 0 else 0
        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget.setRowCount(num_rows + 1)
        self.ui.tableWidget.setColumnCount(num_cols + 1)
        # Заполняем таблицу данными
        for i in range(num_rows):
            # Вставляем номер строки
            item = QTableWidgetItem(str(i + 1))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(i + 1, 0, item)

            for j in range(num_cols):
                # Вставляем имя столбца
                if i == 0:
                    item = QTableWidgetItem(str(j + 1))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(0, j + 1, item)

                # Вставляем данные
                item = QTableWidgetItem(str(rows[i][j]))
                self.ui.tableWidget.setItem(i + 1, j + 1, item)
        # Если таблица пустая, вставляем заголовки
        if num_rows == 0:
            item = QTableWidgetItem("No data")
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(1, 1, item)
        else:
            # Вставляем заголовок для номеров строк
            item = QTableWidgetItem("#")
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(0, 0, item)

            # Вставляем заголовки для имен столбцов
            for j in range(num_cols):
                item = QTableWidgetItem(attributes[j])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(0, j + 1, item)

        self.ui.tableWidget.resizeColumnsToContents()

    def table_selecting(self):
        table = tables[self.ui.tables_comboBox.currentText()]
        query = tables_queries[table]
        db.execute(query)

        rows = db.cur.fetchall()
        attributes = [desc[0] for desc in db.cur.description]
        self.show_table(rows, attributes)


def on_app_exit():
    db.close()


if __name__ == "__main__":
    app = QApplication()
    widget = MainWindow()
    widget.show()
    app.aboutToQuit.connect(on_app_exit)
    sys.exit(app.exec_())
