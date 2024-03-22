# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oneForm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_oneForm(object):
    def setupUi(self, oneForm):
        if not oneForm.objectName():
            oneForm.setObjectName(u"oneForm")
        oneForm.resize(717, 438)
        self.gridLayout = QGridLayout(oneForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lab = QLabel(oneForm)
        self.lab.setObjectName(u"lab")
        font = QFont()
        font.setPointSize(15)
        self.lab.setFont(font)
        self.lab.setAlignment(Qt.AlignCenter)
        self.lab.setWordWrap(True)

        self.horizontalLayout.addWidget(self.lab)

        self.piclab = QLabel(oneForm)
        self.piclab.setObjectName(u"piclab")
        self.piclab.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.piclab)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn = QPushButton(oneForm)
        self.btn.setObjectName(u"btn")

        self.verticalLayout.addWidget(self.btn)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(oneForm)

        QMetaObject.connectSlotsByName(oneForm)
    # setupUi

    def retranslateUi(self, oneForm):
        oneForm.setWindowTitle(QCoreApplication.translate("oneForm", u"\u4e86\u89e3\u51b7\u6324\u538b\u5f3a\u5316\u6280\u672f", None))
        self.lab.setText("")
        self.piclab.setText("")
        self.btn.setText(QCoreApplication.translate("oneForm", u"\u8fde\u63a5", None))
    # retranslateUi

