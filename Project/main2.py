import sys

import pymysql
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QVBoxLayout, QMessageBox
)
from PySide6.QtGui import QStandardItemModel, QStandardItem

from f1 import Ui_Form

from PyQt6.QtWidgets import QMainWindow
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'autosalon',
    'charset': 'utf8mb4'
}

class AvtoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Просмотр автомобилей")
        self.load_avto()
        self.ui.pushButton.clicked.connect(self.filtracia)
        self.ui.pushButton_2.clicked.connect(self.load_avto)

    def filtracia(self):
        p = self.ui.lineEdit.text()
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT automobile.id as Номер, Cvet.Nazvanie as Цвет, Marka.Nazvanie AS "
            "Название, Model AS Модель, Obiem_dvigatelya AS Объём_двигателя, "
            "Complectacia AS Комплектация, Stoimost AS Стоимость,"
            " Foto AS Фото FROM automobile INNER JOIN Marka ON Marka.id = "
            "automobile.Marka INNER JOIN Cvet ON Cvet.id = automobile.Cvet WHERE model LIKE '%"+p+"%'")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        # Создаём модель
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(column_names)

        # Заполняем модель данными
        for row_data in rows:
            items = []
            for cell in row_data:
                item = QStandardItem(str(cell) if cell is not None else "")
                item.setEditable(False)  # делаем ячейки только для чтения
                items.append(item)
            model.appendRow(items)

        # Привязываем модель к tableView
        self.ui.tableView.setModel(model)

        # Опционально: подгоняем ширину столбцов
        self.ui.tableView.resizeColumnsToContents()

    def load_avto(self):
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT automobile.id as Номер, Cvet.Nazvanie as Цвет, Marka.Nazvanie AS Название, Model AS Модель, Obiem_dvigatelya AS Объём_двигателя, Complectacia AS Комплектация, Stoimost AS Стоимость, Foto AS Фото FROM automobile INNER JOIN Marka ON Marka.id = automobile.Marka INNER JOIN Cvet ON Cvet.id = automobile.Cvet")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        # Создаём модель
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(column_names)

        # Заполняем модель данными
        for row_data in rows:
            items = []
            for cell in row_data:
                item = QStandardItem(str(cell) if cell is not None else "")
                item.setEditable(False)  # делаем ячейки только для чтения
                items.append(item)
            model.appendRow(items)

        # Привязываем модель к tableView
        self.ui.tableView.setModel(model)

        # Опционально: подгоняем ширину столбцов
        self.ui.tableView.resizeColumnsToContents()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AvtoForm()
    window.show()
    sys.exit(app.exec())