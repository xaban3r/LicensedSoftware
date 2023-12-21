import sys

from PySide2 import QtCore

from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from database import db
from form import Ui_MainWindow
from widgets import StreetWidget, CityWidget, StreetTypeWidget, CityTypeWidget, AddressWidget, SoftwareWidget, \
    OrganizationWidget, DivisionWidget, SellerWidget, PCWidget
from values import tables, tables_queries, reports


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
        self.ui.add_street_pushButton.clicked.connect(self.open_widget)
        self.ui.add_city_pushButton.clicked.connect(self.open_widget)
        self.ui.add_type_street_pushButton.clicked.connect(self.open_widget)
        self.ui.add_type_city_pushButton.clicked.connect(self.open_widget)
        self.ui.add_address_pushButton.clicked.connect(self.open_widget)
        self.ui.add_software_pushButton.clicked.connect(self.open_widget)
        self.ui.add_organization_pushButton.clicked.connect(self.open_widget)
        self.ui.add_division_pushButton.clicked.connect(self.open_widget)
        self.ui.add_seller_pushButton.clicked.connect(self.open_widget)
        self.ui.add_pc_pushButton.clicked.connect(self.open_widget)
        self.ui.reports_comboBox.activated.connect(self.report_selecting)
        self.show()

    def open_widget(self):
        button_text = self.sender().text()
        if button_text == "Добавить улицу":
            new_widget = StreetWidget(self)
            new_widget.setWindowTitle('Добавить улицу')
        elif button_text == "Добавить тип улицы":
            new_widget = StreetTypeWidget(self)
            new_widget.setWindowTitle('Добавить тип улицы')
        elif button_text == "Добавить нас. пункт":
            new_widget = CityWidget(self)
            new_widget.setWindowTitle('Добавить нас. пункт')
        elif button_text == "Добавить тип нас. пункта":
            new_widget = CityTypeWidget(self)
            new_widget.setWindowTitle('Добавить тип нас. пункта')
        elif button_text == "Добавить адрес":
            new_widget = AddressWidget(self)
            new_widget.setWindowTitle('Добавить адрес')
        elif button_text == "Добавить ПО":
            new_widget = SoftwareWidget(self)
            new_widget.setWindowTitle('Добавить ПО')
        elif button_text == "Добавить организацию":
            new_widget = OrganizationWidget(self)
            new_widget.setWindowTitle('Добавить Организацию')
        elif button_text == "Добавить отдел":
            new_widget = DivisionWidget(self)
            new_widget.setWindowTitle('Добавить Отдел')
        elif button_text == "Добавить продавца":
            new_widget = SellerWidget(self)
            new_widget.setWindowTitle('Добавить Продавца')
        elif button_text == "Добавить компьютер":
            new_widget = PCWidget(self)
            new_widget.setWindowTitle('Добавить Компьютер')
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

    def report_selecting(self):
        query = reports[self.ui.reports_comboBox.currentText()]
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
