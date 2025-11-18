from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QWidget, QTableView, QLabel, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QSplitter
)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")

        main_layout = QVBoxLayout(Form)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        top_splitter = QSplitter(Qt.Horizontal)
        top_splitter.setHandleWidth(10)

        self.tableView = QTableView()
        self.tableView.setObjectName("tableView")
        self.tableView.setMinimumSize(600, 400)
        top_splitter.addWidget(self.tableView)

        self.photo_label = QLabel()
        self.photo_label.setObjectName("photo_label")
        self.photo_label.setMinimumSize(250, 250)
        self.photo_label.setStyleSheet("border: 1px solid #ccc; background: white;")
        self.pixmap = QPixmap("1.png")
        if self.pixmap.isNull():
            self.photo_label.setText("Фото\nне\nзагружено")
        else:
            scaled = self.pixmap.scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.photo_label.setPixmap(scaled)
        self.photo_label.setAlignment(Qt.AlignCenter)
        top_splitter.addWidget(self.photo_label)

        main_layout.addWidget(top_splitter)

        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(10)

        self.lineEdit = QLineEdit()
        self.lineEdit.setObjectName("lineEdit")
        font = QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText("Введите модель для поиска...")
        bottom_layout.addWidget(self.lineEdit, 3)

        self.pushButton = QPushButton("Найти")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setFixedHeight(50)
        bottom_layout.addWidget(self.pushButton, 1)

        self.pushButton_2 = QPushButton("Сброс")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFixedHeight(50)
        bottom_layout.addWidget(self.pushButton_2, 1)

        bottom_layout.addStretch(1)

        self.pushButton_3 = QPushButton("Назад")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFixedHeight(50)
        self.pushButton_3.setFixedWidth(150)
        bottom_layout.addWidget(self.pushButton_3)

        main_layout.addLayout(bottom_layout)

        self.retranslateUi(Form)
        Form.setLayout(main_layout)

        from PySide6.QtCore import QMetaObject
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        from PySide6.QtCore import QCoreApplication
        Form.setWindowTitle(QCoreApplication.translate("Form", "Автоцентр — Каталог", None))
        self.pushButton.setText(QCoreApplication.translate("Form", "Найти", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", "Сброс", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", "Назад", None))