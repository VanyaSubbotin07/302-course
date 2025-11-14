import sys
import pymysql
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QVBoxLayout, QMessageBox
)

from PySide6.QtWidgets import (
    QWidget, QLabel, QTableView, QVBoxLayout, QHBoxLayout, QHeaderView,
    QMessageBox, QPushButton, QComboBox, QLineEdit, QFormLayout, QDialog, QSpinBox, QDoubleSpinBox
)

from PySide6.QtWidgets import (
    QWidget, QLabel, QTableView, QVBoxLayout, QHBoxLayout, QHeaderView, QInputDialog,
    QMessageBox, QPushButton
)

from PySide6.QtGui import QFont
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout
)

from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt
from f1 import Ui_Form
from f2 import Ui_Form2


AUTO_SALON_STYLE = """
QWidget {
    background-color: #fafafa;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 14px;
}

QLabel {
    color: #1a1a1a;
    font-weight: bold;
}

QLineEdit, QComboBox, QDateEdit {
    border: 2px solid #d0d0d0;
    border-radius: 10px;
    padding: 8px;
    background: white;
}

QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
    border: 2px solid #c00000;
}

QPushButton {
    font-weight: bold;
    border: none;
    border-radius: 12px;
    color: white;
    padding: 12px;
    font-size: 15px;
}

QPushButton#btn-primary {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #d32f2f, stop:1 #b71c1c);
}

QPushButton#btn-primary:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #f44336, stop:1 #c62828);
}

QPushButton#btn-secondary {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #607d8b, stop:1 #455a64);
}

QPushButton#btn-secondary:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78909c, stop:1 #546e7a);
}

QPushButton#pushButton, QPushButton#button_login {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #d32f2f, stop:1 #b71c1c);
}

QPushButton#pushButton:hover, QPushButton#button_login:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #f44336, stop:1 #c62828);
}

QPushButton#pushButton_2, QPushButton#pushButton_3,
QPushButton#button_registration,
QPushButton#button_check_avtomobile,
QPushButton#button_exit {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #607d8b, stop:1 #455a64);
}

QPushButton#pushButton_2:hover,
QPushButton#pushButton_3:hover,
QPushButton#button_registration:hover,
QPushButton#button_check_avtomobile:hover,
QPushButton#button_exit:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78909c, stop:1 #546e7a);
}

QTableView {
    border: 1px solid #ccc;
    gridline-color: #ddd;
    selection-background-color: #ffebee;
    selection-color: #c00000;
}

QHeaderView::section {
    background-color: #f5f5f5;
    padding: 6px;
    border: 1px solid #ddd;
    font-weight: bold;
    color: #333;
}

QMessageBox {
    background-color: #ffffff;
}

QMessageBox QLabel {
    color: #1a1a1a;
    font-weight: normal;
}

QMessageBox QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #607d8b, stop:1 #455a64);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: bold;
    min-width: 80px;
}

QMessageBox QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78909c, stop:1 #546e7a);
}

QMessageBox QPushButton:default {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #d32f2f, stop:1 #b71c1c);
}

QMessageBox QPushButton:default:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #f44336, stop:1 #c62828);
}

QInputDialog {
    background: white;
}

QInputDialog QPushButton {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: bold;
}

QInputDialog QPushButton:hover {
    background-color: #45a049;
}

QInputDialog QPushButton:pressed {
    background-color: #3d8b40;
}

/* Стили для кнопок */
QPushButton {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: bold;
    min-height: 35px;
}

QPushButton:hover {
    background-color: #45a049;
}

QPushButton:pressed {
    background-color: #3d8b40;
}

/* === ВАЖНО: стили для кнопок в диалогах === */
QMessageBox QPushButton,
QInputDialog QPushButton,
QDialog QPushButton {
    background-color: #2196F3;
    color: white;
    border: none;
    padding: 6px 12px;
    border-radius: 4px;
    min-height: 30px;
    min-width: 80px;
}

QMessageBox QPushButton:hover,
QInputDialog QPushButton:hover,
QDialog QPushButton:hover {
    background-color: #1976D2;
}

QMessageBox QPushButton:pressed,
QInputDialog QPushButton:pressed,
QDialog QPushButton:pressed {
    background-color: #1565C0;
}

QMessageBox QPushButton {
        background-color: #4CAF50;
        color: white;
        border-radius: 6px;
        padding: 6px 16px;
    }

"""

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'autosalon'
}

class AddStaffForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Автоцентр — Управление сотрудниками")
        self.setFixedSize(400, 550)
        self.setWindowIcon(QIcon(str("Icon.png")))
        self.doljnosti = []
        self.init_ui()
        self.setStyleSheet(AUTO_SALON_STYLE)
        self.load_doljnosti()

    def init_ui(self):
        layout = QVBoxLayout()
        title = QLabel("Добавить нового сотрудника")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()

        self.fio_input = QLineEdit()
        self.login_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.doljnost_combo = QComboBox()
        self.doljnost_combo.setFixedHeight(35)

        form_layout.addRow("ФИО (через пробел):", self.fio_input)
        form_layout.addRow("Логин:", self.login_input)
        form_layout.addRow("Пароль:", self.password_input)
        form_layout.addRow("Должность:", self.doljnost_combo)

        layout.addLayout(form_layout)

        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Добавить сотрудника")
        self.add_btn.clicked.connect(self.add_staff)
        self.cancel_btn = QPushButton("Отмена")
        self.cancel_btn.clicked.connect(self.on_cancel)

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def on_cancel(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()
    def load_doljnosti(self):
        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()
            cur.execute("SELECT ID, Dolzhnost FROM Dolzhnosti")
            self.doljnosti = cur.fetchall()
            conn.close()

            self.doljnost_combo.clear()
            for id_, name in self.doljnosti:
                self.doljnost_combo.addItem(name, id_)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить должности:\n{e}")

    def add_staff(self):
        fio = self.fio_input.text().strip()
        login = self.login_input.text().strip()
        password = self.password_input.text().strip()
        doljnost_id = self.doljnost_combo.currentData()

        if not fio or not login or not password or doljnost_id is None:
            QMessageBox.warning(self, "Ошибка", "Все поля обязательны.")
            return

        parts = fio.split()
        if len(parts) < 3:
            QMessageBox.warning(self, "Ошибка", "Введите ФИО в формате: Фамилия Имя Отчество")
            return

        fam, im, ot = parts[0], parts[1], " ".join(parts[2:])

        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()

            cur.execute("SELECT ID FROM Sotrudnik WHERE login = %s", (login,))
            if cur.fetchone():
                QMessageBox.warning(self, "Ошибка", "Сотрудник с таким логином уже существует!")
                conn.close()
                return

            cur.execute("SELECT MAX(ID) FROM Sotrudnik")
            max_id = cur.fetchone()[0]
            new_id = 1 if max_id is None else max_id + 1

            cur.execute("""
                INSERT INTO Sotrudnik (ID, Familia, Imya, Otchestvo, login, pass, Dolzhnost)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (new_id, fam, im, ot, login, password, doljnost_id))

            conn.commit()
            conn.close()

            QMessageBox.information(self, "Успех", "Сотрудник успешно добавлен!")
            self.fio_input.clear()
            self.login_input.clear()
            self.password_input.clear()
            self.doljnost_combo.setCurrentIndex(0)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить сотрудника:\n{e}")

class StaffCabinetForm(QWidget):
    def __init__(self, staff_fio):
        super().__init__()
        self.staff_fio = staff_fio
        self.setWindowTitle("Автоцентр — Кабинет сотрудника")
        self.setWindowIcon(QIcon(str("Icon.png")))
        self.resize(1000, 700)
        self.setStyleSheet(AUTO_SALON_STYLE)
        self.marka_list = []
        self.cvet_list = []
        self.init_ui()
        self.load_filters()
        self.load_cars()

    def init_ui(self):
        self.title_label = QLabel(f"Кабинет сотрудника: {self.staff_fio}")
        self.title_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #c00000; margin: 10px;")

        filter_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск по модели...")
        self.search_input.setFixedHeight(40)

        self.marka_combo = QComboBox()
        self.marka_combo.setFixedHeight(40)
        self.marka_combo.addItem("Все марки", -1)

        self.cvet_combo = QComboBox()
        self.cvet_combo.setFixedHeight(40)
        self.cvet_combo.addItem("Все цвета", -1)

        self.btn_search = QPushButton("Найти")
        self.btn_search.setObjectName("btn-primary")
        self.btn_search.setFixedHeight(40)
        self.btn_search.clicked.connect(self.load_cars)

        self.btn_reset = QPushButton("Сброс")
        self.btn_reset.setObjectName("btn-secondary")
        self.btn_reset.setFixedHeight(40)
        self.btn_reset.clicked.connect(self.reset_filters)

        filter_layout.addWidget(QLabel("Модель:"))
        filter_layout.addWidget(self.search_input, 2)
        filter_layout.addWidget(QLabel("Марка:"))
        filter_layout.addWidget(self.marka_combo, 1)
        filter_layout.addWidget(QLabel("Цвет:"))
        filter_layout.addWidget(self.cvet_combo, 1)
        filter_layout.addWidget(self.btn_search)
        filter_layout.addWidget(self.btn_reset)

        self.table_view = QTableView()
        self.table_view.setAlternatingRowColors(True)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSelectionMode(QTableView.SingleSelection)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Добавить авто")
        self.btn_add.setObjectName("btn-primary")
        self.btn_add.setFixedHeight(40)
        self.btn_add.clicked.connect(self.add_car)

        self.btn_edit = QPushButton("Редактировать")
        self.btn_edit.setObjectName("btn-secondary")
        self.btn_edit.setFixedHeight(40)
        self.btn_edit.clicked.connect(self.edit_car)

        self.btn_delete = QPushButton("Удалить")
        self.btn_delete.setObjectName("btn-secondary")
        self.btn_delete.setFixedHeight(40)
        self.btn_delete.clicked.connect(self.delete_car)

        self.btn_sell = QPushButton("Оформить продажу")
        self.btn_sell.setObjectName("btn-primary")
        self.btn_sell.setFixedHeight(40)
        self.btn_sell.clicked.connect(self.sell_car)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(40)
        self.back_button.setStyleSheet("""
                    QPushButton {
                        background: #607d8b;
                        color: white;
                        border-radius: 8px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background: #78909c;
                    }
                """)
        self.back_button.clicked.connect(self.on_cancel)

        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_sell)
        btn_layout.addWidget(self.back_button)
        btn_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(filter_layout)
        main_layout.addWidget(self.table_view)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def on_cancel(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()

    def sell_car(self):
        car_id = self.get_selected_car_id()
        if car_id is None:
            return

        client_id, ok = QInputDialog.getText(
            self,
            "Оформление продажи",
            "Введите ID клиента:"
        )

        if not ok or not client_id.strip():
            return

        if not client_id.strip().isdigit():
            QMessageBox.warning(self, "Ошибка", "ID клиента должен быть целым числом.")
            return

        client_id = int(client_id.strip())

        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()

            cur.execute("SELECT ID FROM Client WHERE ID = %s", (client_id,))
            if not cur.fetchone():
                QMessageBox.warning(self, "Ошибка", "Клиент с таким ID не найден.")
                conn.close()
                return

            cur.execute("SELECT MAX(ID) FROM prodazhi_automobiley")
            max_id = cur.fetchone()[0]
            new_id = 1 if max_id is None else max_id + 1

            cur.execute("""
                        INSERT INTO prodazhi_automobiley (ID, ID_clienta, ID_automobilya, Data_prodazhi)
                        VALUES (%s, %s, %s, NOW())
                    """, (new_id, client_id, car_id))

            conn.commit()
            conn.close()

            QMessageBox.information(self, "Успех", f"Продажа оформлена! Номер продажи: {new_id}")
            self.load_cars()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось оформить продажу:\n{e}")
    def load_filters(self):
        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()

            cur.execute("SELECT id, Nazvanie FROM Marka ORDER BY Nazvanie")
            self.marka_list = cur.fetchall()
            self.marka_combo.clear()
            self.marka_combo.addItem("Все марки", -1)
            for id_, name in self.marka_list:
                self.marka_combo.addItem(name, id_)

            cur.execute("SELECT id, Nazvanie FROM Cvet ORDER BY Nazvanie")
            self.cvet_list = cur.fetchall()
            self.cvet_combo.clear()
            self.cvet_combo.addItem("Все цвета", -1)
            for id_, name in self.cvet_list:
                self.cvet_combo.addItem(name, id_)

            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить фильтры:\n{e}")

    def reset_filters(self):
        self.search_input.clear()
        self.marka_combo.setCurrentIndex(0)
        self.cvet_combo.setCurrentIndex(0)
        self.load_cars()

    def load_cars(self):
        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()
            model_filter = self.search_input.text().strip()
            marka_id = self.marka_combo.currentData()
            cvet_id = self.cvet_combo.currentData()

            query = """
                SELECT 
                    a.id AS Номер,
                    m.Nazvanie AS Марка,
                    a.Model AS Модель,
                    c.Nazvanie AS Цвет,
                    a.Obiem_dvigatelya AS `Объём`,
                    a.Complectacia AS Комплектация,
                    a.Stoimost AS Стоимость
                FROM automobile a
                INNER JOIN Marka m ON a.Marka = m.id
                INNER JOIN Cvet c ON a.Cvet = c.id
                WHERE 1=1
            """
            params = []

            if model_filter:
                query += " AND a.Model LIKE %s"
                params.append(f"%{model_filter}%")
            if marka_id != -1:
                query += " AND a.Marka = %s"
                params.append(marka_id)
            if cvet_id != -1:
                query += " AND a.Cvet = %s"
                params.append(cvet_id)

            query += " ORDER BY a.id"

            cur.execute(query, params)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            conn.close()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(columns)
            for row in rows:
                items = [QStandardItem(str(cell) if cell is not None else "") for cell in row]
                for item in items:
                    item.setEditable(False)
                model.appendRow(items)

            self.table_view.setModel(model)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить автомобили:\n{e}")

    def get_selected_car_id(self):
        selection = self.table_view.selectionModel()
        if not selection.hasSelection():
            QMessageBox.warning(self, "Внимание", "Выберите автомобиль в таблице.")
            return None
        row = selection.selectedRows()[0].row()
        model = self.table_view.model()
        return int(model.index(row, 0).data())

    def add_car(self):
        dialog = CarEditDialog(self, mode="add")
        if dialog.exec():
            self.load_cars()

    def edit_car(self):
        car_id = self.get_selected_car_id()
        if car_id is not None:
            dialog = CarEditDialog(self, mode="edit", car_id=car_id)
            if dialog.exec():
                self.load_cars()

    def delete_car(self):
        car_id = self.get_selected_car_id()
        if car_id is None:
            return

        reply = QMessageBox.question(
            self, "Подтверждение",
            "Вы уверены, что хотите удалить этот автомобиль?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                conn = pymysql.connect(**DB_CONFIG)
                cur = conn.cursor()
                cur.execute("DELETE FROM automobile WHERE id = %s", (car_id,))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Успех", "Автомобиль удалён.")
                self.load_cars()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось удалить автомобиль:\n{e}")

class CarEditDialog(QDialog):
    def __init__(self, parent=None, mode="add", car_id=None):
        super().__init__(parent)
        self.mode = mode
        self.car_id = car_id
        self.setWindowTitle("Добавить автомобиль" if mode == "add" else "Редактировать автомобиль")
        self.setWindowIcon(QIcon(str("Icon.png")))
        self.setFixedSize(400, 400)
        self.setStyleSheet(AUTO_SALON_STYLE)
        self.marka_list = []
        self.cvet_list = []
        self.init_ui()
        self.load_references()
        if mode == "edit":
            self.load_car_data()

    def init_ui(self):
        layout = QFormLayout()
        layout.setSpacing(15)

        self.model_input = QLineEdit()
        self.obiem_input = QDoubleSpinBox()
        self.obiem_input.setRange(0.5, 10.0)
        self.obiem_input.setSingleStep(0.1)
        self.complect_input = QLineEdit()
        self.price_input = QSpinBox()
        self.price_input.setRange(100000, 50000000)
        self.price_input.setSingleStep(50000)

        self.marka_combo = QComboBox()
        self.cvet_combo = QComboBox()

        layout.addRow("Модель:", self.model_input)
        layout.addRow("Марка:", self.marka_combo)
        layout.addRow("Цвет:", self.cvet_combo)
        layout.addRow("Объём двигателя:", self.obiem_input)
        layout.addRow("Комплектация:", self.complect_input)
        layout.addRow("Стоимость:", self.price_input)

        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("Сохранить")
        self.save_btn.setObjectName("btn-primary")
        self.cancel_btn = QPushButton("Отмена")
        self.cancel_btn.setObjectName("btn-secondary")
        self.save_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addRow(btn_layout)

        self.setLayout(layout)

    def load_references(self):
        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()
            cur.execute("SELECT id, Nazvanie FROM Marka ORDER BY Nazvanie")
            self.marka_list = cur.fetchall()
            self.marka_combo.clear()
            for id_, name in self.marka_list:
                self.marka_combo.addItem(name, id_)

            cur.execute("SELECT id, Nazvanie FROM Cvet ORDER BY Nazvanie")
            self.cvet_list = cur.fetchall()
            self.cvet_combo.clear()
            for id_, name in self.cvet_list:
                self.cvet_combo.addItem(name, id_)

            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить справочники:\n{e}")

    def load_car_data(self):
        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()
            cur.execute("""
                SELECT Model, Marka, Cvet, Obiem_dvigatelya, Complectacia, Stoimost
                FROM automobile WHERE id = %s
            """, (self.car_id,))
            row = cur.fetchone()
            conn.close()

            if row:
                self.model_input.setText(row[0])
                self.set_combo_by_data(self.marka_combo, row[1])
                self.set_combo_by_data(self.cvet_combo, row[2])
                self.obiem_input.setValue(float(row[3]) if row[3] else 0.0)
                self.complect_input.setText(row[4] or "")
                self.price_input.setValue(int(row[5]) if row[5] else 0)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные авто:\n{e}")

    def set_combo_by_data(self, combo, target_id):
        for i in range(combo.count()):
            if combo.itemData(i) == target_id:
                combo.setCurrentIndex(i)
                break

    def accept(self):
        model = self.model_input.text().strip()
        marka_id = self.marka_combo.currentData()
        cvet_id = self.cvet_combo.currentData()
        obiem = self.obiem_input.value()
        complect = self.complect_input.text().strip()
        price = self.price_input.value()

        if not model:
            QMessageBox.warning(self, "Ошибка", "Укажите модель автомобиля.")
            return

        try:
            conn = pymysql.connect(**DB_CONFIG)
            cur = conn.cursor()
            if self.mode == "add":
                cur.execute("SELECT MAX(ID) AS max_id FROM automobile")
                result = cur.fetchone()
                max_id = result[0] if result and result[0] is not None else 0
                new_id = max_id + 1
                print(marka_id, model, cvet_id, obiem, complect, price)
                cur.execute("""
                        INSERT INTO automobile (id, Marka, Model, Cvet, Obiem_dvigatelya, Complectacia, Stoimost)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (new_id, marka_id, model, cvet_id, obiem, complect, price))

            else:
                cur.execute("""
                    UPDATE automobile 
                    SET Marka = %s, Model = %s, Cvet = %s, Obiem_dvigatelya = %s, Complectacia = %s, Stoimost = %s
                    WHERE id = %s
                """, (marka_id, model, cvet_id, obiem, complect, price, self.car_id))
            conn.commit()
            conn.close()
            super().accept()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить данные:\n{e}")

class ClientCabinetForm(QWidget):
    def __init__(self, client_id, fio):
        super().__init__()
        self.client_id = client_id
        self.fio = fio
        self.setWindowTitle("Автоцентр — Личный кабинет")
        self.setWindowIcon(QIcon("Icon.png"))
        self.setFixedSize(950, 700)
        self.setStyleSheet(AUTO_SALON_STYLE)
        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.fio_label = QLabel(f"Добро пожаловать, {self.fio}!")
        self.fio_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.fio_label.setAlignment(Qt.AlignCenter)
        self.fio_label.setStyleSheet("color: #c00000; margin: 10px;")

        self.car_purchases_label = QLabel("Ваши покупки автомобилей:")
        self.car_purchases_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.car_purchases_table = QTableView()
        self.setup_table_view(self.car_purchases_table)

        self.parts_purchases_label = QLabel("Ваши покупки комплектующих:")
        self.parts_purchases_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.parts_purchases_table = QTableView()
        self.setup_table_view(self.parts_purchases_table)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(40)
        self.back_button.setStyleSheet("""
            QPushButton {
                background: #607d8b;
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #78909c;
            }
        """)
        self.back_button.clicked.connect(self.on_cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.fio_label)

        main_layout.addWidget(self.car_purchases_label)
        main_layout.addWidget(self.car_purchases_table)

        main_layout.addWidget(self.parts_purchases_label)
        main_layout.addWidget(self.parts_purchases_table)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.back_button)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def on_cancel(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()


    def setup_table_view(self, table_view):
        table_view.setAlternatingRowColors(True)
        table_view.verticalHeader().setVisible(False)
        table_view.horizontalHeader().setStretchLastSection(True)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        table_view.setFixedHeight(200)

    def load_data(self):
        self.load_car_purchases()
        self.load_parts_purchases()

    def load_car_purchases(self):
        try:
            connection = pymysql.connect(**DB_CONFIG)
            cursor = connection.cursor()
            query = """
                SELECT 
                    prodazhi_automobiley.Data_prodazhi AS Дата_продажи,
                    automobile.Model AS Модель,
                    Cvet.Nazvanie AS Цвет,
                    Marka.Nazvanie AS Марка,
                    Obiem_dvigatelya AS Объём_двигателя,
                    Complectacia AS Комплектация,
                    Stoimost AS Стоимость
                FROM prodazhi_automobiley
                INNER JOIN Client ON Client.ID = prodazhi_automobiley.ID_clienta
                INNER JOIN automobile ON automobile.ID = prodazhi_automobiley.ID_automobilya
                INNER JOIN Marka ON Marka.id = automobile.Marka
                INNER JOIN Cvet ON Cvet.id = automobile.Cvet
                WHERE Client.ID = %s
                ORDER BY prodazhi_automobiley.Data_prodazhi DESC
            """
            cursor.execute(query, (self.client_id,))
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            connection.close()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(column_names)

            if not rows:
                model.appendRow([QStandardItem("Нет покупок автомобилей")])
                for i in range(1, len(column_names)):
                    item = QStandardItem("")
                    item.setEnabled(False)
                    model.setItem(0, i, item)
            else:
                for row_data in rows:
                    items = [QStandardItem(str(cell) if cell is not None else "") for cell in row_data]
                    for item in items:
                        item.setEditable(False)
                    model.appendRow(items)

            self.car_purchases_table.setModel(model)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить покупки автомобилей:\n{e}")

    def load_parts_purchases(self):
        try:
            connection = pymysql.connect(**DB_CONFIG)
            cursor = connection.cursor()
            query = """
                SELECT 
                    complectyushie.Nazvanie AS Название,
                    complectyushie.Model AS Модель,
                    complectyushie.Stoimost AS Стоимость,
                    sostav_prodazhi_complectyushih.Kolichestvo AS Количество,
                    prodazhi_complectyushih.Data_prodazhy AS Дата_продажи
                FROM complectyushie 
                INNER JOIN sostav_prodazhi_complectyushih 
                    ON complectyushie.ID = sostav_prodazhi_complectyushih.ID_complectyushego
                INNER JOIN prodazhi_complectyushih 
                    ON prodazhi_complectyushih.ID = sostav_prodazhi_complectyushih.ID_prodazhi
                WHERE prodazhi_complectyushih.ID_clienta = %s
                ORDER BY prodazhi_complectyushih.Data_prodazhy DESC
            """
            cursor.execute(query, (self.client_id,))
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            connection.close()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(column_names)

            if not rows:
                model.appendRow([QStandardItem("Нет покупок комплектующих")])
                for i in range(1, len(column_names)):
                    item = QStandardItem("")
                    item.setEnabled(False)
                    model.setItem(0, i, item)
            else:
                for row_data in rows:
                    items = [QStandardItem(str(cell) if cell is not None else "") for cell in row_data]
                    for item in items:
                        item.setEditable(False)
                    model.appendRow(items)

            self.parts_purchases_table.setModel(model)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить покупки комплектующих:\n{e}")

class RegForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.setWindowTitle("Автоцентр — Регистрация")
        self.setWindowIcon(QIcon(str("Icon.png")))
        self.apply_styles()
        self.setup_fields()
        self.ui.pushButton.clicked.connect(self.registration)
        self.ui.pushButton_2.clicked.connect(self.close)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #fafafa;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel {
                color: #1a1a1a;
                font-weight: bold;
            }
            QLineEdit, QDateEdit {
                border: 2px solid #d0d0d0;
                border-radius: 10px;
                padding: 8px;
                background: white;
                font-size: 14px;
            }
            QLineEdit:focus, QDateEdit:focus {
                border: 2px solid #c00000;
            }
            QPushButton {
                font-weight: bold;
                border: none;
                border-radius: 12px;
                color: white;
                font-size: 15px;
                padding: 12px;
            }
            QPushButton#pushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #d32f2f, stop:1 #b71c1c);
            }
            QPushButton#pushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #f44336, stop:1 #c62828);
            }
            QPushButton#pushButton_2 {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #607d8b, stop:1 #455a64);
            }
            QPushButton#pushButton_2:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #78909c, stop:1 #546e7a);
            }
            QMessageBox QPushButton {
        background-color: #4CAF50;
        color: white;
        border-radius: 6px;
        padding: 6px 16px;
            
        """)

    def setup_fields(self):
        self.ui.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.ui.lineEdit_6.setInputMask("+7(999)999-99-99")

        self.ui.lineEdit.setPlaceholderText("Иванов")
        self.ui.lineEdit_2.setPlaceholderText("Иван")
        self.ui.lineEdit_3.setPlaceholderText("Иванович")
        self.ui.lineEdit_4.setPlaceholderText("••••••••")
        self.ui.lineEdit_5.setPlaceholderText("••••••••")
        self.ui.lineEdit_6.setPlaceholderText("+7(999)999-99-99")

    def show_message(self, title, text, icon=QMessageBox.Information):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #ffffff;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 14px;
            }
            QMessageBox QLabel {
                color: #1a1a1a;
                min-width: 150px;
                padding: 10px;
            }
            QMessageBox QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 6px 16px;
                border-radius: 6px;
                min-width: 80px;
                font-weight: bold;
            }
            QMessageBox QPushButton:hover {
                background-color: #45a049;
            }
            QMessageBox QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        msg.exec()

    def registration(self):
        familia = self.ui.lineEdit.text().strip()
        imya = self.ui.lineEdit_2.text().strip()
        otchestvo = self.ui.lineEdit_3.text().strip()
        telephone = self.ui.lineEdit_6.text().replace("_", "").strip()
        password = self.ui.lineEdit_4.text().strip()
        password2 = self.ui.lineEdit_5.text().strip()

        if not all([familia, imya, otchestvo, telephone, password, password2]):
            self.show_message("Ошибка", "Заполнены не все поля!", QMessageBox.Warning)
            return

        if password != password2:
            self.show_message("Ошибка", "Пароли не совпадают!", QMessageBox.Warning)
            return

        if len(telephone) != 16 or "_" in telephone:
            self.show_message("Ошибка", "Пожалуйста, введите корректный номер телефона.", QMessageBox.Warning)
            return

        try:
            connection = pymysql.connect(**DB_CONFIG)
            cursor = connection.cursor()
            cursor.execute("SELECT ID FROM Client WHERE Nomer_telephona = %s", (telephone,))
            if cursor.fetchone():
                self.show_message("Ошибка", "Пользователь с таким номером уже зарегистрирован!", QMessageBox.Warning)
                return

            cursor.execute("SELECT MAX(ID) AS max_id FROM Client")
            result = cursor.fetchone()
            new_id = (result[0] or 0) + 1

            cursor.execute("""
                INSERT INTO autosalon.client 
                (ID, Familia, Imya, Otchestvo, Data_rozhdenia, Nomer_telephona, Pass)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (new_id, familia, imya, otchestvo, "2000-10-10", telephone, password))

            connection.commit()
            connection.close()

            self.show_message("Успех", "Регистрация прошла успешно!", QMessageBox.Information)
            self.close()

        except Exception as e:
            self.show_message("Ошибка БД", f"Не удалось подключиться к базе данных:\n{str(e)}", QMessageBox.Critical)

class AvtoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.setWindowTitle("Автоцентр — Каталог автомобилей")
        self.setWindowIcon(QIcon(str("Icon.png")))
        self.setStyleSheet(AUTO_SALON_STYLE)

        self.ui.tableView.setStyleSheet("""
                   QTableView {
                       border: 1px solid #ccc;
                       gridline-color: #eee;
                       font-size: 13px;
                   }
                   QTableView::item {
                       padding: 8px;
                   }
               """)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setVisible(False)

        self.ui.lineEdit.setPlaceholderText("Введите модель для поиска...")

        self.ui.pushButton.clicked.connect(self.filtration)
        self.ui.pushButton_2.clicked.connect(self.load_avto)
        self.ui.pushButton_3.clicked.connect(self.close)

        self.load_avto()

    def on_selection_changed(self):
        selection = self.ui.tableView.selectionModel()
        if not selection.hasSelection():
            self.ui.photo_label.clear()
            self.ui.photo_label.setText("Фото\nавтомобиля")
            return

        index = selection.selectedRows()[0] if selection.selectedRows() else selection.selectedIndexes()[0]
        row = index.row()

        model = self.ui.tableView.model()
        if not model:
            return

        photo_col = model.columnCount() - 1
        photo_path = model.index(row, photo_col).data()

        if photo_path and isinstance(photo_path, str):
            pixmap = QPixmap(photo_path)
            if not pixmap.isNull():
                scaled = pixmap.scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.photo_label.setPixmap(scaled)
                return

        self.ui.photo_label.clear()
        self.ui.photo_label.setText("Нет\nфото")

    def close_form(self):
        self.close()

    def filtration(self):
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
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(column_names)

        for row_data in rows:
            items = []
            for cell in row_data:
                item = QStandardItem(str(cell) if cell is not None else "")
                item.setEditable(False)
                items.append(item)
            model.appendRow(items)

        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()

    def load_avto(self):
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT automobile.id as Номер, Cvet.Nazvanie as Цвет, Marka.Nazvanie AS Название, Model AS Модель, Obiem_dvigatelya AS Объём_двигателя, Complectacia AS Комплектация, Stoimost AS Стоимость, Foto AS Фото FROM automobile INNER JOIN Marka ON Marka.id = automobile.Marka INNER JOIN Cvet ON Cvet.id = automobile.Cvet")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(column_names)

        for row_data in rows:
            items = []
            for cell in row_data:
                item = QStandardItem(str(cell) if cell is not None else "")
                item.setEditable(False)
                items.append(item)
            model.appendRow(items)

        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Автоцентр — Авторизация")
        self.setWindowIcon(QIcon("Icon.png"))
        self.setFixedSize(380, 700)
        self.setStyleSheet(AUTO_SALON_STYLE)
        self.init_ui()

    def init_ui(self):
        font = QFont()
        font.setPointSize(14)

        self.logo_label = QLabel()
        pixmap = QPixmap("Logo.png")
        scaled_pixmap = pixmap.scaled(
            300, 150,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.login_label = QLabel("Логин:")
        self.login_label.setFont(font)
        self.login_input = QLineEdit()
        self.login_input.setFont(font)
        self.login_input.setFixedHeight(50)
        self.login_input.setPlaceholderText("Номер телефона или логин")

        self.password_label = QLabel("Пароль:")
        self.password_label.setFont(font)
        self.password_input = QLineEdit()
        self.password_input.setFont(font)
        self.password_input.setFixedHeight(50)
        self.password_input.setPlaceholderText("••••••••")
        self.password_input.setEchoMode(QLineEdit.Password)

        # Кнопка "Показать/Скрыть пароль"
        self.toggle_password_button = QPushButton("Показать")
        self.toggle_password_button.setFixedWidth(100)
        self.toggle_password_button.setCheckable(True)
        self.toggle_password_button.clicked.connect(self.toggle_password_visibility)

        # Горизонтальный layout для поля пароля и кнопки
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.toggle_password_button)

        self.combo_box_label = QLabel("Роль:")
        self.combo_box_label.setFont(font)
        self.combo_box = QComboBox()
        self.combo_box.setFont(font)
        self.combo_box.setFixedHeight(50)
        self.combo_box.addItems(["Сотрудник", "Клиент"])

        self.button_login = QPushButton("Войти")
        self.button_login.setFont(font)
        self.button_login.setFixedHeight(50)
        self.button_login.setObjectName("button_login")

        self.button_registration = QPushButton("Регистрация")
        self.button_registration.setFont(font)
        self.button_registration.setFixedHeight(50)
        self.button_registration.setObjectName("button_registration")

        self.button_check_avtomobile = QPushButton("Просмотр автомобилей")
        self.button_check_avtomobile.setFont(font)
        self.button_check_avtomobile.setFixedHeight(50)
        self.button_check_avtomobile.setObjectName("button_check_avtomobile")

        self.button_exit = QPushButton("Выход")
        self.button_exit.setFont(font)
        self.button_exit.setFixedHeight(50)
        self.button_exit.setObjectName("button_exit")

        # Подключение сигналов
        self.button_exit.clicked.connect(self.close)
        self.button_login.clicked.connect(self.autorisation_app)
        self.button_check_avtomobile.clicked.connect(self.show_f1)
        self.button_registration.clicked.connect(self.show_f2)

        # Основной layout
        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.addWidget(self.logo_label)
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addLayout(password_layout)  # ← здесь добавляем горизонтальный layout
        layout.addWidget(self.combo_box_label)
        layout.addWidget(self.combo_box)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_registration)
        layout.addWidget(self.button_check_avtomobile)
        layout.addWidget(self.button_exit)
        self.setLayout(layout)

    def toggle_password_visibility(self):
        """Переключает режим отображения пароля."""
        if self.toggle_password_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.toggle_password_button.setText("Скрыть")
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.toggle_password_button.setText("Показать")

    def show_f2(self):
        self.reg_window = RegForm()
        self.reg_window.show()

    def show_f1(self):
        self.avto_window = AvtoForm()
        self.avto_window.show()

    def close_app(self):
        self.close()

    def autorisation_app(self):
        login = self.login_input.text().strip()
        password = self.password_input.text()
        role = self.combo_box.currentText()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        connection = None
        try:
            connection = pymysql.connect(**DB_CONFIG)
            cursor = connection.cursor()

            if role == "Сотрудник":
                cursor.execute(
                    "SELECT ID, Familia, Imya, Otchestvo, Dolzhnost FROM Sotrudnik WHERE login = %s AND pass = %s",
                    (login, password)
                )
                result = cursor.fetchone()

                if result:
                    user_id, f, i, o, user_role = result
                    full_name = f"{f} {i} {o}"

                    if user_role == 7:
                        self.admin_window = AddStaffForm()
                        self.admin_window.show()
                    else:
                        self.staff_window = StaffCabinetForm(full_name)
                        self.staff_window.show()

                    self.close()
                else:
                    QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль для сотрудника!")

            else:  # Клиент
                cursor.execute(
                    "SELECT ID, Familia, Imya, Otchestvo FROM Client WHERE Nomer_telephona = %s AND pass = %s",
                    (login, password)
                )
                result = cursor.fetchone()

                if result:
                    user_id, f, i, o = result
                    self.cabinet_window = ClientCabinetForm(user_id, f"{f} {i} {o}")
                    self.cabinet_window.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "Ошибка", "Неверный номер телефона или пароль для клиента!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка подключения к базе данных:\n{str(e)}")
            print("DB Error:", e)
        finally:
            if connection:
                connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec())