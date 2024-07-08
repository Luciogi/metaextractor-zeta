# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(670, 543)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnAdd = QPushButton(Widget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.verticalLayout.addWidget(self.btnAdd)

        self.btnRemove = QPushButton(Widget)
        self.btnRemove.setObjectName(u"btnRemove")

        self.verticalLayout.addWidget(self.btnRemove)

        self.btnClearAll = QPushButton(Widget)
        self.btnClearAll.setObjectName(u"btnClearAll")

        self.verticalLayout.addWidget(self.btnClearAll)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 2)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_5, 4, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnExtract = QPushButton(Widget)
        self.btnExtract.setObjectName(u"btnExtract")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExtract.sizePolicy().hasHeightForWidth())
        self.btnExtract.setSizePolicy(sizePolicy)
        self.btnExtract.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btnExtract)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)

        self.txtHeader = QLabel(Widget)
        self.txtHeader.setObjectName(u"txtHeader")
        self.txtHeader.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(20)
        font.setBold(True)
        self.txtHeader.setFont(font)
        self.txtHeader.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.txtHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.txtHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.txtHeader.setTextFormat(Qt.TextFormat.MarkdownText)
        self.txtHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txtHeader, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 2, 1, 1)


        self.retranslateUi(Widget)

        self.btnExtract.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Metadata Extractor Zeta", None))
        self.btnAdd.setText(QCoreApplication.translate("Widget", u"+", None))
        self.btnRemove.setText(QCoreApplication.translate("Widget", u"-", None))
        self.btnClearAll.setText(QCoreApplication.translate("Widget", u"Clear All", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Files", None))
        self.btnExtract.setText(QCoreApplication.translate("Widget", u"Extract", None))
        self.txtHeader.setText(QCoreApplication.translate("Widget", u"Metadata Extractor Zeta", None))
    # retranslateUi

