# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'twoForm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_twoForm(object):
    def setupUi(self, twoForm):
        if not twoForm.objectName():
            twoForm.setObjectName(u"twoForm")
        twoForm.resize(452, 529)
        self.gridLayout = QGridLayout(twoForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.piclab = QLabel(twoForm)
        self.piclab.setObjectName(u"piclab")

        self.gridLayout.addWidget(self.piclab, 0, 0, 1, 1)

        self.lab = QLabel(twoForm)
        self.lab.setObjectName(u"lab")
        font = QFont()
        font.setPointSize(15)
        self.lab.setFont(font)
        self.lab.setWordWrap(True)

        self.gridLayout.addWidget(self.lab, 1, 0, 1, 1)

        self.btn = QPushButton(twoForm)
        self.btn.setObjectName(u"btn")

        self.gridLayout.addWidget(self.btn, 2, 0, 1, 1)


        self.retranslateUi(twoForm)

        QMetaObject.connectSlotsByName(twoForm)
    # setupUi

    def retranslateUi(self, twoForm):
        twoForm.setWindowTitle(QCoreApplication.translate("twoForm", u"\u4e86\u89e3\u51b7\u6324\u538b\u5f3a\u5316\u6280\u672f", None))
        self.piclab.setText("")
        self.lab.setText("")
        self.btn.setText("")
    # retranslateUi

