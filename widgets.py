from PySide2.QtWidgets import QDialog
from PySide2.QtUiTools import loadUiType

Ui_street, _ = loadUiType('street_window.ui')


class StreetWidget(QDialog, Ui_street):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Настраиваем действия для кнопки сохранения
    def save_data(self):
        # Здесь вы можете добавить код для сохранения данных из виджета
        pass
