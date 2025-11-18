from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget,QFormLayout, QVBoxLayout, QHBoxLayout)

class Ui_Form2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")

        main_layout = QVBoxLayout(Form)
        main_layout.setContentsMargins(30, 20, 30, 20)
        main_layout.setSpacing(12)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignLeft)
        form_layout.setSpacing(15)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)

        font = QFont()
        font.setPointSize(14)

        self.label = QLabel("Фамилия")
        self.label.setFont(font)
        self.lineEdit = QLineEdit()
        self.lineEdit.setFont(font)
        self.lineEdit.setFixedHeight(40)
        form_layout.addRow(self.label, self.lineEdit)

        self.label_2 = QLabel("Имя")
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFixedHeight(40)
        form_layout.addRow(self.label_2, self.lineEdit_2)

        self.label_3 = QLabel("Отчество")
        self.label_3.setFont(font)
        self.lineEdit_3 = QLineEdit()
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFixedHeight(40)
        form_layout.addRow(self.label_3, self.lineEdit_3)

        self.label_7 = QLabel("Телефон")
        self.label_7.setFont(font)
        self.lineEdit_6 = QLineEdit()
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setFixedHeight(40)
        self.lineEdit_6.setInputMask("+7(999)999-99-99")
        form_layout.addRow(self.label_7, self.lineEdit_6)

        self.label_4 = QLabel("Дата рождения")
        self.label_4.setFont(font)
        self.dateEdit = QDateEdit()
        self.dateEdit.setFont(font)
        self.dateEdit.setFixedHeight(40)
        self.dateEdit.setCalendarPopup(True)
        form_layout.addRow(self.label_4, self.dateEdit)

        self.label_5 = QLabel("Пароль")
        self.label_5.setFont(font)
        self.lineEdit_4 = QLineEdit()
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFixedHeight(40)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.label_5, self.lineEdit_4)

        self.label_6 = QLabel("Подтверждение пароля")
        self.label_6.setFont(font)
        self.lineEdit_5 = QLineEdit()
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFixedHeight(40)
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.label_6, self.lineEdit_5)

        main_layout.addLayout(form_layout)
        main_layout.addStretch()

        button_layout = QHBoxLayout()
        self.pushButton = QPushButton("Регистрация")
        self.pushButton.setFont(font)
        self.pushButton.setFixedHeight(50)

        self.pushButton_2 = QPushButton("Отмена")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFixedHeight(50)

        button_layout.addWidget(self.pushButton)
        button_layout.addWidget(self.pushButton_2)

        main_layout.addLayout(button_layout)

        self.retranslateUi(Form)
        Form.setLayout(main_layout)

        from PySide6.QtCore import QMetaObject
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Автоцентр — Регистрация", None))