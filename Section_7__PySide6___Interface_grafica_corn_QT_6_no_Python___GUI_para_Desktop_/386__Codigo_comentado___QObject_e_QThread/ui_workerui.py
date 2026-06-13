# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workerui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_myWidget(object):
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(437, 300)
        self.label1 = QLabel(myWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(0, 130, 81, 51))
        font = QFont()
        font.setPointSize(40)
        self.label1.setFont(font)
        self.label1.setLineWidth(1)
        self.label2 = QLabel(myWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(140, 140, 61, 41))
        self.label2.setFont(font)
        self.label2.setLineWidth(1)
        self.button1 = QPushButton(myWidget)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(30, 243, 91, 51))
        self.button1.setFont(font)
        self.button2 = QPushButton(myWidget)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(274, 243, 91, 51))
        self.button2.setFont(font)

        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"Form", None))
        self.label1.setText(QCoreApplication.translate("myWidget", u"L1", None))
        self.label2.setText(QCoreApplication.translate("myWidget", u"L2", None))
        self.button1.setText(QCoreApplication.translate("myWidget", u"B1", None))
        self.button2.setText(QCoreApplication.translate("myWidget", u"B2", None))
    # retranslateUi

