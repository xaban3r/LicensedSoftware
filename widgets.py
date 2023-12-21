from PySide2.QtWidgets import QDialog
from PySide2.QtUiTools import loadUiType

from database import db

Ui_street, _ = loadUiType('street_window.ui')
Ui_type_street, _ = loadUiType('street_type.ui')
Ui_address, _ = loadUiType('address.ui')
Ui_software, _ = loadUiType('software.ui')
Ui_organization, _ = loadUiType('organization.ui')
Ui_seller, _ = loadUiType('seller.ui')
Ui_pc, _ = loadUiType('PC.ui')


class StreetWidget(QDialog, Ui_street):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        query = "SELECT type_street FROM StreetTypes;"
        db.execute(query)
        types = [row[0] for row in db.cur.fetchall()]
        self.comboBox.addItems(sorted(types))
        self.pushButton.clicked.connect(self.save_data)

    def save_data(self):
        street = self.lineEdit.text()
        street_type = str(self.comboBox.currentText())
        print(street_type)
        query = f"INSERT INTO Streets (street, street_type) VALUES ('{street}', '{street_type}')"
        db.execute(query)
        db.conn.commit()


class CityWidget(QDialog, Ui_street):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label.setText("Название нас. пункта")
        self.label_2.setText("Тип нас. пункта")

        query = "SELECT type_city FROM CityTypes;"
        db.execute(query)
        types = [row[0] for row in db.cur.fetchall()]
        self.comboBox.addItems(sorted(types))
        self.pushButton.clicked.connect(self.save_data)
        # Настраиваем действия для кнопки сохранения

    def save_data(self):
        city = self.lineEdit.text()
        city_type = str(self.comboBox.currentText())
        query = f"INSERT INTO Cities (city, city_type) VALUES ('{city}', '{city_type}')"
        db.execute(query)
        db.conn.commit()


class StreetTypeWidget(QDialog, Ui_type_street):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save_data)
        # Настраиваем действия для кнопки сохранения

    def save_data(self):
        # Здесь вы можете добавить код для сохранения данных из виджета
        street_type = self.lineEdit.text()
        query = f"INSERT INTO StreetTypes (type_street) VALUES ('{street_type}')"
        db.execute(query)
        db.conn.commit()


class CityTypeWidget(QDialog, Ui_type_street):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label.setText("Название типа нас. пункта")
        # Настраиваем действия для кнопки сохранения
        self.pushButton.clicked.connect(self.save_data)

    def save_data(self):
        city_type = self.lineEdit.text()
        query = f"INSERT INTO CityTypes (type_city) VALUES ('{city_type}')"
        db.execute(query)
        db.conn.commit()


class AddressWidget(QDialog, Ui_address):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        query = "SELECT type_street FROM StreetTypes;"
        db.execute(query)
        types = [row[0] for row in db.cur.fetchall()]
        self.type_street_comboBox.addItems(sorted(types))

        query = "SELECT street FROM Streets;"
        db.execute(query)
        streets = [row[0] for row in db.cur.fetchall()]
        self.street_comboBox.addItems(sorted(streets))

        query = "SELECT type_city FROM CityTypes;"
        db.execute(query)
        types = [row[0] for row in db.cur.fetchall()]
        self.type_city_comboBox.addItems(sorted(types))

        query = "SELECT city FROM Cities;"
        db.execute(query)
        cities = [row[0] for row in db.cur.fetchall()]
        self.city_comboBox.addItems(sorted(cities))

        self.save_pushButton.clicked.connect(self.save_data)
        # Настраиваем действия для кнопки сохранения

    def save_data(self):
        house_number = self.number_house_lineEdit.text()
        street = str(self.street_comboBox.currentText())
        type_street = str(self.type_street_comboBox.currentText())
        city = str(self.city_comboBox.currentText())
        city_type = str(self.type_city_comboBox.currentText())
        query = f"""INSERT INTO Addresses (house_number, street_name, street_type, city_name, city_type)
                    VALUES 
                      ('{house_number}', '{street}', '{type_street}', '{city}', '{city_type}');"""
        db.execute(query)
        db.conn.commit()


