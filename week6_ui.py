# Form implementation generated from reading ui file 'd:\0\SEMESTER 6\Pemrograman Visual (S6)\Tugas\week6.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FontAdjuster(object):
    def setupUi(self, FontAdjuster):
        FontAdjuster.setObjectName("FontAdjuster")
        FontAdjuster.resize(520, 480)
        self.centralwidget = QtWidgets.QWidget(parent=FontAdjuster)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.labelNIM = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNIM.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelNIM.setMinimumHeight(100)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.labelNIM.setFont(font)
        self.labelNIM.setAutoFillBackground(True)
        self.labelNIM.setObjectName("labelNIM")
        self.mainLayout.addWidget(self.labelNIM)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.labelFontSizeTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFontSizeTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelFontSizeTitle.setObjectName("labelFontSizeTitle")
        self.vboxlayout.addWidget(self.labelFontSizeTitle)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.labelFontMin = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFontMin.setObjectName("labelFontMin")
        self.hboxlayout.addWidget(self.labelFontMin)
        self.sliderFontSize = QtWidgets.QSlider(parent=self.centralwidget)
        self.sliderFontSize.setMinimum(20)
        self.sliderFontSize.setMaximum(60)
        self.sliderFontSize.setProperty("value", 30)
        self.sliderFontSize.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sliderFontSize.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.sliderFontSize.setTickInterval(5)
        self.sliderFontSize.setObjectName("sliderFontSize")
        self.hboxlayout.addWidget(self.sliderFontSize)
        self.labelFontMax = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFontMax.setObjectName("labelFontMax")
        self.hboxlayout.addWidget(self.labelFontMax)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.mainLayout.addLayout(self.vboxlayout)
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.labelBgColorTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelBgColorTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelBgColorTitle.setObjectName("labelBgColorTitle")
        self.vboxlayout1.addWidget(self.labelBgColorTitle)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.hboxlayout1.addWidget(self.label)
        self.sliderBgColor = QtWidgets.QSlider(parent=self.centralwidget)
        self.sliderBgColor.setMinimum(0)
        self.sliderBgColor.setMaximum(255)
        self.sliderBgColor.setProperty("value", 0)
        self.sliderBgColor.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sliderBgColor.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.sliderBgColor.setTickInterval(25)
        self.sliderBgColor.setObjectName("sliderBgColor")
        self.hboxlayout1.addWidget(self.sliderBgColor)
        self.label1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label1.setObjectName("label1")
        self.hboxlayout1.addWidget(self.label1)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.mainLayout.addLayout(self.vboxlayout1)
        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.labelFontColorTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFontColorTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelFontColorTitle.setObjectName("labelFontColorTitle")
        self.vboxlayout2.addWidget(self.labelFontColorTitle)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.label2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label2.setObjectName("label2")
        self.hboxlayout2.addWidget(self.label2)
        self.sliderFontColor = QtWidgets.QSlider(parent=self.centralwidget)
        self.sliderFontColor.setMinimum(0)
        self.sliderFontColor.setMaximum(255)
        self.sliderFontColor.setProperty("value", 255)
        self.sliderFontColor.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sliderFontColor.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.sliderFontColor.setTickInterval(25)
        self.sliderFontColor.setObjectName("sliderFontColor")
        self.hboxlayout2.addWidget(self.sliderFontColor)
        self.label3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label3.setObjectName("label3")
        self.hboxlayout2.addWidget(self.label3)
        self.vboxlayout2.addLayout(self.hboxlayout2)
        self.mainLayout.addLayout(self.vboxlayout2)
        self.labelNamaNIM = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNamaNIM.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.labelNamaNIM.setStyleSheet("color: gray; font-size: 10pt;")
        self.labelNamaNIM.setObjectName("labelNamaNIM")
        self.mainLayout.addWidget(self.labelNamaNIM)
        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 1)
        self.mainLayout.setStretch(2, 1)
        self.mainLayout.setStretch(3, 1)
        FontAdjuster.setCentralWidget(self.centralwidget)

        self.retranslateUi(FontAdjuster)
        QtCore.QMetaObject.connectSlotsByName(FontAdjuster)

    def retranslateUi(self, FontAdjuster):
        _translate = QtCore.QCoreApplication.translate
        FontAdjuster.setWindowTitle(_translate("FontAdjuster", "Font Size and Color Adjuster"))
        self.labelNIM.setText(_translate("FontAdjuster", "F1D022122"))
        self.labelFontSizeTitle.setText(_translate("FontAdjuster", "Font Size"))
        self.labelFontMin.setText(_translate("FontAdjuster", "20"))
        self.labelFontMax.setText(_translate("FontAdjuster", "60"))
        self.labelBgColorTitle.setText(_translate("FontAdjuster", "Background Color"))
        self.label.setText(_translate("FontAdjuster", "0"))
        self.label1.setText(_translate("FontAdjuster", "255"))
        self.labelFontColorTitle.setText(_translate("FontAdjuster", "Font Color"))
        self.label2.setText(_translate("FontAdjuster", "0"))
        self.label3.setText(_translate("FontAdjuster", "255"))
        self.labelNamaNIM.setText(_translate("FontAdjuster", "Hendra Ahmad Yani - F1D022122"))
