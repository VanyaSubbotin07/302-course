from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QPushButton,
                               QSizePolicy, QTableView, QWidget, QLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1250, 536)
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(30, 20, 931, 411))

        self.photo_label = QLabel(Form)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setGeometry(QRect(970, 20, 250, 250))
        self.photo_label.setStyleSheet("border: 1px solid #ccc; background: white;")
        self.pixmap = QPixmap("1.png")
        if self.pixmap.isNull():
            self.photo_label.setText("Фото\nне\nзагружено")
        else:
            scaled = self.pixmap.scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.photo_label.setPixmap(scaled)
        self.photo_label.setAlignment(Qt.AlignCenter)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 450, 301, 50))
        font = QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 450, 150, 50))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 450, 150, 50))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(810, 450, 150, 50))
        self.pushButton_3.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Автоцентр — Каталог", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Найти", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Сброс", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Назад", None))