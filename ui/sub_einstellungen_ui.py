# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Rainer\PycharmProjects\Akuvet\ui\sub_einstellungen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(905, 599)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tb_einstellungen = QtWidgets.QToolBox(Frame)
        self.tb_einstellungen.setObjectName("tb_einstellungen")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 887, 365))
        self.page_1.setObjectName("page_1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame = QtWidgets.QFrame(self.page_1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnSave = QtWidgets.QPushButton(self.frame)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_3.addWidget(self.btnSave)
        self.btnCancel = QtWidgets.QPushButton(self.frame)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_25 = QtWidgets.QSplitter(self.frame)
        self.splitter_25.setOrientation(QtCore.Qt.Vertical)
        self.splitter_25.setObjectName("splitter_25")
        self.tb_pg1_la12 = QtWidgets.QLabel(self.splitter_25)
        self.tb_pg1_la12.setObjectName("tb_pg1_la12")
        self.tb_pg1_le12 = QtWidgets.QLineEdit(self.splitter_25)
        self.tb_pg1_le12.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le12.setObjectName("tb_pg1_le12")
        self.gridLayout_2.addWidget(self.splitter_25, 4, 1, 1, 1)
        self.splitter_24 = QtWidgets.QSplitter(self.frame)
        self.splitter_24.setOrientation(QtCore.Qt.Vertical)
        self.splitter_24.setObjectName("splitter_24")
        self.tb_pg1_la10 = QtWidgets.QLabel(self.splitter_24)
        self.tb_pg1_la10.setObjectName("tb_pg1_la10")
        self.tb_pg1_le10 = QtWidgets.QLineEdit(self.splitter_24)
        self.tb_pg1_le10.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le10.setObjectName("tb_pg1_le10")
        self.gridLayout_2.addWidget(self.splitter_24, 3, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter_22 = QtWidgets.QSplitter(self.frame)
        self.splitter_22.setOrientation(QtCore.Qt.Vertical)
        self.splitter_22.setObjectName("splitter_22")
        self.tb_pg1_la7 = QtWidgets.QLabel(self.splitter_22)
        self.tb_pg1_la7.setObjectName("tb_pg1_la7")
        self.tb_pg1_le7 = QtWidgets.QLineEdit(self.splitter_22)
        self.tb_pg1_le7.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le7.setObjectName("tb_pg1_le7")
        self.horizontalLayout_7.addWidget(self.splitter_22)
        self.splitter_23 = QtWidgets.QSplitter(self.frame)
        self.splitter_23.setOrientation(QtCore.Qt.Vertical)
        self.splitter_23.setObjectName("splitter_23")
        self.tb_pg1_la8 = QtWidgets.QLabel(self.splitter_23)
        self.tb_pg1_la8.setObjectName("tb_pg1_la8")
        self.tb_pg1_le8 = QtWidgets.QLineEdit(self.splitter_23)
        self.tb_pg1_le8.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le8.setObjectName("tb_pg1_le8")
        self.horizontalLayout_7.addWidget(self.splitter_23)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.splitter_20 = QtWidgets.QSplitter(self.frame)
        self.splitter_20.setOrientation(QtCore.Qt.Vertical)
        self.splitter_20.setObjectName("splitter_20")
        self.tb_pg1_la4 = QtWidgets.QLabel(self.splitter_20)
        self.tb_pg1_la4.setObjectName("tb_pg1_la4")
        self.tb_pg1_le4 = QtWidgets.QLineEdit(self.splitter_20)
        self.tb_pg1_le4.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le4.setObjectName("tb_pg1_le4")
        self.horizontalLayout_6.addWidget(self.splitter_20)
        self.splitter_21 = QtWidgets.QSplitter(self.frame)
        self.splitter_21.setOrientation(QtCore.Qt.Vertical)
        self.splitter_21.setObjectName("splitter_21")
        self.tb_pg1_la5 = QtWidgets.QLabel(self.splitter_21)
        self.tb_pg1_la5.setObjectName("tb_pg1_la5")
        self.tb_pg1_le5 = QtWidgets.QLineEdit(self.splitter_21)
        self.tb_pg1_le5.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le5.setObjectName("tb_pg1_le5")
        self.horizontalLayout_6.addWidget(self.splitter_21)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.splitter_17 = QtWidgets.QSplitter(self.frame)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName("splitter_17")
        self.tb_pg1_la6 = QtWidgets.QLabel(self.splitter_17)
        self.tb_pg1_la6.setObjectName("tb_pg1_la6")
        self.tb_pg1_le6 = QtWidgets.QLineEdit(self.splitter_17)
        self.tb_pg1_le6.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le6.setObjectName("tb_pg1_le6")
        self.gridLayout_2.addWidget(self.splitter_17, 2, 0, 1, 1)
        self.splitter_18 = QtWidgets.QSplitter(self.frame)
        self.splitter_18.setOrientation(QtCore.Qt.Vertical)
        self.splitter_18.setObjectName("splitter_18")
        self.tb_pg1_la9 = QtWidgets.QLabel(self.splitter_18)
        self.tb_pg1_la9.setObjectName("tb_pg1_la9")
        self.tb_pg1_le9 = QtWidgets.QLineEdit(self.splitter_18)
        self.tb_pg1_le9.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le9.setObjectName("tb_pg1_le9")
        self.gridLayout_2.addWidget(self.splitter_18, 3, 0, 1, 1)
        self.splitter_19 = QtWidgets.QSplitter(self.frame)
        self.splitter_19.setOrientation(QtCore.Qt.Vertical)
        self.splitter_19.setObjectName("splitter_19")
        self.tb_pg1_la11 = QtWidgets.QLabel(self.splitter_19)
        self.tb_pg1_la11.setObjectName("tb_pg1_la11")
        self.tb_pg1_le11 = QtWidgets.QLineEdit(self.splitter_19)
        self.tb_pg1_le11.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le11.setObjectName("tb_pg1_le11")
        self.gridLayout_2.addWidget(self.splitter_19, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter_14 = QtWidgets.QSplitter(self.frame)
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName("splitter_14")
        self.tb_pg1_la1 = QtWidgets.QLabel(self.splitter_14)
        self.tb_pg1_la1.setObjectName("tb_pg1_la1")
        self.tb_pg1_le1 = QtWidgets.QLineEdit(self.splitter_14)
        self.tb_pg1_le1.setMinimumSize(QtCore.QSize(0, 20))
        self.tb_pg1_le1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le1.setObjectName("tb_pg1_le1")
        self.horizontalLayout_5.addWidget(self.splitter_14)
        self.splitter_15 = QtWidgets.QSplitter(self.frame)
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName("splitter_15")
        self.tb_pg1_la2 = QtWidgets.QLabel(self.splitter_15)
        self.tb_pg1_la2.setObjectName("tb_pg1_la2")
        self.tb_pg1_le2 = QtWidgets.QLineEdit(self.splitter_15)
        self.tb_pg1_le2.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le2.setObjectName("tb_pg1_le2")
        self.horizontalLayout_5.addWidget(self.splitter_15)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.splitter_16 = QtWidgets.QSplitter(self.frame)
        self.splitter_16.setOrientation(QtCore.Qt.Vertical)
        self.splitter_16.setObjectName("splitter_16")
        self.tb_pg1_la0 = QtWidgets.QLabel(self.splitter_16)
        self.tb_pg1_la0.setObjectName("tb_pg1_la0")
        self.tb_pg1_le0 = QtWidgets.QLineEdit(self.splitter_16)
        self.tb_pg1_le0.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le0.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le0.setObjectName("tb_pg1_le0")
        self.gridLayout_2.addWidget(self.splitter_16, 0, 0, 1, 1)
        self.splitter_26 = QtWidgets.QSplitter(self.frame)
        self.splitter_26.setOrientation(QtCore.Qt.Vertical)
        self.splitter_26.setObjectName("splitter_26")
        self.tb_pg1_la3 = QtWidgets.QLabel(self.splitter_26)
        self.tb_pg1_la3.setObjectName("tb_pg1_la3")
        self.tb_pg1_le3 = QtWidgets.QLineEdit(self.splitter_26)
        self.tb_pg1_le3.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le3.setObjectName("tb_pg1_le3")
        self.gridLayout_2.addWidget(self.splitter_26, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
        self.tb_einstellungen.addItem(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 887, 365))
        self.page_2.setObjectName("page_2")
        self.tb_einstellungen.addItem(self.page_2, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 887, 365))
        self.page_5.setObjectName("page_5")
        self.tb_einstellungen.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 887, 365))
        self.page_6.setObjectName("page_6")
        self.tb_einstellungen.addItem(self.page_6, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 887, 365))
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cv_test = QtWidgets.QColumnView(self.page_3)
        self.cv_test.setObjectName("cv_test")
        self.gridLayout_4.addWidget(self.cv_test, 0, 0, 1, 1)
        self.tb_einstellungen.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 887, 365))
        self.page_4.setObjectName("page_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.trwTiere = QtWidgets.QTreeWidget(self.page_4)
        self.trwTiere.setObjectName("trwTiere")
        self.trwTiere.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.trwTiere)
        self.tb_einstellungen.addItem(self.page_4, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 887, 365))
        self.page_7.setObjectName("page_7")
        self.tb_einstellungen.addItem(self.page_7, "")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tb_pg7_la0 = QtWidgets.QLabel(self.splitter)
        self.tb_pg7_la0.setObjectName("tb_pg7_la0")
        self.tb_pg7_le0 = QtWidgets.QLineEdit(self.splitter)
        self.tb_pg7_le0.setObjectName("tb_pg7_le0")
        self.gridLayout_7.addWidget(self.splitter, 1, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.tb_pg7_la1 = QtWidgets.QLabel(self.splitter_2)
        self.tb_pg7_la1.setObjectName("tb_pg7_la1")
        self.tb_pg7_le1 = QtWidgets.QLineEdit(self.splitter_2)
        self.tb_pg7_le1.setObjectName("tb_pg7_le1")
        self.gridLayout_7.addWidget(self.splitter_2, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_7.addWidget(self.comboBox, 0, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.tb_pg7_la2 = QtWidgets.QLabel(self.splitter_3)
        self.tb_pg7_la2.setObjectName("tb_pg7_la2")
        self.tb_pg7_le2 = QtWidgets.QLineEdit(self.splitter_3)
        self.tb_pg7_le2.setObjectName("tb_pg7_le2")
        self.gridLayout_7.addWidget(self.splitter_3, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 1, 0, 1, 1)
        self.tb_einstellungen.addItem(self.page, "")
        self.gridLayout.addWidget(self.tb_einstellungen, 1, 0, 1, 1)

        self.retranslateUi(Frame)
        self.tb_einstellungen.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.btnSave.setText(_translate("Frame", "Speichern"))
        self.btnCancel.setText(_translate("Frame", "Zurücksetzten"))
        self.tb_pg1_la12.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la10.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la7.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la8.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la4.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la5.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la6.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la9.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la11.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la1.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la2.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la0.setText(_translate("Frame", "TextLabel"))
        self.tb_pg1_la3.setText(_translate("Frame", "TextLabel"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page_1), _translate("Frame", "Praxisdaten"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page_2), _translate("Frame", "Medikamente"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page_5), _translate("Frame", "Verwaltung Diagnosen"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page_6), _translate("Frame", "Tierärtlicheleistungen und GOT"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page_3), _translate("Frame", "Vorlagen Behandlungen"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page_4), _translate("Frame", "Tierarten/ Rassen /Farben"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page_7), _translate("Frame", "Chinesische Kräuter"))
        self.tb_pg7_la0.setText(_translate("Frame", "Postleitzahl"))
        self.tb_pg7_la1.setText(_translate("Frame", "Ort"))
        self.tb_pg7_la2.setText(_translate("Frame", "Ortsteil"))
        self.tb_einstellungen.setItemText(self.tb_einstellungen.indexOf(self.page), _translate("Frame", "Orte"))