class SoftwareWidget(QDialog, Ui_software):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        query = "SELECT type_name FROM SoftwareType;"
        db.execute(query)
        types = [row[0] for row in db.cur.fetchall()]
        self.type_software_comboBox.addItems(sorted(types))

        query = "SELECT firm_name FROM Firm;"
        db.execute(query)
        firms = [row[0] for row in db.cur.fetchall()]
        self.firm_comboBox.addItems(sorted(firms))

        query = "SELECT name_seller FROM seller;"
        db.execute(query)
        sellers = [row[0] for row in db.cur.fetchall()]
        self.seller_comboBox.addItems(sorted(sellers))

        self.save_pushButton.clicked.connect(self.save_data)
        # Настраиваем действия для кнопки сохранения

    def save_data(self):
        software_name = self.software_name_lineEdit.text()
        validity_period = self.validate_period_lineEdit.text()
        cost = self.cost_lineEdit.text()
        software_type = str(self.type_software_comboBox.currentText())
        firm = str(self.firm_comboBox.currentText())
        name_seller = str(self.seller_comboBox.currentText())
        query = f"""INSERT INTO Software (software_name, validity_period, cost, software_type, firm, name_seller)
                    VALUES ('{software_name}', '{validity_period}', {cost}, '{software_type}', '{firm}', '{name_seller}');
                """
        # VALUES ('Название программы', '30 days', 99.99, 'Тип программы', 'Название фирмы', 'Имя продавца');
        db.execute(query)
        db.conn.commit()


class OrganizationWidget(QDialog, Ui_organization):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.save_pushButton.clicked.connect(self.save_data)
        # Настраиваем действия для кнопки сохранения

    def save_data(self):
        # Здесь вы можете добавить код для сохранения данных из виджета
        name_organization = self.name_lineEdit.text()
        shortname_organization = self.shortname_lineEdit.text()
        query = f"""INSERT INTO Organizations (name_organization, shortname_organization)
                            VALUES 
                              ('{name_organization}', '{shortname_organization}');"""
        db.execute(query)
        db.conn.commit()


class DivisionWidget(QDialog, Ui_street):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label.setText("Название отдела")
        self.label_2.setText("Название организации")
        # Настраиваем действия для кнопки сохранения
        query = "SELECT name_organization FROM Organizations;"
        db.execute(query)
        organizations = [row[0] for row in db.cur.fetchall()]
        self.comboBox.addItems(sorted(organizations))
        self.pushButton.clicked.connect(self.save_data)

    def save_data(self):
        # Здесь вы можете добавить код для сохранения данных из виджета
        division = self.lineEdit.text()
        organization = str(self.comboBox.currentText())
        query = (f"INSERT INTO Division (name_organization, name_organization_division) VALUES ('{organization}',"
                 f" '{division}')")
        db.execute(query)
        db.conn.commit()


class SellerWidget(QDialog, Ui_seller):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        query = "SELECT id_address FROM Addresses;"
        db.execute(query)
        addresses_id = [row[0] for row in db.cur.fetchall()]
        self.comboBox.addItems(sorted(addresses_id))

        self.save_pushButton.clicked.connect(self.save_data)
        # Настраиваем действия для кнопки сохранения

    def save_data(self):
        name_seller = self.name_lineEdit.text()
        telephone_number = self.telephone_lineEdit.text()
        site_name = self.site_lineEdit.text()
        seller_address_id = str(self.comboBox.currentText())
        query = (f"""
                    INSERT INTO Seller (name_seller, telephone_number, site_name, seller_address_id)
                    VALUES ('{name_seller}', '{telephone_number}', '{site_name}', '{seller_address_id}');""")
        db.execute(query)
        db.conn.commit()


class PCWidget(QDialog, Ui_pc):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        query = "SELECT software_name FROM Software;"
        db.execute(query)
        softwares = [row[0] for row in db.cur.fetchall()]
        self.software_comboBox.addItems(sorted(softwares))

        query = "SELECT name_organization_division FROM Division;"
        db.execute(query)
        divisions = [row[0] for row in db.cur.fetchall()]
        self.division_comboBox.addItems(sorted(divisions))

        self.save_pushButton.clicked.connect(self.save_data)
        # Настраиваем действия для кнопки сохранения

    def save_data(self):
        # Здесь вы можете добавить код для сохранения данных из виджета
        inventory_number = self.inv_number_lineEdit.text()
        computer_type = self.type_lineEdit.text()
        date_start = self.date_start_lineEdit.text()
        date_end = self.date_end_lineEdit.text()
        document_number = self.doc_number_lineEdit.text()
        document_date = self.date_doc_lineEdit.text()
        software = str(self.software_comboBox.currentText())
        computer_division = str(self.division_comboBox.currentText())

        query = (f"""
                     INSERT INTO Computers (inventory_number, computer_type, date_start, date_end, document_number,
                         document_date, software, computer_division)
                     VALUES ({inventory_number}, '{computer_type}', '{date_start}', '{date_end}', {document_number}, 
                     '{document_date}', '{software}', '{computer_division}');
""")
        # VALUES (12345, 'station', '2023-01-01', '2023-12-31', 9876, '2023-01-05', 'Название программы',
        #                             'Название дивизиона');
        db.execute(query)
        db.conn.commit()
