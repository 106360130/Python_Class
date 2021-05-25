from PyQt5 import QtWidgets, QtCore, QtGui


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignLeft)

        self.setFont(QtGui.QFont("微軟正黑體", font_size, QtGui.QFont.Bold))
        self.setText(content)

class HintLabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignLeft)

        self.setFont(QtGui.QFont("微軟正黑體", font_size, QtGui.QFont.Bold))
        self.setText(content)
        self.setStyleSheet("color:red")


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16):
        super().__init__()
        #self.setAlignment(QtCore.Qt.AlignLeft)
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))
        


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))
        self.setEnabled(False)  #初始設定將btn不能按


