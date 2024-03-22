# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guideFrom.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_guideFrom(object):
    def setupUi(self, guideFrom):
        if not guideFrom.objectName():
            guideFrom.setObjectName(u"guideFrom")
        guideFrom.resize(491, 356)
        self.gridLayout = QGridLayout(guideFrom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.onebtn = QPushButton(guideFrom)
        self.onebtn.setObjectName(u"onebtn")
        self.onebtn.setMinimumSize(QSize(150, 80))

        self.gridLayout.addWidget(self.onebtn, 0, 0, 1, 1)

        self.twobtn = QPushButton(guideFrom)
        self.twobtn.setObjectName(u"twobtn")
        self.twobtn.setMinimumSize(QSize(150, 80))

        self.gridLayout.addWidget(self.twobtn, 0, 1, 1, 1)

        self.threebtn = QPushButton(guideFrom)
        self.threebtn.setObjectName(u"threebtn")
        self.threebtn.setMinimumSize(QSize(150, 80))

        self.gridLayout.addWidget(self.threebtn, 1, 0, 1, 1)

        self.fourbtn = QPushButton(guideFrom)
        self.fourbtn.setObjectName(u"fourbtn")
        self.fourbtn.setMinimumSize(QSize(150, 80))

        self.gridLayout.addWidget(self.fourbtn, 1, 1, 1, 1)

        self.fivebtn = QPushButton(guideFrom)
        self.fivebtn.setObjectName(u"fivebtn")
        self.fivebtn.setMinimumSize(QSize(150, 80))

        self.gridLayout.addWidget(self.fivebtn, 2, 0, 1, 1)

        self.sixbtn = QPushButton(guideFrom)
        self.sixbtn.setObjectName(u"sixbtn")
        self.sixbtn.setMinimumSize(QSize(150, 80))

        self.gridLayout.addWidget(self.sixbtn, 2, 1, 1, 1)


        self.retranslateUi(guideFrom)

        QMetaObject.connectSlotsByName(guideFrom)
    # setupUi

    def retranslateUi(self, guideFrom):
        guideFrom.setWindowTitle(QCoreApplication.translate("guideFrom", u"\u5f00\u59cb", None))
        self.onebtn.setText(QCoreApplication.translate("guideFrom", u"\u4e86\u89e3\u51b7\u6324\u538b\u5f3a\u5316\u6280\u672f", None))
        self.twobtn.setText(QCoreApplication.translate("guideFrom", u"\u5f00\u7f1d\u886c\u5957\u51b7\u6324\u538b\u5de5\u827a\u786c\u4ef6\u7ec4\u6210", None))
        self.threebtn.setText(QCoreApplication.translate("guideFrom", u"\u5f00\u7f1d\u886c\u5957\u51b7\u6324\u538b\u5de5\u827a\u8bd5\u9a8c\u8fc7\u7a0b", None))
        self.fourbtn.setText(QCoreApplication.translate("guideFrom", u"\u5f00\u7f1d\u886c\u5957\u7684\u5236\u5907\u6280\u672f", None))
        self.fivebtn.setText(QCoreApplication.translate("guideFrom", u"\u5f00\u7f1d\u886c\u5957\u51b7\u6324\u538b\u5f3a\u5316\u5de5\u827a\u53c2\u6570", None))
        self.sixbtn.setText(QCoreApplication.translate("guideFrom", u"\u5f00\u7f1d\u886c\u5957\u5e94\u529b\u5e94\u53d8\u60c5\u51b5\u5206\u6790", None))
    # retranslateUi

