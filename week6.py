import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class FontAdjusterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("week6.ui", self)
        self.label = self.findChild(QtWidgets.QLabel, "labelNIM")
        self.sliderFontSize = self.findChild(QtWidgets.QSlider, "sliderFontSize")
        self.sliderFontColor = self.findChild(QtWidgets.QSlider, "sliderFontColor")
        self.sliderBgColor = self.findChild(QtWidgets.QSlider, "sliderBgColor")

        self.sliderFontSize.valueChanged.connect(self.updateFontSize)
        self.sliderFontColor.valueChanged.connect(self.updateFontColor)
        self.sliderBgColor.valueChanged.connect(self.updateBgColor)

        self.updateFontSize()
        self.updateFontColor()
        self.updateBgColor()

    def updateFontSize(self):
        size = self.sliderFontSize.value()
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)

    def updateFontColor(self):
        value = self.sliderFontColor.value()
        color = QColor(value, value, value)  
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, color)
        self.label.setPalette(palette)

    def updateBgColor(self):
        value = self.sliderBgColor.value()
        color = QColor(value, value, value) 
        palette = self.label.palette()
        palette.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FontAdjusterApp()
    window.show()
    sys.exit(app.exec_())
