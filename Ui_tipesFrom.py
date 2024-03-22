# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tipesFrom.ui'
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

class Ui_tipesFrom(object):
    def setupUi(self, tipesFrom):
        if not tipesFrom.objectName():
            tipesFrom.setObjectName(u"tipesFrom")
        tipesFrom.resize(400, 300)
        self.gridLayout = QGridLayout(tipesFrom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(tipesFrom)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.tipeslab = QLabel(tipesFrom)
        self.tipeslab.setObjectName(u"tipeslab")
        font = QFont()
        font.setPointSize(15)
        self.tipeslab.setFont(font)
        self.tipeslab.setWordWrap(True)

        self.gridLayout.addWidget(self.tipeslab, 0, 1, 1, 1)

        self.widget_2 = QWidget(tipesFrom)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.widget_2, 0, 3, 1, 1)

        self.starbtn = QPushButton(tipesFrom)
        self.starbtn.setObjectName(u"starbtn")

        self.gridLayout.addWidget(self.starbtn, 1, 0, 1, 4)


        self.retranslateUi(tipesFrom)

        QMetaObject.connectSlotsByName(tipesFrom)
    # setupUi

    def retranslateUi(self, tipesFrom):
        tipesFrom.setWindowTitle(QCoreApplication.translate("tipesFrom", u"\u6b22\u8fce", None))
        self.tipeslab.setText(QCoreApplication.translate("tipesFrom", u"    \u63a5\u4e0b\u6765\u6211\u4eec\u5c06\u4e86\u89e3\u51b7\u6324\u538b\u6280\u672f\u548c\u5f00\u7f1d\u886c\u5957\u7ed3\u6784\u4e0e\u5b89\u88c5\u8fc7\u7a0b\uff0c\u5e76\u5bf9\u5f00\u7f1d\u886c\u5957\u8fdb\u884c\u7b80\u5355\u7684\u53d7\u529b\u5206\u6790\uff0c\u4f7f\u7528\u6237\u53ef\u4ee5\u7b80\u5355\u4e86\u89e3\u5f00\u7f1d\u886c\u5957\u7684\u7ed3\u6784\u539f\u7406\uff0c\u5f62\u6210\u5bf9\u51b7\u6324\u538b\u5f3a\u5316\u6280\u672f\u548c\u5f00\u7f1d\u886c\u5957\u7684\u521d\u6b65\u4e86\u89e3\u3002", None))
        self.starbtn.setText(QCoreApplication.translate("tipesFrom", u"\u5f00\u59cb", None))
    # retranslateUi

