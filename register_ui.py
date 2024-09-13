# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_RegisterWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(199, 229)
        MainWindow.setStyleSheet(u"background-color: black; \n"
"background: #2C2D2F;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name_line = QLineEdit(self.centralwidget)
        self.name_line.setObjectName(u"name_line")
        self.name_line.setGeometry(QRect(30, 40, 140, 25))
        self.name_line.setStyleSheet(u"border-radius: 30px; \n"
"background: white; ")
        self.surname_line = QLineEdit(self.centralwidget)
        self.surname_line.setObjectName(u"surname_line")
        self.surname_line.setGeometry(QRect(30, 90, 140, 25))
        self.surname_line.setStyleSheet(u"border: 20px; \n"
"background-color: white; ")
        self.old_line = QLineEdit(self.centralwidget)
        self.old_line.setObjectName(u"old_line")
        self.old_line.setGeometry(QRect(30, 140, 140, 25))
        self.old_line.setStyleSheet(u"background-color: white; ")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 175, 141, 31))
        self.pushButton.setStyleSheet(u"background-color: lime; \n"
"color: white; \n"
"border-radius: 24px; ")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(75, 20, 51, 17))
        self.label.setStyleSheet(u"color: white; ")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(63, 70, 81, 17))
        self.label_2.setStyleSheet(u"color: white; ")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 120, 81, 17))
        self.label_3.setStyleSheet(u"color: white; ")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name_line.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0418\u043c\u044f</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412\u043e\u0437\u0440\u0430\u0441\u0442</p></body></html>", None))
    # retranslateUi

